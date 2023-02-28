#!/usr/bin/env python3

"""Manages page redirects for the Godot documentation on ReadTheDocs. (https://docs.godotengine.org)
Note that RTD redirects only apply in case of 404 errors, and to all branches and languages:
https://docs.readthedocs.io/en/stable/user-defined-redirects.html.
If this ever changes, we need to rework how we manage these (likely adding per-branch logic).

How to use:
- Install requirements: pip3 install -r requirements.txt
- Store your API token in RTD_API_TOKEN environment variable or
  a .env file (the latter requires the package dotenv)
- Generate new redirects from two git revisions using convert_git_renames_to_csv.py
- Run this script

Example:
  python convert_git_renames_to_csv.py stable latest >> redirects.csv
  python create_redirects.py

This would add all files that were renamed in latest from stable to redirects.csv,
and then create the redirects on RTD accordingly.
Make sure to use the old branch first, then the more recent branch (i.e., stable > master).
You need to have both branches or revisions available and up to date locally.
Care is taken to not add redirects that already exist on RTD.
"""

import argparse
import csv
import os
import time

import requests
from requests.models import default_hooks
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

RTD_AUTH_TOKEN = ""
REQUEST_HEADERS = ""
REDIRECT_URL = "https://readthedocs.org/api/v3/projects/godot/redirects/"
USER_AGENT = "Godot RTD Redirects on Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
DEFAULT_PAGINATED_SIZE = 1024
API_SLEEP_TIME = 0.2 # Seconds.
REDIRECT_SUFFIXES = [".html", "/"]
BUILD_PATH = "../../_build/html"
TIMEOUT_SECONDS = 5
HTTP = None

def parse_command_line_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "-f",
        "--file",
        metavar="file",
        default="redirects.csv",
        type=str,
        help="Path to a CSV file used to keep a list of redirects, containing two columns: source and destination.",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Deletes all currently setup 'page' and 'exact' redirects on ReadTheDocs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Safe mode: Run the program and output information without any calls to the ReadTheDocs API.",
    )
    parser.add_argument(
        "--dump",
        action="store_true",
        help="Only dumps or deletes (if --delete) existing RTD redirects, skips submission.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enables verbose output.",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validates each redirect by checking the target page exists. Implies --dry-run.",
    )
    return parser.parse_args()

def is_dry_run(args):
    return args.dry_run or args.validate

def validate(destination):
    p = BUILD_PATH + destination
    if not os.path.exists(p):
        print("Invalid destination: " + destination + " (" + p + ")")

def make_redirect(source, destination, args, retry=0):
    if args.validate:
        validate(destination)

    json_data = {"from_url": source, "to_url": destination, "type": "page"}
    headers = REQUEST_HEADERS

    if args.verbose:
        print("POST " + REDIRECT_URL, headers, json_data)

    if is_dry_run(args):
        if not args.validate:
            print(f"Created redirect {source} -> {destination} (DRY RUN)")
        return

    response = HTTP.post(
        REDIRECT_URL,
        json=json_data,
        headers=headers,
        timeout=TIMEOUT_SECONDS
    )

    if response.status_code == 201:
        print(f"Created redirect {source} -> {destination}")
    elif response.status_code == 429 and retry<5:
        retry += 1
        time.sleep(retry*retry)
        make_redirect(source, destination, args, retry)
        return
    else:
        print(
            f"Failed to create redirect {source} -> {destination}. "
            f"Status code: {response.status_code}"
        )
        exit(1)


def sleep():
    time.sleep(API_SLEEP_TIME)


def id(from_url, to_url):
    return from_url + " -> " + to_url


def get_paginated(url, parameters={"limit": DEFAULT_PAGINATED_SIZE}):
    entries = []
    count = -1
    while True:
        data = HTTP.get(
            url,
            headers=REQUEST_HEADERS,
            params=parameters,
            timeout=TIMEOUT_SECONDS
        )
        if data.status_code != 200:
            if data.status_code == 401:
                print("Access denied, check RTD API key in RTD_AUTH_TOKEN!")
            print("Error accessing RTD API: " + url + ": " + str(data.status_code))
            exit(1)
        else:
            json = data.json()
            if json["count"] and count < 0:
                count = json["count"]
            entries.extend(json["results"])
            next = json["next"]
            if next and len(next) > 0 and next != url:
                url = next
                sleep()
                continue
        if count > 0 and len(entries) != count:
            print(
                "Mismatch getting paginated content from " + url + ": " +
                "expected " + str(count) + " items, got " + str(len(entries)))
            exit(1)
        return entries


def delete_redirect(id):
    url = REDIRECT_URL + str(id)
    data = HTTP.delete(url, headers=REQUEST_HEADERS, timeout=TIMEOUT_SECONDS)
    if data.status_code != 204:
        print("Error deleting redirect with ID", id, "- code:", data.status_code)
        exit(1)
    else:
        print("Deleted redirect", id, "on RTD.")


def get_existing_redirects(delete=False):
    redirs = get_paginated(REDIRECT_URL)
    existing = []
    for redir in redirs:
        if redir["type"] != "page":
            print(
                "Ignoring redirect (only type 'page' is handled): #" +
                str(redir["pk"]) + " " + id(redir["from_url"], redir["to_url"]) +
                " on ReadTheDocs is '" + redir["type"] + "'. "
            )
            continue
        if delete:
            delete_redirect(redir["pk"])
            sleep()
        else:
            existing.append([redir["from_url"], redir["to_url"]])
    return existing


def set_auth(token):
    global RTD_AUTH_TOKEN
    RTD_AUTH_TOKEN = token
    global REQUEST_HEADERS
    REQUEST_HEADERS = {"Authorization": f"token {RTD_AUTH_TOKEN}", "User-Agent": USER_AGENT}


def load_auth():
    try:
        import dotenv
        dotenv.load_dotenv()
    except:
        print("Failed to load dotenv. If you want to use .env files, install the dotenv.")
    token = os.environ.get("RTD_AUTH_TOKEN", "")
    if len(token) < 1:
        print("Missing auth token in RTD_AUTH_TOKEN env var or .env file not found. Aborting.")
        exit(1)
    set_auth(token)


def has_suffix(s, suffixes):
    for suffix in suffixes:
        if s.endswith(suffix):
            return True
    return False


def is_valid_redirect_url(url):
    if len(url) < len("/a"):
        return False

    if not has_suffix(url.lower(), REDIRECT_SUFFIXES):
        return False

    return True


def redirect_to_str(item):
    return id(item[0], item[1])


def main():
    args = parse_command_line_args()

    if not is_dry_run(args):
        load_auth()

        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=2,
            method_whitelist=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        global HTTP
        HTTP = requests.Session()
        HTTP.mount("https://", adapter)
        HTTP.mount("http://", adapter)

    to_add = []
    redirects_file = []
    with open(args.file, "r", encoding="utf-8") as f:
        redirects_file = list(csv.DictReader(f))
        if len(redirects_file) > 0:
            assert redirects_file[0].keys() == {
                "source",
                "destination",
            }, "CSV file must have a header and two columns: source, destination."

    for row in redirects_file:
        to_add.append([row["source"], row["destination"]])
    print("Loaded", len(redirects_file), "redirects from", args.file + ".")

    existing = []
    if not is_dry_run(args):
        existing = get_existing_redirects(args.delete)
    print("Loaded", len(existing), "existing redirects from RTD.")

    print("Total redirects:", str(len(to_add)) +
          " new + " + str(len(existing)), "existing =", to_add+existing, "total")

    redirects = []
    added = {}
    sources = {}

    for redirect in to_add:
        if len(redirect) != 2:
            print("Invalid redirect:", redirect, "- expected 2 elements, got:", len(redirect))
            continue

        if redirect[0] == redirect[1]:
            print("Invalid redirect:", redirect, "- redirects to itself!")
            continue

        if not is_valid_redirect_url(redirect[0]) or not is_valid_redirect_url(redirect[1]):
            print("Invalid redirect:", redirect, "- invalid URL!")
            continue

        if not redirect[0].startswith("/") or not redirect[1].startswith("/"):
            print("Invalid redirect:", redirect, "- invalid URL: should start with slash!")
            continue

        if redirect[0] in sources:
            print("Invalid redirect:", redirect,
                  "- collision, source", redirect[0], "already has redirect:",
                  sources[redirect[0]])
            continue

        redirect_id = id(redirect[0], redirect[1])
        if redirect_id in added:
            # Duplicate; skip.
            continue

        added[redirect_id] = True
        sources[redirect[0]] = redirect
        redirects.append(redirect)

    redirects.sort(key=redirect_to_str)

    with open(args.file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([["source", "destination"]])
        writer.writerows(redirects)

    existing_ids = {}
    for e in existing:
        existing_ids[id(e[0], e[1])] = True

    if not args.dump:
        print("Creating redirects.")
        for redirect in redirects:
            if not id(redirect[0], redirect[1]) in existing_ids:
                make_redirect(redirect[0], redirect[1], args)

            if not is_dry_run(args):
                sleep()

    print("Finished creating", len(redirects), "redirects.")

    if is_dry_run(args):
        print("THIS WAS A DRY RUN, NOTHING WAS SUBMITTED TO READTHEDOCS!")


if __name__ == "__main__":
    main()

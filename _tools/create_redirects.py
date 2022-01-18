"""Create page redirects for a specific branch of the docs.

Loads data from a CSV file with three columns: source, destination, branch

Where the source and destination are paths to RST files in the repository.

Pre-requisites:

- You need the dotenv Python module installed. We use this to let you store your
  API auth token privately.
  
  You can install it by running: pip3 install -r requirements.txt

How to use:

- Generate a CSV file from two git revisions using convert_git_renames_to_csv.py
- Store your API token in a .env variable in this directory like so:
  RTD_API_TOKEN=your_token_here
- Run this script, passing it the path to your generated CSV file as an
  argument.

The script directly creates redirects using the CSV data. It does not check if a
redirect already exist or if it's correct.
"""

import argparse
import csv
import json
import os

import dotenv
from requests.models import default_hooks

try:
    import requests
except ImportError:
    print(
        "Required third-party module `requests` not found. "
        "Please install it with `pip install requests` (or `pip3 install requests` on Linux)."
    )


dotenv.load_dotenv()
RTD_AUTH_TOKEN: str = os.environ.get("RTD_AUTH_TOKEN", "")
if RTD_AUTH_TOKEN == "":
    print("Missing auth token in .env file or .env file not found. Aborting.")
    exit(1)

REDIRECT_URL = "https://readthedocs.org/api/v3/projects/pip/redirects/"
REQUEST_HEADERS = {"Authorization": f"token {RTD_AUTH_TOKEN}"}


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description="Create page redirects for a specific branch of the docs."
    )
    parser.add_argument(
        "csv_file",
        type=str,
        help="Path to a CSV file with three columns: source, destination, branch.",
    )
    # add dry-run argument
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Run the program and output information without side effects.",
    )
    return parser.parse_args()


def make_redirect(source, destination, branch, args):
    # Currently, the program only works for the EN version of the docs
    trimmed_source = source.replace(".rst", "")
    trimmed_destination = destination.replace(".rst", "")

    source_slug = f"/en/{branch}/{trimmed_source}"
    destination_slug = f"/en/{branch}/{trimmed_destination}"
    json_data = {"from_url": source_slug, "to_url": destination_slug, "type": "page"}
    if args.dry_run:
        print(f"{source_slug} -> {destination_slug}")
    else:
        response = requests.post(
            REDIRECT_URL,
            json=json.dumps(json_data),
            headers=REQUEST_HEADERS,
        )
        if response.status_code == 201:
            print(f"Created redirect {source_slug} -> {destination_slug}")
        else:
            print(
                f"Failed to create redirect {source_slug} -> {destination_slug}. "
                f"Status code: {response.status_code}"
            )


def main():
    args = parse_command_line_args()
    redirect_data = []
    with open(args.csv_file, "r") as f:
        redirect_data = list(csv.DictReader(f))
    assert redirect_data[0].keys() == {
        "source",
        "destination",
        "branch",
    }, "CSV file must have those three columns: source, destination, branch."
    for row in redirect_data:
        make_redirect(row["source"], row["destination"], row["branch"], args)


if __name__ == "__main__":
    main()

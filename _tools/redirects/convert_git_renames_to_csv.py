#!/usr/bin/env python3

"""Uses Git to list files that were renamed between two revisions and converts
that to a CSV table.

Use it to prepare and double-check data for create_redirects.py.
"""

import subprocess
import argparse
import csv
import sys


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description="Uses Git to list files that were renamed between two revisions and "
        "converts that to a CSV table. Use it to prepare and double-check data for create_redirects.py."
    )
    parser.add_argument(
        "revision1",
        type=str,
        help="Start revision to get renamed files from (old).",
    )
    parser.add_argument(
        "revision2",
        type=str,
        help="End revision to get renamed files from (new).",
    )
    parser.add_argument("-f", "--output-file", type=str, help="Path to the output file")
    return parser.parse_args()


def dict_item_to_str(item):
    s = ""
    for key in item:
        s += item[key]
    return s


def main():
    try:
        subprocess.check_output(["git", "--version"])
    except subprocess.CalledProcessError:
        print("Git not found. It's required to run this program.")
        exit(1)

    args = parse_command_line_args()
    assert args.revision1 != args.revision2, "Revisions must be different."
    for revision in [args.revision1, args.revision2]:
        assert not "/" in revision, "Revisions must be local branches only."

    # Ensure that both revisions are present in the local repository.
    for revision in [args.revision1, args.revision2]:
        try:
            subprocess.check_output(
                ["git", "rev-list", f"HEAD..{revision}"], stderr=subprocess.STDOUT
            )
        except subprocess.CalledProcessError:
            print(
                f"Revision {revision} not found in this repository. "
                "Please make sure that both revisions exist locally in your Git repository."
            )
            exit(1)

    # Get the list of renamed files between the two revisions.
    renamed_files = (
        subprocess.check_output(
            [
                "git",
                "diff",
                "--find-renames",
                "--name-status",
                "--diff-filter=R",
                args.revision1,
                args.revision2,
            ]
        )
        .decode("utf-8")
        .split("\n")
    )
    renamed_documents = [f for f in renamed_files if f.lower().endswith(".rst")]

    csv_data: list[dict] = []

    for document in renamed_documents:
        _, source, destination = document.split("\t")
        source = source.replace(".rst", ".html")
        destination = destination.replace(".rst", ".html")
        if not source.startswith("/"):
            source = "/" + source
        if not destination.startswith("/"):
            destination = "/" + destination
        csv_data.append(
            {"source": source, "destination": destination}
        )

    if len(csv_data) < 1:
        print("No renames found for", args.revision1, "->", args.revision2)
        return

    csv_data.sort(key=dict_item_to_str)

    out = args.output_file
    if not out:
        out = sys.stdout.fileno()

    with open(out, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
        writer.writeheader()
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()

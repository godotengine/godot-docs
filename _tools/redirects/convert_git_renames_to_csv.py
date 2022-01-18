"""Uses git to list files that were renamed between two revisions and converts
that to a CSV table.

Use it to prepare and double-check data for create_redirects.py.
"""

import subprocess
import argparse
import csv
import sys

try:
    subprocess.check_output(["git", "--version"])
except subprocess.CalledProcessError:
    print("Git not found. It's required to run this program.")


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description="Uses git to list files that were renamed between two revisions and "
        "converts that to a CSV table. Use it to prepare and double-check data for create_redirects.py."
    )
    parser.add_argument(
        "revision1",
        type=str,
        help="Start revision to get renamed files from.",
    )
    parser.add_argument(
        "revision2",
        type=str,
        help="End revision to get renamed files from.",
    )
    parser.add_argument("-f", "--output-file", type=str, help="Path to the output file")
    return parser.parse_args()


def main():
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
                "Please make sure that both revisions exist locally in your git repository."
            )
            exit(1)

    # Get the list of renamed files between the two revisions.
    renamed_files = (
        subprocess.check_output(
            [
                "git",
                "diff",
                "--name-status",
                "--diff-filter=R",
                args.revision1,
                args.revision2,
            ]
        )
        .decode("utf-8")
        .split("\n")
    )
    renamed_documents = [f for f in renamed_files if f.endswith(".rst")]

    csv_data: list[dict] = []
    branch = args.revision2
    for document in renamed_documents:
        _, source, destination = document.split("\t")
        csv_data.append(
            {"source": source, "destination": destination, "branch": branch}
        )

    if args.output_file:
        with open(args.output_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=csv_data[0].keys()).writerows(
                csv_data
            )
            writer.writeheader()
            writer.writerows(csv_data)
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=csv_data[0].keys())
        writer.writeheader()
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()

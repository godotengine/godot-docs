import os
import re
import sys

def check_headings():
    search_dir = "tutorials"
    exclude_path = "tutorials/io/binary_serialization_api.rst"
    info_message = "Headings which start with a number must have a custom anchor defined before them to prevent malformed link fragments.\nSee here: https://contributing.godotengine.org/en/latest/documentation/manual/contributing_to_the_manual.html \n"
    
    pattern = re.compile(r"^(?!\.\. _doc)(.+\n\s*^\d.*\n^[~-].*)", re.M)
    
    found_issues = False
    header_printed = False

    for root, _, files in os.walk(search_dir):
        for f in files:
            path = os.path.join(root, f)
            
            if not f.endswith(".rst") or path == exclude_path:
                continue
            
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            
            for match in pattern.finditer(content):
                if not header_printed:
                    print(f"{info_message}\n")
                    header_printed = True
                
                line_no = content[:match.start()].count("\n") + 1
                print(f"Violation in {path} at line {line_no}:\n{match.group(1)}\n")
                found_issues = True

    if found_issues:
        sys.exit(1)

if __name__ == "__main__":
    check_headings()
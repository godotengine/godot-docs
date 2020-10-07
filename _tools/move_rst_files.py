import re
from argparse import ArgumentParser
from os.path import isfile, isdir, join, realpath, split, dirname, relpath
import os
import shutil


def parse_and_get_arguments():
    """Creates and returns an object with parsed arguments, using argparse."""
    parser: ArgumentParser = ArgumentParser(
        prog="move_rst_files",
        description="Moves reST documents and their dependencies from one folder to another. Outputs required redirections in the ReadTheDocs backend.",
    )
    parser.add_argument(
        "documents", nargs="+", help="Paths of documents to move.",
    )
    parser.add_argument(
        "output_path", help="Path to the target output directory.",
    )
    return parser.parse_args()


def find_project_root_path(document_path):
    """Returns the path to the repository's root directory by looking for the file conf.py, starting
from the path of any file in the project."""
    full_path = realpath(document_path)
    dirpath = split(full_path)[0]

    root_path = ""
    current = dirpath
    iterations = 0
    while root_path == "":
        if isfile(join(current, "conf.py")):
            root_path = current
        else:
            current = split(current)[0]
            if current == "":
                break
        iterations += 1
        if iterations > 20:
            break
    return root_path


def find_images(document):
    """Returns the list of image filepaths used by the `document`."""
    images = []
    for line in document:
        match = re.match(r"\.\. image::\s+(img\/.+)", line)
        if match:
            images.append(match[1])
    return list(set(images))


def find_document_dependencies(documents):
    """For each document path in `documents`, finds all pictures it depends on and returns a dict with the form { document: [images] }."""
    data = {}
    for path in documents:
        with open(path, "r") as rst_file:
            images = find_images(rst_file)
            data[path] = images
    return data


def move_documents(paths, output_path):
    """Moves .rst files and all their image dependencies to `output_path`"""
    data = find_document_dependencies(paths)
    for path in data:
        directory = dirname(path)
        shutil.move(path, output_path)
        for image in data[path]:
            image_in_path = join(directory, image)
            image_out_path = join(output_path, image)
            image_out_dirpath = dirname(image_out_path)
            if not isdir(image_out_dirpath):
                os.makedirs(image_out_dirpath)
            shutil.move(image_in_path, image_out_path)


def print_redirects(paths):
    """Prints redirects we need to make on the ReadTheDocs backend with the form "input -> output".
    Moving the file /learning/features/viewports/viewports.rst to /tutorials/viewports/viewports.rst
    Requires the following redirect:
    /learning/features/viewports/viewports.html -> /tutorials/viewports/viewports.html
    """
    redirects = ""
    project_root_path = find_project_root_path(paths[0])
    out_path_relative = relpath(args.output_path, project_root_path)
    for document in paths:
        in_path_relative = relpath(document, project_root_path)
        in_directory, filename_rst = split(in_path_relative)
        filename_html = filename_rst.rsplit(".rst", 1)[0] + ".html"

        in_path = join(in_directory, filename_html)
        out_path = join(out_path_relative, filename_html)
        redirects += in_path + " -> " + out_path + "\n"
    print(redirects)


if __name__ == "__main__":
    args = parse_and_get_arguments()
    assert isdir(args.output_path)

    documents = [
        path for path in args.documents if isfile(path) and path.endswith(".rst")
    ]
    move_documents(documents, args.output_path)
    print_redirects(documents)

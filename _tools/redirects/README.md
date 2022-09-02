# ReadTheDocs redirect tools

The scripts located in this directory help in creating and maintaining redirects on [Read the Docs](https://readthedocs.io).
Also refer to Read the Docs [API documentation](https://docs.readthedocs.io/en/stable/api/index.html).

Note that RTD redirects only apply in case of 404 errors, and to all branches and languages:
<https://docs.readthedocs.io/en/stable/user-defined-redirects.html>.
If this ever changes, we need to rework how we manage these (likely adding per-branch logic).

`convert_git_renames_to_csv.py` creates a list of renamed files in Git to create redirects for.
`create_redirects.py` is used to actually manage redirects on ReadTheDocs.

For more information on the scripts themselves, see their help output.

## Setup

To install requirements: `pip3 install -r requirements.txt`.
Git is also required and needs to be available in the `PATH`.
To interact with the Read the Docs API, a valid API key must be set as
`RTD_AUTH_TOKEN` (either as a environment variable or in a [.env file](https://pypi.org/project/python-dotenv/)).

## Usage

Lets say we recently renamed some files in the Git branch `3.4` (compared to the `stable` branch), and now we want to create redirects for these.
For this, we would (after setting up the API token and requirements, see Setup above):

> python convert_git_renames_to_csv.py stable 3.4

This should output a list of the redirects to create. Lets append these to the redirects file:

> python convert_git_renames_to_csv.py stable 3.4 >> redirects.csv

After this, redirects for renamed files should have been appended to `redirects.csv`. You may want to double check that!
Now lets submit these to ReadTheDocs and create redirects there:

> python create_redirects.py

And that should be it!

The script takes care to not add duplicate redirects if the same ones already exist.
The created redirects are also valid for all branches and languages, which works out
as they only apply for actually missing files - when a user encounters a 404, that is.

The script also only touches `page` type redirects, all other types may still be added
and managed manually on RTD or via other means. All `page` redirects need to
be managed with these tools however, as they will otherwise just overwrite any
changes made elsewhere.

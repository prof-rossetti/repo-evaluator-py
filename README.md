# Repository Evaluation System

## Installation

Install package dependencies:

```sh
# For Pipenv users:
pipenv install -r requirements.txt # then run `pipenv shell`

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

## Setup

Populate `db/submissions.csv` with entries like the following:

    github_username, repository_url
    user123, https://github.com/user123/some-repo
    user456, https://github.com/user456/another-repo-py/tree/my-branch
    "partner1, partner2, partner3", https://github.com/partner2/group-repo

> NOTE: All repository urls are assumed to be valid. It's ok if they point to certain branches (i.e. urls with "`repo_name`/tree/`branch_name`")

To take advantage of file-checking features, also populate the `db/filenames.csv` file with a list of files each repository should contain, for example:

    filepath
    .env.example
    LICENSE
    README.md
    products_app/app.py
    products_app/db/products_default.csv
    tests/products_app/app_test.py

## Usage

Download all the repos:

```sh
python3 app/repo_downloader.py
```

Analyze contents of each repo to detect presence of files at specified locations:

```sh
python3 app/file_checker.py # this will write a report to `db/file_checks.csv`
```

## Testing

Run tests:

```sh
pytest tests/
```

# Repository Evaluation System

[![Build Status](https://travis-ci.com/prof-rossetti/repo-evaluator-py.svg?branch=master)](https://travis-ci.com/prof-rossetti/repo-evaluator-py)

Downloads student project repositories for further evaluation.
Also checks the repositories for files at specified locations,
and produces a corresponding CSV report of the results.

## Prerequisites

Requires Git and Python 3.x.

## Installation

Install source code:

```sh
git clone git@github.com:prof-rossetti/repo-evaluator-py.git
cd repo-evaluator-py/
```

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

To take advantage of file-checking features, also populate the `db/filenames.csv` file with a list of files and/or directories each repository should contain, for example:

    filepath
    .env.example
    LICENSE
    README.md
    products_app/app.py
    products_app/db/products_default.csv
    tests

## Usage

Download all the repos:

```sh
python3 app/repo_downloader.py # this will populate the `repos` directory!
```

Analyze contents of each repo to detect presence of files at specified locations:

```sh
python3 app/file_checker.py # this will write a report to `db/file_checks.csv`
```

## Testing

Run tests:

```sh
pytest tests/ # specify filepath to exclude tests from downloaded repos
```

## [License](LICENSE.md)

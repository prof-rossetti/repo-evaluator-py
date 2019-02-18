# Repository Evaluation System

[![Build Status](https://travis-ci.com/prof-rossetti/repo-evaluator-py.svg?branch=master)](https://travis-ci.com/prof-rossetti/repo-evaluator-py)

Downloads student project repositories for further evaluation.
Also checks the repositories for files at specified locations,
and produces a corresponding CSV report of the results (i.e. for importing into a spreadsheet gradebook).

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
pip install -r requirements.txt
```

## Usage

### Downloading Repos

Populate `db/submissions.csv` with entries like the following:

    github_username, repository_url
    user123, https://github.com/user123/some-repo
    user456, https://github.com/user456/another-repo-py/tree/my-branch
    "partner1, partner2, partner3", https://github.com/partner2/group-repo

> NOTE: All repository urls are assumed to be valid. It's ok if they point to certain branches (i.e. urls with "`repo_name`/tree/`branch_name`")

Download all the repos:

```sh
python app/repo_downloader.py # this will populate the `repos` directory!
```

### File Analysis

Populate the `db/filenames.csv` file with a list of files and/or directories each repository should contain, for example:

    filepath
    .env.example
    LICENSE
    README.md
    products_app/app.py
    products_app/db/products_default.csv
    tests

Analyze contents of each repo to detect presence of files at specified locations:

```sh
python app/file_checker.py # this will write a report to `db/file_checks.csv`
```

### History Viewing

View in a browser the version history of each repo:

```sh
python -m app.history_viewer
```

### History Analysis

Populate the `db/authors_excluded.csv` to exclude professor commits in starter repos:

    author_name
    Polly Professor
    Tommy TA

Populate the `db/users_authors.csv` file to specify a GitHub username for each non-username author name, so commits by the same username under different author names will be rolled-up into the same username:

    username, author_name
    user123, First User
    user456, Nickname Lastname
    user456, Fullfirst Lastname
    user789, Firstname

Analyze the version history for each repo:

```sh
python -m app.history_checker # this will write a report to `db/history_checks.csv`
```

## Testing

Run tests:

```sh
pytest tests/ # specify filepath to exclude tests from downloaded repos
```

## [License](LICENSE.md)

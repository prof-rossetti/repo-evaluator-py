# Repository Evaluation System

[![Build Status](https://travis-ci.com/prof-rossetti/repo-evaluator-py.svg?branch=master)](https://travis-ci.com/prof-rossetti/repo-evaluator-py)

Downloads student project repositories for further evaluation. Also:
  + checks for files at specified locations
  + analyzes version histories
  + opens version history URLs in a browser for further inspection

## Prerequisites

  + Git
  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Install source code:

```sh
git clone git@github.com:prof-rossetti/repo-evaluator-py.git
cd repo-evaluator-py/
```

Create and activate a new virtual environment:

```sh
conda create -n repo-eval-env python=3.7 # first time only
conda activate repo-eval-env
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

Populate the `db/files_expected.csv` file with a list of files and/or directories each repository should contain, for example:

    filepath
    .env.example
    LICENSE
    README.md
    products_app/app.py
    products_app/db/products_default.csv
    tests

Analyze contents of each repo to detect presence of files at specified locations:

```sh
python app/file_checker.py # this will write a report to `db/files_checked.csv`
```

### Standard File Analysis

Analyze contents of each repo to detect presence of standard files (README, LICENSE, and tests):

```sh
python app/standard_file_checker.py # this will write a report to `reports/standard_files_checked.csv`
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
python -m app.history_checker # this will write a report to `db/histories_checked.csv`
```

## Testing

Run tests:

```sh
pytest tests/ # specify filepath to exclude tests from downloaded repos
```

## [License](LICENSE.md)

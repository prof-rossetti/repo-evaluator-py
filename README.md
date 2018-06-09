

## Installation

Install package dependencies:

```sh
pipenv install -r requirements.txt
```

```sh
pipenv shell
```

## Setup

Populate `db/submissions.csv` with entries like the following:

    github_username, repository_url
    user123, https://github.com/user123/some-repo
    user456, https://github.com/user456/another-repo-py/tree/my-branch
    "partner1, partner2, partner3", https://github.com/partner2/group-repo

> NOTE: All repository urls are assumed to be valid. It's ok if they point to certain branches (i.e. urls with "`repo_name`/tree/`branch_name`")

## Usage

Download all the repos:

```sh
python3 app/repo_downloader.py
```

## Testing

Run tests:

```sh
pytest tests/
```

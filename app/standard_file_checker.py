#import csv
import os
from pathlib import Path

REPOS_DIRPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos"))

#CSV_FILEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports", "standard_files_checked.csv"))

if __name__ == "__main__":

    repo_names = os.listdir(REPOS_DIRPATH)

    for repo_name in repo_names:
        print("-----------------")
        print(repo_name.upper())
        print("-----------------")
        repo_path = os.path.join(REPOS_DIRPATH, repo_name)

        # h/t: https://stackoverflow.com/a/2186565/670433
        python_files = Path(repo_path).glob("**/*.py")
        for python_filename in python_files:
            print("...", python_filename)

#import csv
import os

REPOS_DIRPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos")) # need absolute path to pass to os.listdir(), adapted from source: https://stackoverflow.com/a/2860193/670433

#STANDARD_FILES = {
#    "README": ["README", "README.md", "README.txt"],
#    "LICENSE": ["LICENSE", "LICENSE.md", "LICENSE.txt"]
#}

#CSV_FILEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports", "standard_files_checked.csv"))

if __name__ == "__main__":

    repos = os.listdir(REPOS_DIRPATH)

    #results = []
    for repo_name in repos:
        print("-----------------")
        print(repo_name.upper())
        print("-----------------")
        repo_path = os.path.join(REPOS_DIRPATH, repo_name)
        print(repo_path)

        #results.append()

    #print("-----------------")
#
    #if results:
    #    #write_results_to_file(results=results, filename="db/files_checked.csv")
    #else:
    #    print("OOPS, NO REPOS. HAVE YOU RUN THE REPO DOWNLOADER?")

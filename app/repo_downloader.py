import csv
import os
import pdb
import shutil
import subprocess

def parsed_output(my_output):
    return my_output.decode().strip()

def system_command(my_command="whoami"):
    # adapted from source: https://stackoverflow.com/a/4256153/670433
    process = subprocess.Popen(my_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def repo_clone_address(url="", mode="ssh"):
    repo = repo_name(url)
    last_char_index = url.index(repo) + len(repo)
    if mode == "https":
        clone_address = f"{url[:last_char_index]}.git"
    elif mode == "ssh":
        user = repo_owner(url)
        clone_address = f"git@github.com:{user}/{repo}.git"
    return clone_address

def repo_owner(url):
    return url.split("/")[3]

def repo_name(url):
    return url.split("/")[4]

def clean_up(dirname="repos"):
    dirpath = os.path.join(os.path.dirname(__file__), "..", dirname)
    print(dirpath)
    if os.path.isdir(dirpath):
        shutil.rmtree(dirpath) # source: https://stackoverflow.com/a/186236/670433

def read_submission_from_file(filename="db/submissions.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    print("-----------------")
    print("READING SUBMISSIONS FROM FILE:\n", csv_filepath)
    submissions = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True) # source: https://stackoverflow.com/a/17255790/670433
        for row in reader:
            submissions.append(dict(row))
    return submissions

if __name__ == '__main__':

    repos_dirname = "repos"

    # CLEAN REPOS DIR

    try: clean_up(repos_dirname)
    except FileNotFoundError as e: print(e)

    # READ URLS FROM SUBMISSIONS.CSV FILE

    submissions = read_submission_from_file("db/submissions.csv")
    submission_urls = [s["repository_url"] for s in submissions]

    for submission_url in submission_urls:

        # DOWNLOAD REPO

        clone_address = repo_clone_address(url=submission_url, mode="ssh")
        user = repo_owner(submission_url)
        command = f"git clone {clone_address} repos/{user}" # clone into a specific dir

        print("-----------------")
        print(f"{user}".upper())
        print("-----------------")
        results, err = system_command(command)
        if err:
            print("ERROR:", error)
        if results:
            print("-----------------")
            print("RESULTS:", parsed_output(results))

        # CHECKOUT BRANCH AS NECESSARY
        # TODO: if repo_url contains the word "tree" (e.g. /tree/my_branch),
        # ... then checkout that branch after downloading

    # OPEN FOR INSPECTION

    results, err = system_command(f"open {repos_dirname}")
    if err:
        print("ERROR:", error)
    if results:
        print("-----------------")
        print("RESULTS:", parsed_output(results))

    print("-----------------")
    print("DONE! HAPPY GRADING :-)")
    print("-----------------")

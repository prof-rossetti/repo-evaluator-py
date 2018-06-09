from IPython import embed
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

def repo_clone_address(url):
    name = repo_name(url)
    last_char_index = url.index(name) + len(name)
    repo_url = url[:last_char_index]
    return f"{repo_url}.git"

def repo_owner(url):
    return url.split("/")[3]

def repo_name(url):
    return url.split("/")[4]

def clean_up(dirname="repos"):
    dirpath = os.path.join(os.path.dirname(__file__), "..", dirname)
    shutil.rmtree(dirpath) # source: https://stackoverflow.com/a/186236/670433

if __name__ == '__main__':

    # CLEAN REPOS DIR
    try: clean_up()
    except FileNotFoundError as e: print(e)

    # READ URLS FROM SUBMISSIONS.CSV FILE
    repo_urls = [
        "https://github.com/s2t2/python-csv-crud-app",
        #"https://github.com/s2t2/python-csv-crud-app/tree/testing4",
        "https://github.com/prof-rossetti/inventory-mgmt-app-py/tree/solution"
    ]

    for repo_url in repo_urls:

        # CLONE/DOWNLOAD REPO
        clone_address = repo_clone_address(repo_url)
        user = repo_owner(repo_url)
        command = f"git clone {clone_address} repos/{user}" # clone into a specific dir
        results, err = system_command(command)
        if err: print("ERROR:", error)
        if results: print("RESULTS:", parsed_output(results))

        # CHECKOUT BRANCH AS NECESSARY
        # ... if repo_url contains the word "tree" (e.g. /tree/my_branch),
        # ... then checkout that branch after downloading

        # OPEN FOR INSPECTION
        results, err = system_command("open repos")
        if err: print("ERROR:", error)
        if results: print("RESULTS:", parsed_output(results))

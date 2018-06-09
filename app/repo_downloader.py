import subprocess
from IPython import embed

def parsed_output(my_output):
    return my_output.decode().strip()

def system_command(my_command="whoami"):
    # adapted from source: https://stackoverflow.com/a/4256153/670433
    process = subprocess.Popen(my_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

if __name__ == '__main__':

    # CLEAN REPOS DIR
    # ... os delete all files in "repos" dir

    # COMPILE CLONE COMMAND

    https_clone_url = "https://github.com/s2t2/python-csv-crud-app.git"
    command = f"git clone {https_clone_url} repos/my_user/my_repo" # clone into a specific dir

    # CLONE/DOWNLOAD REPO

    results, err = system_command(command)
    if err: print("ERROR:", error)
    if results: print("RESULTS:", parsed_output(results))

    # CHECKOUT BRANCH AS NECESSARY
    # ... if repo_url contains the word "tree" (e.g. /tree/my_branch),
    # ... then checkout that branch after downloading

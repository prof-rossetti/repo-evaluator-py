import csv
import os
import pdb

def read_filepaths_from_file(filename="db/files_expected.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    #print("-----------------")
    #print("READING EXPECTED REPO FILEPATHS FROM FILE:", csv_filepath)
    expected_filepaths = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True) # source: https://stackoverflow.com/a/17255790/670433
        for row in reader:
            expected_filepaths.append(row["filepath"])
    return expected_filepaths

def check_files(repo_name="repos/my_repo", expected_files=[]):
    repo_filepath = os.path.join(os.path.dirname(__file__), "..", repo_name)
    files_report = {}
    for expected_file in expected_files:
        expected_filepath = os.path.join(repo_filepath, expected_file)
        files_report[expected_file] = os.path.exists(expected_filepath) # h/t: https://stackoverflow.com/a/17752147/670433

    repo = repo_name
    if "/" in repo: repo = repo.split("/")[-1]
    return {"repo": repo, "files": files_report}

def write_results_to_file(results=[], filename="db/files_checked.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    expected_files = results[0]["files"]
    headers = ["repo"] + list(expected_files)

    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader() # uses fieldnames set above
        for result in results:
            row = {"repo": result["repo"]}
            for expected_file in expected_files:
                row[expected_file] = result["files"][expected_file]
            writer.writerow(row)


if __name__ == '__main__':

    expected_files = read_filepaths_from_file("db/files_expected.csv")

    repos_dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos")) # need absolute path to pass to os.listdir(), adapted from source: https://stackoverflow.com/a/2860193/670433
    repos = os.listdir(repos_dirpath)

    results = []
    for repo in repos:
        print("-----------------")
        print(repo.upper())
        print("-----------------")
        repo_path = os.path.join(os.path.dirname(__file__), "..", "repos", repo)
        result = check_files(repo_name=repo_path, expected_files=expected_files)
        results.append(result)

        for k, v in result["files"].items(): # adapted from: https://stackoverflow.com/a/3294899/670433
            if v == True:
                print(v, " |", k) # pad a space to make up for difference in chars between "true" and "false"
            else:
                print(v, "|", k)
    print("-----------------")

    write_results_to_file(results=results, filename="db/files_checked.csv")

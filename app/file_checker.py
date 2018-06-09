import csv
import os
import pdb

def read_filepaths_from_file(filename="db/filepaths.csv"):
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
    report = {}
    for expected_file in expected_files:
        expected_filepath = os.path.join(repo_filepath, expected_file)
        report[expected_file] = os.path.exists(expected_filepath) # h/t: https://stackoverflow.com/a/17752147/670433
    return report

if __name__ == '__main__':

    expected_files = read_filepaths_from_file("db/files_expected.csv")

    repos_dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos")) # need absolute path to pass to os.listdir(), adapted from source: https://stackoverflow.com/a/2860193/670433
    repos = os.listdir(repos_dirpath)

    for repo in repos:
        print("-----------------")
        print(repo.upper())
        print("-----------------")
        repo_path = os.path.join(os.path.dirname(__file__), "..", "repos", repo)
        results = check_files(repo_name=repo_path, expected_files=expected_files)
        for k, v in results.items(): # adapted from: https://stackoverflow.com/a/3294899/670433
            if v == True:
                print(v, " |", k) # pad a space to make up for difference in chars between "true" and "false"
            else:
                print(v, "|", k)
    print("-----------------")

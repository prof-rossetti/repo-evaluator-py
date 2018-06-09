import csv
import os
import pdb

def read_filepaths_from_file(filename="db/filepaths.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    print("-----------------")
    print("READING EXPECTED REPO FILEPATHS FROM FILE:", csv_filepath)
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
        report[expected_file] = os.path.isfile(expected_filepath)
    return report

if __name__ == '__main__':

    expected_filepaths = read_filepaths_from_file("db/filepaths.csv")
    print(expected_filepaths)

    #repo_dirs = os.listfiles("repos")
    pdb.set_trace()

    #for repo_dirname in repo_dirs:
    #    print("-----------")
    #    result = check_files(repo_dirname=repo_dirname, expected_filepaths=expected_filepaths)
    #    print(result)

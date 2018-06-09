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

if __name__ == '__main__':
    expected_filepaths = read_filepaths_from_file("db/filepaths.csv")
    print(expected_filepaths)

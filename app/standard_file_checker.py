#import csv
import os
from pathlib import Path

TEST_FILE_SUBSTR= os.getenv("TEST_FILE_SUBSTR", default="test") # can be "spec", etc.
REPOS_DIRPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos"))

#CSV_FILEPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports", "standard_files_checked.csv"))

if __name__ == "__main__":

    repo_names = os.listdir(REPOS_DIRPATH)

    for repo_name in repo_names:
        print("-----------------")
        print(repo_name.upper())
        print("-----------------")
        repo_path = os.path.join(REPOS_DIRPATH, repo_name)

        #tests_present = False
        #python_files = Path(repo_path).glob("**/*.py")
        #for python_filename in python_files:
        #    #print("...", python_filename)
        #    #type(python_filename) #> PosixPath
        #    if "_test" in str(python_filename) or "test_" in str(python_filename):
        #        tests_present = True
        #print("TESTS PRESENT:", tests)

        readme_present = False
        license_present = False
        tests_present = False

        all_files = Path(repo_path).glob("**/*")
        for filepath in all_files:
            #filename = str(filepath)
            #filename = os.path.split(filename)[-1]
            filestem = filepath.stem #> LICENSE
            if filestem in ["README", "README.md", "README.txt"]:
                readme_present = True
            elif filestem in ["LICENSE", "LICENSE.md", "LICENSE.txt"]:
                license_present = True
            elif f"_{TEST_FILE_SUBSTR}" in filestem or f"{TEST_FILE_SUBSTR}_" in filestem:
                tests_present = True

        #print("README PRESENT:", readme_present)
        #print("LICENSE PRESENT:", license_present)
        #print("TESTS PRESENT:", tests_present)
        results = {"README": readme_present, "LICENSE": license_present, "TESTS": tests_present}
        print(results)

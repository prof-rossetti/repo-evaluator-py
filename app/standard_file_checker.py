import os
from pathlib import Path

import pandas

TEST_FILE_SUBSTR= os.getenv("TEST_FILE_SUBSTR", default="test") # can be "spec", etc.

REPOS_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "repos")
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "reports", "standard_files_checked.csv")

if __name__ == "__main__":

    repo_names = os.listdir(REPOS_DIRPATH)

    results = []
    for repo_name in repo_names:
        #print("-----------------")
        #print(repo_name.upper())
        #print("-----------------")
        repo_path = os.path.join(REPOS_DIRPATH, repo_name)

        readme_present = False
        license_present = False
        tests_present = False

        all_files = Path(repo_path).glob("**/*")
        for filepath in all_files:
            filestem = filepath.stem #> LICENSE
            if filestem in ["README", "README.md", "README.txt"]:
                readme_present = True
            elif filestem in ["LICENSE", "LICENSE.md", "LICENSE.txt"]:
                license_present = True
            elif f"_{TEST_FILE_SUBSTR}" in filestem or f"{TEST_FILE_SUBSTR}_" in filestem:
                tests_present = True

        result = {
            "REPO": repo_name,
            "README": readme_present,
            "LICENSE": license_present,
            "TESTS": tests_present
        }
        print(result)
        results.append(result)


    print("-------------")
    print("WRITING TO CSV", CSV_FILEPATH)
    print("-------------")

    df = pandas.DataFrame(results)
    df.to_csv(CSV_FILEPATH, index=False)

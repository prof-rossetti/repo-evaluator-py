
from app.file_checker import *

def test_read_filepaths_from_file():
    filepaths = read_filepaths_from_file("tests/mocks/files_expected.csv")
    assert len(filepaths) == 5

def test_check_files():
    repo = "tests/mocks/repos/my_repo"
    files = ["README.md", "app/my_app.py", ".env.example"]
    result = check_files(repo_name=repo, expected_files=files)
    assert result == {"repo": "my_repo", "files":{"README.md":True, "app/my_app.py":True, ".env.example":True}}

def test_check_files_missing():
    repo = "tests/mocks/repos/my_repo"
    files = ["README.md", "some/other/nonexistent_file.md"]
    result = check_files(repo_name=repo, expected_files=files)
    assert result == {"repo": "my_repo", "files":{"README.md":True, "some/other/nonexistent_file.md":False}}

def test_check_files_including_dirs():
    repo = "tests/mocks/repos/my_repo"
    files = ["app", "app/db", "nonexistent_dir"]
    result = check_files(repo_name=repo, expected_files=files)
    assert result == {"repo": "my_repo", "files":{"app":True, "app/db": True, "nonexistent_dir":False}}

def test_write_results_to_file():
    # setup:
    results = [
        {"repo": "my_repo", "files": {"README.md":True, "app/my_app.py":True, ".env.example":True}},
        {"repo": "other_repo", "files": {"README.md":True, "app/my_app.py":False, ".env.example":False}},
    ]
    csv_filename = "tests/mocks/files_checked.csv"
    write_results_to_file(results=results, filename=csv_filename)
    # test:
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", csv_filename)
    rows_written = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True) # h/t: https://stackoverflow.com/a/17255790/670433
        for row in reader:
            rows_written.append(dict(row))
    assert rows_written[0]["repo"] == "my_repo"
    assert rows_written[0]["README.md"] == "True"
    assert rows_written[0]["app/my_app.py"] == "True"
    assert rows_written[1]["repo"] == "other_repo"
    assert rows_written[1]["README.md"] == "True"
    assert rows_written[1]["app/my_app.py"] == "False"

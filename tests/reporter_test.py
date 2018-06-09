
from app.repo_reporter import *

def test_read_filepaths_from_file():
    filepaths = read_filepaths_from_file("tests/mocks/filepaths.csv")
    assert len(filepaths) == 5

def test_check_files():
    repo = "tests/mocks/repos/my_repo"
    files = ["README.md", "app/my_app.py", ".env.example"]
    result = check_files(repo_name=repo, expected_files=files)
    assert result == {"README.md":True, "app/my_app.py":True, ".env.example":True}

#def test_check_files_missing():
#    repo = "tests/mocks/repos/my_repo"
#    files = ["README.md", "some/other/file.md"]
#    result = check_files(repo_name=repo, expected_files=files)
#    assert result == {"README.md":True, "some/other/file.md":True}

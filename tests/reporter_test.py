
from app.repo_reporter import *

def test_read_filepaths_from_file():
    filepaths = read_filepaths_from_file("tests/mocks/filepaths.csv")
    assert len(filepaths) == 5

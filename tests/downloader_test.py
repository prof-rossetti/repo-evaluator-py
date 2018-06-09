import pathlib
import os
import pytest

from app.repo_downloader import *

def test_parsed_output():
    raw_output = b'testing testing\n'
    assert isinstance(raw_output, bytes) # test that the test was setup properly
    assert parsed_output(raw_output) == "testing testing"

def test_system_command():
    results, error = system_command(f"echo testing testing")
    assert results == b'testing testing\n'
    assert error == None

def test_repo_clone_address():
    assert repo_clone_address(url="https://github.com/user123/repo456", mode="https") == "https://github.com/user123/repo456.git"
    assert repo_clone_address(url="https://github.com/user123/repo456", mode="ssh") == "git@github.com:user123/repo456.git"
    assert repo_clone_address(url="https://github.com/user123/repo456/tree/branch789", mode="https") == "https://github.com/user123/repo456.git"
    assert repo_clone_address(url="https://github.com/user123/repo456/tree/branch789", mode="ssh") == "git@github.com:user123/repo456.git"

def test_repo_owner():
    assert repo_owner("https://github.com/user123/repo456") == "user123"

def test_repo_name():
    assert repo_name("https://github.com/user123/repo456") == "repo456"

def test_clean_up():
    my_dir = "tests/mocks/clean_me"
    pathlib.Path(my_dir).mkdir(parents=True, exist_ok=True) # source: https://stackoverflow.com/a/14364249/670433
    assert os.path.isdir(my_dir) == True
    clean_up(my_dir)
    assert os.path.isdir(my_dir) == False

def test_clean_up_nothing():
    my_dir = "tests/mocks/clean_me"
    with pytest.raises(FileNotFoundError) as e: # should raise error if dir doesn't exist, source: https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
        clean_up(my_dir)

def test_read_submission_from_file():
    submissions = read_submission_from_file("tests/submissions.csv")
    assert len(submissions) == 3
    assert submissions[0]["repository_url"] == "https://github.com/user123/some-repo"

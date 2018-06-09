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
    assert repo_clone_address("https://github.com/user123/repo456") == "https://github.com/user123/repo456.git"
    assert repo_clone_address("https://github.com/user123/repo456/tree/branch789") == "https://github.com/user123/repo456.git"

def test_repo_owner():
    assert repo_owner("https://github.com/user123/repo456") == "user123"

def test_repo_name():
    assert repo_name("https://github.com/user123/repo456") == "repo456"

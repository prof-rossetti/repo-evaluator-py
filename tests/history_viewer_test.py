from app.history_viewer import history_url

def test_repo_history_url():
    repo_url = "https://github.com/user123/my-project"
    expected_url = "https://github.com/user123/my-project/commits/master"
    assert history_url(repo_url) == expected_url

def test_file_history_url():
    file_url = "https://github.com/user123/my-project/blob/master/my_script.py"
    expected_url = "https://github.com/user123/my-project/commits/master/my_script.py"
    assert history_url(file_url) == expected_url

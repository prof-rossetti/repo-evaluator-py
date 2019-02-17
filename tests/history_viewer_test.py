from app.history_viewer import history_url

def test_repo_history_url():
    repo_url = "__________"
    expected_url = "________"
    assert history_url(repo_url) == expected_url

def test_file_history_url():
    file_url = "__________"
    expected_url = "________"
    assert history_url(file_url) == expected_url

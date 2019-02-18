from app.history_checker import read_excluded_authors, group_by_username

def test_read_excluded_authors():
    author_names = read_excluded_authors("tests/mocks/authors_excluded.csv")
    assert author_names == ["Polly Professor", "Tommy TA"]

def test_group_by_username():
    author_histories = [
        {'owner': 'user123', 'username': 'user123', 'author_name': 'user123', 'commit_count': 20},
        {'owner': 'user456', 'username': 'user456', 'author_name': 'Full Name', 'commit_count': 5},
        {'owner': 'user456', 'username': 'user456', 'author_name': 'Nickname', 'commit_count': 10},
        {'owner': 'user456', 'username': 'user456', 'author_name': 'user456', 'commit_count': 15},
        {'owner': 'user456', 'username': 'guestcontrib', 'author_name': 'guestcontrib', 'commit_count': 3}
    ]
    user_histories = [
        {'owner': 'user123', 'username': 'user123', 'commit_count': 20},
        {'owner': 'user456', 'username': 'guestcontrib', 'commit_count': 3},
        {'owner': 'user456', 'username': 'user456', 'commit_count': 30}
    ]
    assert group_by_username(author_histories) == user_histories

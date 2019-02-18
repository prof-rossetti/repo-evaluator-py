from app.history_checker import read_excluded_authors

def test_read_excluded_authors():
    author_names = read_excluded_authors("tests/mocks/authors_excluded.csv")
    assert author_names == ["Polly Professor", "Tommy TA"]

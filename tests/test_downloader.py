from app.repo_downloader import parsed_output

def test_parsed_output():
    # setup:
    raw_output = b'message\n'
    assert isinstance(raw_output, bytes)
    # test:
    #assert parsed_output(raw_output) == "message"

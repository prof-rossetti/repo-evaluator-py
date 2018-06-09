from app.repo_downloader import parsed_output, system_command

def test_parsed_output():
    raw_output = b'testing testing\n'
    assert isinstance(raw_output, bytes) # test that the test was setup properly
    assert parsed_output(raw_output) == "testing testing"

def test_system_command():
    results, error = system_command(f"echo testing testing")
    assert results == b'testing testing\n'
    assert error == None

import webbrowser

from app.repo_downloader import read_submission_from_file

# Different URL templates for commit history pages:
# ... https://github.com/{USERNAME}/{REPONAME}/commits/master"
# ... https://github.com/{USERNAME}/{REPONAME}/commits/master/{FILENAME}.py"
# Some submission URLs may include the file paths already, but most might not.
# TODO: prefer file-specific history, if possible
def history_url(submission_url):
    return f"{submission_url}/commits/master" # view the history for whatever url (repo or file) was submitted

if __name__ == "__main__":
    submissions = read_submission_from_file("db/submissions.csv")
    urls = [history_url(s["repository_url"]) for s in submissions]

    print("-----------------")
    confirm = input(f"DETECTED {len(urls)} HISTORY URLS. \nCONTINUE TO OPEN THEM ALL IN A BROWSER? (Y/N): ")

    if confirm.upper() == "Y":
        for url in urls:
            print("---")
            print("OPENING...")
            print(url)
            # see: https://docs.python.org/3/library/webbrowser.html
            # open_new_tab() defaults to open_new() if necessary
            webbrowser.open_new_tab(url)
        print("-----------------")
        print("DONE. HAPPY GRADING!")

    else:
        print("CANCELLING... PLEASE TRY AGAIN.")

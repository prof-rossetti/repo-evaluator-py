import os
import webbrowser

from app.repo_downloader import read_submission_from_file

# SUBMISSION URL EXAMPLES:
# ... https://github.com/{USERNAME}/{REPONAME}
# ... https://github.com/{USERNAME}/{REPONAME}/blob/master/{FILENAME}.py
#
# HISTORY URLS:
# ... https://github.com/{USERNAME}/{REPONAME}/commits/master"
# ... https://github.com/{USERNAME}/{REPONAME}/commits/master/{FILENAME}.py"
#
def history_url(submission_url):
    if "/blob/" in submission_url:
        return submission_url.replace("blob", "commits")
    else:
        return os.path.join(submission_url, "commits", "master")

if __name__ == "__main__":

    submissions = read_submission_from_file("db/submissions.csv")
    urls = [history_url(s["repository_url"]) for s in submissions]

    print("-----------------")
    confirm = input(f"DETECTED {len(urls)} HISTORY URLS. \nCONTINUE TO OPEN THEM ALL IN A BROWSER? (Y/N): ")

    if confirm.upper() != "Y":
        exit("CANCELLING... PLEASE TRY AGAIN.")
    else:
        for url in urls:
            print(f" ... {url}") # source: https://docs.python.org/3/library/webbrowser.html
            #webbrowser.open_new_tab(url)
        print("-----------------")

    print("DONE. HAPPY GRADING!")

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
        return os.path.join(submission_url, "commits", "main")

if __name__ == "__main__":

    submissions = read_submission_from_file("db/submissions.csv")

    url_field = input("PLEASE SELECT A COLUMN NAME THAT HAS THE URLS YOU WANT TO OPEN: ") or "repository_url"
    print("OK, USING:", url_field)

    urls = [history_url(s[url_field]) for s in submissions]
    urls = sorted(urls, key=lambda url: url.upper())
    #print(urls[0])

    print("-----------------")
    confirm = input(f"DETECTED {len(urls)} URLS. \nCONTINUE TO OPEN THEM ALL IN A BROWSER? (Y/N): ")

    if confirm.upper() != "Y":
        exit("CANCELLING... PLEASE TRY AGAIN.")
    else:
        for url in urls:
            print(f" ... {url}")
            webbrowser.open_new_tab(url) # source: https://docs.python.org/3/library/webbrowser.html
        print("-----------------")

    print("DONE. HAPPY GRADING!")

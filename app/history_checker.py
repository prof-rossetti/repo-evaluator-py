import csv
import os
import pandas as pd
#import itertools
#from operator import itemgetter

from app.repo_downloader import system_command, parsed_output

def read_excluded_authors(filename="db/authors_excluded.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    author_names = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True) # source: https://stackoverflow.com/a/17255790/670433
        for row in reader:
            author_names.append(row["author_name"])
    return author_names

def read_author_names(filename="db/user_author_names.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    author_names = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True) # source: https://stackoverflow.com/a/17255790/670433
        for row in reader:
            author_names.append(dict(row))
    return author_names

def write_results_to_file(results=[], filename="db/histories_checked.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    headers = list(results[0].keys())
    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader() # uses fieldnames set above
        for result in results:
            writer.writerow(result)

def group_by_username(author_histories):
    #sorted_histories = sorted(author_histories, key=itemgetter("username")) # sort by some attribute
    #histories_by_username = itertools.groupby(sorted_histories, key=itemgetter("username")) # group by the sorted attribute
    #user_histories = []
    #for username, histories in histories_by_username:
    #    breakpoint()
    #    history = histories[0]
    #    history["commit_count"] = 0
    #    for h in histories:
    #        history["commit_count"] += int(h["commit_count"])
    #    user_histories.append(h)
    #return user_histories
    df = pd.DataFrame(author_histories)
    grouped_df = df.groupby(["owner", "username"]).sum()
    user_histories = []
    for i, row in grouped_df.iterrows():
        user_histories.append({
            "owner": row.name[0],
            "username": row.name[1],
            "commit_count": row["commit_count"]
        })
    return user_histories

def lookup_username(author_name, users_authors):
    matching_usernames = [d["username"] for d in users_authors if d["author_name"].upper() == author_name.upper()]
    try:
        return matching_usernames[0]
    except IndexError as err:
        return author_name

if __name__ == "__main__":

    print("-----------------")
    print("CHECKING EXCLUDED AUTHORS...")
    print("-----------------")

    excluded_author_names = read_excluded_authors()
    print(excluded_author_names)

    print("-----------------")
    print("GETTING USERNAME / AUTHOR NAME MAPPINGS...")
    print("-----------------")

    users_authors = read_author_names()

    print("-----------------")
    print("CHECKING VERSION HISTORIES...")
    print("-----------------")

    histories = []

    repos_dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos")) # need absolute path to pass to os.listdir(), adapted from source: https://stackoverflow.com/a/2860193/670433
    repos = os.listdir(repos_dirpath)
    repos.sort()
    for repo in repos:
        print(" ... ", repo)
        repo_path = os.path.join(os.path.dirname(__file__), "..", "repos", repo)
        os.chdir(repo_path)

        #command = f"git shortlog -s -e"
        ##> 24     Author XYZ <xyz@Username-MacBook-Pro.local>
        ##> 12     Author123 <author123@users.noreply.github.com>
        command = f"git shortlog -s"
        #> 24     Author XYZ
        #> 12     Author123
        cmd_results, cmd_err = system_command(command)
        if cmd_err:
            print("ERROR:", cmd_err)
            exit()
        if cmd_results:
            parsed_results = parsed_output(cmd_results)
            author_results = parsed_results.split("\n")
            #author_results = [s.strip() for s in author_results]
            #> ['24\tAuthor XYZ <email>', '12\tAuthor123 <email>']
            for s in author_results:
                author_commits = s.split("\t") #> ['24', 'Author XYZ <email>']
                commit_count = int(author_commits[0])
                author = author_commits[1] #> 'Author XYZ <email>'
                #author = author.split("<")
                #author_name = author[0].strip()
                #author_email = author[1].replace(">","").strip()

                author_name = author
                if not author_name in excluded_author_names:
                    history = {
                        "owner": repo,
                        "username": lookup_username(author_name, users_authors),
                        "author_name": author_name,
                        #"author_email": author_email,
                        "commit_count": commit_count
                    }
                    #print(history)
                    histories.append(history)

    username_histories = group_by_username(histories)

    write_results_to_file(results=username_histories)

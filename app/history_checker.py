import csv
import os

from app.repo_downloader import system_command, parsed_output

def read_excluded_authors(filename="db/authors_excluded.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    author_names = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True) # source: https://stackoverflow.com/a/17255790/670433
        for row in reader:
            author_names.append(row["author_name"])
    return author_names

def write_results_to_file(results=[], filename="db/histories_checked.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    headers = list(results[0].keys())
    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader() # uses fieldnames set above
        for result in results:
            writer.writerow(result)



if __name__ == "__main__":


    excluded_author_names = read_excluded_authors()

    histories = []

    repos_dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repos")) # need absolute path to pass to os.listdir(), adapted from source: https://stackoverflow.com/a/2860193/670433
    repos = os.listdir(repos_dirpath)

    for repo in repos:
        print("-----------------")
        print(repo.upper())
        print("-----------------")
        repo_path = os.path.join(os.path.dirname(__file__), "..", "repos", repo)
        #print(repo_path)
        os.chdir(repo_path)

        # source: https://stackoverflow.com/questions/677436/how-do-i-get-the-git-commit-count

        #command = f"git rev-list --count master" #> 36
        #command = f"git shortlog -s -n"
        #> 24 Author XYZ
        #> 12 Author123
        command = f"git shortlog -s -e"
        #> 24 Author XYZ <xyz@Username-MacBook-Pro.local>
        #> 12 Author123 <author123@users.noreply.github.com>

        cmd_results, cmd_err = system_command(command)
        if cmd_err:
            print("ERROR:", cmd_err)
            exit()
        if cmd_results:
            parsed_results = parsed_output(cmd_results)
            #> '36\tMYUSERNAME'
            #> '24\tAuthor XYZ\n     12\tAuthor123'

            #> '36\tMYUSERNAME <email>'

            per_author = parsed_results.split("\n")
            per_author = [a.strip() for a in per_author] #> ['24\tAuthor XYZ', '12\tAuthor123']
            for s in per_author:
                author_commits = s.split("\t") #> ['36', 'MYUSERNAME']
                commit_count = int(author_commits[0])
                author = author_commits[1]
                author = author.split("<")
                author_name = author[0].strip()
                author_email = author[1].replace(">","").strip()
                if not author_name in excluded_author_names:
                    histories.append({
                        "owner": repo,
                        "author_name": author_name,
                        "author_email": author_email,
                        "commit_count": commit_count
                    })

    write_results_to_file(results=histories)

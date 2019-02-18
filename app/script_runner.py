#from app.repo_downloader import system_command, parsed_output
#
#if __name__ == "__main__":
#
#    # if there's a file called requirements.txt...
#    installation_cmd = "pip install -r requirements.txt"
#    installation_results, installation_err = system_command(installation_cmd)
#    if installation_err:
#        print("INSTALLATION ERROR:", error)
#    if installation_results:
#        print("-----------------")
#        print("INSTALLATION RESULTS:", parsed_output(results))
#
#    filename = "monthly_sales.py"
#    command = f"python {filename}"
#
#    results, err = system_command(command)
#        if err:
#            print("ERROR:", error)
#        if results:
#            print("-----------------")
#            print("RESULTS:", parsed_output(results))
#

import subprocess
from IPython import embed

def parsed_output(my_output):
    return my_output.decode().strip()

def system_command(my_command="whoami"):
    # adapted from source: https://stackoverflow.com/a/4256153/670433
    process = subprocess.Popen(my_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

if __name__ == '__main__':
    results, err = system_command("whoami")
    if err:
        print("ERROR:", error)
    if results:
        print("RESULTS:", parsed_output(results))

import subprocess
from IPython import embed

def parsed_output(my_output):
    return my_output.decode().strip()

if __name__ == '__main__':

    # adapted from source: https://stackoverflow.com/a/4256153/670433
    command = "whoami"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if output: print("OUTPUT", output)
    if error: print("ERROR", error)

    results = parsed_output(output)

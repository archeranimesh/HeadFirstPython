import os

# the below line open the file in the directory where the script is present
# not in the directory from where the script is run.
tasks = open(os.path.dirname(os.path.realpath(__file__)) + "/todo.txt")

for chore in tasks:
    # the end="", is added because the file has a new line char already
    print(chore, end="")

tasks.close()

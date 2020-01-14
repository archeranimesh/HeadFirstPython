import os

# the below line open the file in the directory where the script is present
# not in the directory from where the script is run.
todo = open(os.path.dirname(os.path.realpath(__file__)) + "/todo.txt", "a")

print("Put out the trash.", file=todo)
print("Fee the cat.", file=todo)
print("Prepare tax return", file=todo)

todo.close()

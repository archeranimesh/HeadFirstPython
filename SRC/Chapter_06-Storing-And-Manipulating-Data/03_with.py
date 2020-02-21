import os

with open(os.path.dirname(os.path.realpath(__file__)) + "/todo.txt") as tasks:
    for chore in tasks:
        print(chore, end="")

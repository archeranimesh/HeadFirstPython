import csv

csv_file = "/Users/arunab/myWork/myTutorials/myPython/HeadFirstPython/SRC/Chapter_13-Advanced-Iteration/buzzdata.csv"

with open(csv_file) as raw_data:
    for line in csv.reader(raw_data):
        print(line)

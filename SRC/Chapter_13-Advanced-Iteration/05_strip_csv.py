import pprint

csv_file = "/Users/arunab/myWork/myTutorials/myPython/HeadFirstPython/SRC/Chapter_13-Advanced-Iteration/buzzdata.csv"

with open(csv_file) as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        # strip removes the whitespaces,
        k, v = line.strip().split(",")
        flights[k] = v

if __name__ == "__main__":
    pprint.pprint(flights)

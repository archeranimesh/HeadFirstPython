import pprint

csv_file = "/Users/arunab/myWork/myTutorials/myPython/HeadFirstPython/SRC/Chapter_13-Advanced-Iteration/buzzdata.csv"


with open(csv_file) as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        # splits() returns a tuple
        k, v = line.split(",")
        flights[k] = v

if __name__ == "__main__":
    pprint.pprint(flights)

from datetime import datetime
import pprint


csv_file = "/Users/arunab/myWork/myTutorials/myPython/HeadFirstPython/SRC/Chapter_13-Advanced-Iteration/buzzdata.csv"


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, "%H:%M").strftime("%I:%M%p")


with open(csv_file) as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(",")
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)

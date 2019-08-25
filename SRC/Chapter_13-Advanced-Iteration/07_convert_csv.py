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

# Solving using dict Comphrehension
more_flights = {}

more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
print("------Comprehensions---")
pprint.pprint(more_flights)

print("------Filter Comprehensions---")
filtered_flights = {}

filtered_flights = {
    convert2ampm(k): v.title() for k, v in flights.items() if v == "FREEPORT"
}
pprint.pprint(filtered_flights)

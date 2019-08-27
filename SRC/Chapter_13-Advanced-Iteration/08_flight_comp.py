from datetime import datetime

flights = {
    "09:35": "FREEPORT",
    "09:55": "WEST END",
    "10:45": "TREASURE CAY",
    "11:45": "ROCK SOUND",
    "12:00": "TREASURE CAY",
    "17:00": "FREEPORT",
    "17:55": "ROCK SOUND",
    "19:00": "WEST END",
}


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, "%H:%M").strftime("%I:%M%p")


flight_times = []
for ft in flights.keys():
    print(ft)
    flight_times.append(convert2ampm(ft))

print()
print(flight_times)

# solving using comprehension
flight_times2 = [convert2ampm(ft) for ft in flights.keys()]

print(flight_times2)

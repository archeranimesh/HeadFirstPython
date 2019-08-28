from datetime import datetime

string = "I DID NOT MEAN TO SHOUT"
print(string.title())

time = "09:35"


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, "%H:%M").strftime("%I:%M%p")


print(convert2ampm(time))

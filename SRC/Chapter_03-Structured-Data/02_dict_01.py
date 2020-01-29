import pprint

person = {
    "Name": "Ford Prefect",
    "Gender": "Male",
    "Occupation": "Researcher",
    "Home Planet": "Betelgeuse Seven",
}

pprint.pprint(person)

print(person["Name"])

person["Age"] = 33
pprint.pprint(person)

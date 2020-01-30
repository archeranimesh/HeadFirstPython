import pprint

found = {}
found["a"] = 0
found["e"] = 0
found["i"] = 0
found["o"] = 0
found["u"] = 0

pprint.pprint(found)

# update a value
found["i"] = found["i"] + 1
pprint.pprint(found)

# += gives another way to increment.
found["a"] += 1
pprint.pprint(found)

for k, v in found.items():
    print(k, "was found", v, "times.")

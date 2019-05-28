vowels = {"a", "e", "i", "o", "u"}
message = "Don't forget to pack your towel."

found = set()
for v in vowels:
    if v in message:
        found.add(v)

print(found)
print()

found2 = {v for v in vowels if v in message}

print(found2)

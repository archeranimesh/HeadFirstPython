first = [1, 2, 3, 4, 5]
second = first

print("first: ", first)
print("second:", second)

first.append(6)
print("first: ", first)
print("second:", second)

third = first.copy()
print("first: ", first)
print("second: ", second)
print("third: ", third)

first.append(7)
print("first: ", first)
print("second: ", second)
print("third: ", third)

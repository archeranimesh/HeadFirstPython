phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# remove the last 4 char "nic!"
for i in range(4):
    plist.pop()

# Remove the first char, D
plist.pop(0)
# Remove the ', list is ont pa
plist.remove("'")

# Swap last 2 character, list is ont ap
plist.extend([plist.pop(), plist.pop()])
# Shifts the space by 1 index, list is on tap
plist.insert(2, plist.pop(3))

new_phrase = "".join(plist)
print(plist)
print(new_phrase)

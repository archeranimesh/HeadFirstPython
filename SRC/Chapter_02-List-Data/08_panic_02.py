phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = "".join(plist[1:3])
print(new_phrase)
new_phrase = new_phrase + "".join([plist[5], plist[4], plist[7], plist[6]])
print("".join([plist[5], plist[4], plist[7], plist[6]]))
print(plist)
print(new_phrase)

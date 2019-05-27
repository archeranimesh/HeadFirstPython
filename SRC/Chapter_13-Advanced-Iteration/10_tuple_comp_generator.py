for i in [x ** 3 for x in [1, 2, 3, 4, 5]]:
    print(i)

for i in (x ** 3 for x in [1, 2, 3, 4, 5]):
    print(i)

mytuple = (x ** 3 for x in [1, 2, 3, 4, 5])

for x in mytuple:
    print(x)

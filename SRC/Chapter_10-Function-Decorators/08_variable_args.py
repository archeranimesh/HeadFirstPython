def myfunc(*args):
    for a in args:
        print(a, end=" ")
    if args:
        print()


if __name__ == "__main__":

    values = [1, 2, 3, 4, 5, 6]
    myfunc(10)
    myfunc()
    myfunc(10, 20, 30, 40, 50)
    myfunc(values)
    myfunc(*values)

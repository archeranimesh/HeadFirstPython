def outer():
    def inner():
        print("This is Inner")

    print("This is outer, invoking inner")
    return inner


if __name__ == "__main__":
    i = outer()
    print(type(i))
    i()

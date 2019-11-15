def outer():
    def inner():
        print("This is Inner")

    print("This is outer, invoking inner")
    inner()


if __name__ == "__main__":
    outer()

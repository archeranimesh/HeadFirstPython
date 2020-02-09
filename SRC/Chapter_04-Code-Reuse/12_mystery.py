def double(arg):
    print("Before: ", arg)
    arg = arg * 2
    print("After: ", arg)


def change(arg):
    print("Before: ", arg)
    arg.append("more data")
    print("After: ", arg)


if __name__ == "__main__":
    # Call by Value
    num = 10
    double(num)
    print("num = ", num)
    saying = "Hello"
    double(saying)
    print("saying: ", saying)
    numbers = [10, 20, 30]
    double(numbers)
    print("numbers: ", numbers)

    # Call by reference.
    change(numbers)
    print("numbers = ", numbers)

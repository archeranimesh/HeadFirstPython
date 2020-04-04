msg = "Hello from Head First Python 2e"


def hello():
    print(msg)


if __name__ == "__main__":
    print("Id of message is: ", id(msg))
    print("Id of function is: ", id(hello))
    print("type of function is: ", type(hello))
    print(type(id))

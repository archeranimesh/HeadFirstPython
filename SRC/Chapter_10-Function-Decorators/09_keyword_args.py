def myfunckw(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep="->", end=" ")
    if kwargs:
        print()


if __name__ == "__main__":
    dbconfig = {
        "host": "127.0.0.1",
        "user": "vsearch",
        "password": "hello",
        "database": "vsearchlogDB",
    }
    myfunckw(a=10, b=20)
    myfunckw(**dbconfig)

def myfunc_args(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=" ")
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep="->", end=" ")
        print()


if __name__ == "__main__":
    myfunc_args()
    myfunc_args(1, 2, 3)
    myfunc_args(a=10, b=20, c=30)
    myfunc_args(1, 2, 3, a=10, b=20, c=30)


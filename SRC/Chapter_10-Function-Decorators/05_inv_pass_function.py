def apply(func: object, value: object) -> object:
    return func(value)


if __name__ == "__main__":
    (apply(print, 42))
    print(apply(id, 42))
    print(apply(type, 42))
    print(apply(len, "marvin"))

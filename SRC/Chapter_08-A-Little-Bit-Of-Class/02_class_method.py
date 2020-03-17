class CountFromBy:
    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr


a = CountFromBy(100, 10)
a.increase()
print(a.incr, a.val)

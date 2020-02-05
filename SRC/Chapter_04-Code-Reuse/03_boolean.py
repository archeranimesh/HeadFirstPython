# All of the below code evulates to False
print("bool(0): ", bool(0))
print("bool(0.0): ", bool(0.0))
print("bool(''): ", bool(""))
print("bool([])", bool([]))
print("bool({})", bool({}))
print("bool(None)", bool(None))

# All the below code evaluates to True.
print("bool(1)", bool(1))
print("bool(-1)", bool(-1))
print("bool(42)", bool(42))
print("bool(0.0000000000000001)", bool(0.0000000000000001))
print("bool('Panic')", bool("Panic"))
print("bool([42,43,44])", bool([42, 43, 44]))
print("bool({'a' : 42, 'b' : 42})", bool({"a": 42, "b": 42}))

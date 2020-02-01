vowels = set("aeiou")
word = "hello"

# Union operation
# Combines 1 set with another.
u = vowels.union(set(word))
print("Union = ", u)

# Difference operation
# It tells what is present in 1 set bit not in other.
d = vowels.difference(set(word))
print("Diff = ", d)

# Intersection Operation
# Returns the common object in 2 sets.
i = vowels.intersection(set(word))
print("Intersection: ", i)

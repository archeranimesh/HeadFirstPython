nums = [1, 2, 3, 4]

print("Before Remove: ", nums)
nums.remove(3)
print("After Remove: ", nums)

print(nums.pop())
print("After Pop", nums)

nums.extend([3, 4])
print("After Extend: ", nums)

nums.insert(0, 1)
print("After insert: ", nums)

nums.append([])
print("After append: ", nums)

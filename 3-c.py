import numpy as np

# Sorting
# Sort along the first axis
a = np.array([[12, 15], [10, 1]])
sorted_first_axis = np.sort(a, axis=0)
print("Sorted along first axis:\n", sorted_first_axis)

# Sort along the last axis
a = np.array([[10, 15], [12, 1]])
sorted_last_axis = np.sort(a, axis=-1)
print("\nSorted along last axis:\n", sorted_last_axis)

# Sort along none axis (flattened)
a = np.array([[12, 15], [10, 1]])
sorted_none_axis = np.sort(a, axis=None)
print("\nSorted along none axis (flattened):\n", sorted_none_axis)

# Searching
array = np.arange(12).reshape(3, 4)
print("\nInput ARRAY:\n", array)

# Maximum element without specifying axis
print("\nMax element:", np.max(array))

# Indices of the max element along axis 0 and axis 1
print("Indices of Max element along axis 0:", np.argmax(array, axis=0))
print("Indices of Max element along axis 1:", np.argmax(array, axis=1))

# Counting
# Counting the number of non-zero values
a = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
b = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 0, 19]])

print("\nNumber of nonzero values (a):", a)
print("Number of nonzero values (b):", b)

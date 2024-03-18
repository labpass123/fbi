import numpy as np


a = np.array([[12, 15], [10, 1]])
sorted_first_axis = np.sort(a, axis=0)
print("Sorted along first axis:\n", sorted_first_axis)


a = np.array([[10, 15], [12, 1]])
sorted_last_axis = np.sort(a, axis=-1)
print("\nSorted along last axis:\n", sorted_last_axis)

a = np.array([[12, 15], [10, 1]])
sorted_none_axis = np.sort(a, axis=None)
print("\nSorted along none axis (flattened):\n", sorted_none_axis)


array = np.arange(12).reshape(3, 4)
print("\nInput ARRAY:\n", array)


print("\nMax element:", np.max(array))


print("Indices of Max element along axis 0:", np.argmax(array, axis=0))
print("Indices of Max element along axis 1:", np.argmax(array, axis=1))


a = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
b = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 0, 19]])

print("\nNumber of nonzero values (a):", a)
print("Number of nonzero values (b):", b)

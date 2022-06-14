import numpy as np


arr = np.array([
    [0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
])

print(arr)
print(arr.shape)
#全要素数size
print(arr.size)
#次元数ndim
print(arr.ndim)
#データの型dtype
print(arr.dtype)

arr = np.array([
    [0.0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
])

print(arr)
print(arr.dtype)

arr = np.array([
    [0, 1, 2, 3, 4],
    [-10, -11, -12, -13, -14],
    [20, 21, 22, 23, 24],
], dtype=float)

print(arr)
print(arr.dtype)

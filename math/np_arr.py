import numpy as np

# Define the matrices to be multiplied
A = np.array([[1, 2], [3, 4]])  # 2x2 matrix
B = np.array([[5, 6], [7, 8]])  # 2x2 matrix

# Multiply the matrices
C = np.dot(A, B)

# Print the result
print(C)


arrayA = np.array([
    [1, 2, 3, 4],
    [3, 4, 5, 6],
    [5, 6, 7, 8],
    [8, 9, 10, 11]
])
arrayB = np.array([
    [1, 2, 3, 4],
    [3, 4, 5, 6],
    [5, 6, 7, 8],
    [8, 9, 10, 11]
])

result  = np.dot(arrayA, arrayB)

print(result)
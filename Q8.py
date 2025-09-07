import numpy as np
print("Enter elements of first 3x3 matrix:")
A = []
for i in range(3):
    A.append(list(map(int, input().split())))
A = np.array(A)
print("Enter elements of second 3x3 matrix:")
B = []
for i in range(3):
    B.append(list(map(int, input().split())))
B = np.array(B)
C = A + B
print("\nSum of two matrices:")
print(C)

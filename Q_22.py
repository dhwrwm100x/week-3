matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
ptr = matrix  

print("Original Matrix (through matrix):")
for row in matrix:
    print(row)

print("\nAccessing Matrix through ptr:")
for row in ptr:
    print(row)

# Modify using "ptr"
ptr[0][0] = 99

print("\nAfter modifying ptr[0][0] = 99")
print("Matrix:")
for row in matrix:
    print(row)

print("\nPtr:")
for row in ptr:
    print(row)
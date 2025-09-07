def is_symmetric(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
n = int(input("Enter size of square matrix: "))

matrix = []
print("Enter elements row by row:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

if is_symmetric(matrix, n):
    print("The matrix is symmetric.")
else:
    print("The matrix is NOT symmetric.")
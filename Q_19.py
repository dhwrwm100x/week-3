def is_lower_triangular(matrix, n):
    for i in range(n):
        for j in range(i+1, n):   
            if matrix[i][j] != 0:
                return False
    return True
n = int(input("Enter size of square matrix: "))

matrix = []
print("Enter elements row by row:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

if is_lower_triangular(matrix, n):
    print("The matrix is lower triangular.")
else:
    print("The matrix is NOT lower triangular.")
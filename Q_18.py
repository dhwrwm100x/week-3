def is_upper_triangular(matrix, n):
    for i in range(1, n):          
        for j in range(0, i):      
            if matrix[i][j] != 0:
                return False
    return True
n = int(input("Enter size of square matrix: "))

matrix = []
print("Enter elements row by row:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

if is_upper_triangular(matrix, n):
    print("The matrix is upper triangular.")
else:
    print("The matrix is NOT upper triangular.")
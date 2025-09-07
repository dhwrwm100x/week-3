n = int(input("Enter size of square matrix (n x n): "))

print("Enter matrix elements row by row:")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_above = 0
for i in range(n):
    for j in range(n):
        if i < j:  
            sum_above += matrix[i][j]

print("Sum of elements ABOVE main diagonal:", sum_above)
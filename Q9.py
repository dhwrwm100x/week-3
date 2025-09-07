n = int(input("Enter the size of the square matrix: "))
matrix = []

print("Enter the elements row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

product = 1
for i in range(n - 1):  
    product *= matrix[i][i + 1]

print("Product of elements above the main diagonal:", product)

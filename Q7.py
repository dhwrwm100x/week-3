def read_matrix(n):
    matrix = [] 
    print(f"Enter elements row by row for a {n}x{n} matrix:")
    for i in range(n):
        row = list(map(int, input().split())) 
        matrix.append(row)
    return matrix

def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]  
    return total

n = int(input("Enter size of square matrix: "))
matrix = read_matrix(n)

print("\nMatrix:")
for row in matrix:
    print(row)

print("\nSum of main diagonal elements:", diagonal_sum(matrix))

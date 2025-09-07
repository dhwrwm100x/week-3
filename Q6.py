def read_matrix(n):
    matrix = []
    print(f"Enter elements row by row for a {n}x{n} matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    print("\nMatrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

n = int(input("Enter size of square matrix: "))
matrix = read_matrix(n)
display_matrix(matrix)

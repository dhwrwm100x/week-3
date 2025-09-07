def calculate_result(A, B, X, Y, n, m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            val = X * A[i][j] + Y * B[i][j]
            row.append(val)
        result.append(row)
    return result
X, Y = 2, 3
n, m = map(int, input("Enter rows and columns of matrices: ").split())

print("Enter matrix A:")
A = [list(map(int, input().split())) for _ in range(n)]

print("Enter matrix B:")
B = [list(map(int, input().split())) for _ in range(n)]

result = calculate_result(A, B, X, Y, n, m)

print("Result (2A + 3B) is:")
for row in result:
    print(*row)
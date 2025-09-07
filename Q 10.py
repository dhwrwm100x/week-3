matrix = [
    [1, 0, 3],
    [0, 0, 6],
    [7, 8, 0]
]

count = 0
for row in matrix:
    for element in row:
        if element != 0:
            count += 1

print("Total number of nonzero elements:", count)

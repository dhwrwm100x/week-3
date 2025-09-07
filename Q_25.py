n = int(input("Enter number of elements: "))
arr = []
print("Enter float numbers:")
for _ in range(n):
    arr.append(float(input()))
new_num = float(input("Enter the new number to insert: "))
pos = int(input("Enter the position (0-based index): "))
if 0 <= pos <= len(arr):
    arr.insert(pos, new_num)
    print("Updated array:", arr)
else:
    print("Invalid position!")
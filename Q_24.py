n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for _ in range(n):
    arr.append(int(input()))
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)

print("Array after removing duplicates:", unique_arr)
arr1 = list(map(float, input("Enter elements of first array: ").split()))
arr2 = list(map(float, input("Enter elements of second array: ").split()))
merged = arr1 + arr2
print("Resultant array in reverse order:")
print(merged[::-1])
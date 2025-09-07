arr = list(map(int, input("Enter array elements: ").split()))

sorted_arr = sorted(arr)

second_smallest = sorted_arr[1]
second_largest = sorted_arr[-2]
i = arr.index(second_smallest)
j = arr.index(second_largest)
arr[i], arr[j] = arr[j], arr[i]

print("Array after swapping second smallest and second largest:")
print(arr)
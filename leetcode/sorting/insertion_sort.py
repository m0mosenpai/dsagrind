array = [12, 11, 13, 5, 6]
print(f"Unsorted array is: {array}")

for i in range(1, len(array)):
    while i > 0 and array[i] < array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]
        i -= 1

print(f"Sorted array is: {array}")

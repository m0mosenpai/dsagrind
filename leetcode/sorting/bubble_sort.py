# 3, 1, 5, 4, 2

array = [3, 1, 5, 4, 2]
print(f"The unsorted array: {array}")

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[j], array[i] = array[i], array[j]

print(f"The sorted array: {array}")

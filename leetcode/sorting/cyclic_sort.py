# 3 5 2 1 4
#
array = [3, 5, 2, 1, 4]
print(f"Unsorted array is: {array}")

for i in range(len(array)):
    while array[i] - 1 != i:
        val = array[i] - 1
        array[i], array[val] = array[val], array[i]

print(f"Sorted array is: {array}")

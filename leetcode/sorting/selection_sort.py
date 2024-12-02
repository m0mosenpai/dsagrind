array = [4, 5, 1, 2, 3]
print(f"The unsorted array is: {array}")

for i in range(len(array)):
    min_ = i
    for j in range(i + 1, len(array)):
        if array[min_] > array[j]:
            min_ = j

    array[i], array[min_] = array[min_], array[i]

print(f"The sorted array is: {array}")

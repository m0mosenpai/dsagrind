def binary_search(array):
    left = 0
    right = len(array) - 1

    while (left < right):
        mid = left + (right - left) // 2

        if array[mid] > array[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

array = [1, 2, 3, 5, 6, 4, 3, 2]
print(f"This is the sample array: {array}")
print(f"Peak Index of the mountain array is: {binary_search(array)}")


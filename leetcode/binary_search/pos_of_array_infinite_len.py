arr = [2, 3, 5, 6, 7, 8, 10, 11, 12, 15, 20, 23, 30]

def binary_search(arr, target):
    low, high = 0, 1

    # Traversing in chunks through the assumed infinite array
    # Chunk size increases exponentially till we find the element to be between low and high
    while target > arr[high]:
        tmp = high + 1
        high = high + (high - low + 1) * 2
        low = tmp

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid

    return -1

print(f"This is the array: {arr}")
target = int(input("Enter the target number: "))
print(binary_search(arr, target))


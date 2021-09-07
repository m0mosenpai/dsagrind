def get_peak(array):
    left = 0
    right = len(array) - 1

    while (left < right):
        mid = left + (right - left) // 2

        if array[mid] > array[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while (left <= right):
        mid = left + (right - left) // 2
        asc = True
        if array[0] > array[-1]:
            asc = False

        if asc:
            if array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid - 1
            else:
                return mid
        else:
            if array[mid] < target:
                right = mid - 1
            elif array[mid] > target:
                left = mid + 1
            else:
                return mid

    return -1

array = [1, 5, 2]
print(f"This is the sample array: {array}")
target = int(input("Enter the target value: "))
# First we find the peak of the mountain array
peak = get_peak(array)
# Search in the first half of the array
first_search = binary_search(array[:peak], target)
if first_search == -1:
    print("Target not found in first half of the array. Searching in second half...")
    second_search = binary_search(array[peak:], target)
    if second_search != -1:
        print(f"Target found in second half of the array: {peak + second_search}")
    else:
        print(f"Target not found in the complete array!")
else:
    print(f"Target found in first half of the array: {first_search}")


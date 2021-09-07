# Example of rotated sorted array: 3, 4, 5, 6, 7, 0, 1, 2
# Not rotated sorted array: 0, 1, 2, 3, 4, 5, 6, 7
def find_pivot(arr):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = start + (end - start) // 2

        # 4 possible cases
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid

        if mid > start and arr[mid - 1] > arr[mid]:
            return mid - 1

        # Handling duplicate cases
        if (arr[mid] == arr[start] == arr[end]):
            # Check if the duplicates are pivots
            if (arr[start] > arr[start + 1]):
                return start

            # Skip start by 1
            start += 1

            if arr[end] < arr[end - 1]:
                return end

            # Skip end by 1
            end -= 1

        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid - 1

    return -1

def binary_search(arr, target, start, end):
    while (start <= end):
        mid = start + (end - start) // 2

        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return -1

arr = [3, 4, 5, 6, 7, 0, 1, 2]
print(f"This is the rotated sorted array: {arr}")
target = int(input("Enter the target num: "))

# Finding the pivot of the array
pivot = find_pivot(arr)
print(f"The pivot is: {pivot}")
if pivot == -1:
    # Do normal binary search as array is not rotated
    print("Array not rotated!")
    print(f"Performing normal binary search: {binary_search(arr, target, 0 , len(arr) - 1)}")
else:
    if arr[pivot] == target:
        print(f"Pivot is target!: {pivot}")
    elif target >= arr[0]:
        print("BS in first half: ", end='')
        print(binary_search(arr, target, 0, pivot - 1))
    else:
        print("BS in second half: ", end='')
        print(binary_search(arr, target, pivot + 1, len(arr) - 1))

    print(f"Array is rotated {pivot + 1} times")


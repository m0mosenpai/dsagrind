# Finding the largest number just smaller than/equal to target.
def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while (left <= right):
        mid = left + (right - left) // 2

        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid

    return right

array = [2, 3, 5, 9, 14, 16, 18]
print(f"This is the sample array: {array}")
target = int(input("Enter the target number: "))
print(f"This number just smaller or equal to target: {array[binary_search(array, target)]}")


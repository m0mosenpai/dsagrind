nums = [5, 7, 7, 7, 7, 8, 8, 10]

def binary_search(nums, target, side):
    # Incase list is empty, no number will be found in it
    if not nums:
        return [-1, - 1]

    left = 0
    right = len(nums) - 1
    idx = -1

    # Applying BS for finding the start or end position of the target element
    while left <= right:
        mid = left +  (right - left) // 2

        if target == nums[mid]:
            idx = mid
            if side == "end":
                left = mid + 1
            else:
                right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return idx

print(f"This is the array: {nums}")
target = int(input("Enter the target element: "))

start_idx = binary_search(nums, target, "start")
end_idx  = binary_search(nums, target, "end")
print(f"Starting Index: {start_idx}")
print(f"Ending Index: {end_idx}")




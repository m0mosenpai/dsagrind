# Example: [2, 3, 4, 7, 11], k = 5
# Assuming full array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            missing = arr[mid] - mid + 1

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return k + low



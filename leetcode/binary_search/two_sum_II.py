# Example: [2, 7, 11, 15], target: 9
# Example: [3, 24, 50, 79, 88, 150, 345], target: 200
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            sum_ = numbers[left] + numbers[right]
            if sum_ > target:
                right -= 1
            elif sum_ < target:
                left += 1
            else:
                return [left + 1, right + 1]


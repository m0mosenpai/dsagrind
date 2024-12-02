# 1 3 4 2 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[nums[0]] != nums[0]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]

        return nums[0]

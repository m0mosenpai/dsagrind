# 3 0 1
# 0 1 3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while nums[i] < length and nums[i] != i:
                swap = nums[i]
                nums[i], nums[swap] = nums[swap], nums[i]

        for i in range(length):
            if i != nums[i]:
                return i

        return length



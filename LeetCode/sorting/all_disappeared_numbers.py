class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> int:
        length = len(nums)
        missing_nums = []
        for i in range(length):
            while nums[i] - 1 != i:
                swap = nums[i] - 1
                if nums[swap] == nums[i]:
                    break

                nums[i], nums[swap] = nums[swap], nums[i]

        for i in range(length):
            if i != nums[i] - 1:
                missing_nums.append(i + 1)

        return missing_nums

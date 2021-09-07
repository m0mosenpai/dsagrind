class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # We define here, 2 limits for the possible max sum:
        # -> Incase we only divide the array in 1 subsection, the min max-value of each section can only be the sum of all elements.
        # -> Incase we divide the array in n subsections, the min max-value of each section can only be the max value in the array.
        # Hence, we take the range to be [max value in array, sum of all values in array].
        # We'll apply binary search in this range to find the perfect minimum max-value, while making sure we divide the array in exactly m pieces.

        # We'll start from the max value in the array
        start = max(nums)
        # We'll end at the sum of all the values in the array
        end = sum(nums)

        while (start < end):
            # Assume middle value in the range is our desired sum of each subarray
            mid = start + (end - start) // 2

            sum_ = 0
            pieces = 1

            for num in nums:
                # Try to add a num in the current subarray making sure the sum of the subarray doesn't exceed our assumed max
                # Cannot add a new num in the current subarray. Will have to create a new one.
                if sum_ + num > mid:
                    # Reset the sum to only include the new num, since a new subarray is created.
                    sum_ = num
                    # Increment the pieces count since a new subarray has been created.
                    pieces += 1
                else:
                    # Keep adding num to the sum otherwise.
                    sum_ += num

            # If pieces turn out to be greater than what was required, we need to decrease our assumed sum of each subarray
            if pieces > m:
                start = mid + 1
            else:
                # If pieces turn out to be smaller than what was required, we need to increase our assumed sum of each subarray
                end = mid

        # In the end, start == end
        return end

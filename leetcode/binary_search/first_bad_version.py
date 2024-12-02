# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# Example: [1, 2, 3, 4, 5]
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If there is only 1 version, return it as it is
        if n == 1:
            return 1

        # Starting from the first version released to the latest version
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            is_bad = isBadVersion(mid)

            # If current version is bad and the one before it is not, found the ans
            if is_bad and not isBadVersion(mid - 1):
                return mid

            # If current version is not bad, reduce search space to start from the one after it
            if not is_bad:
                low = mid + 1
            else:
                high = mid - 1



# possible square root of a number can be in the range: [0, number itself]
# Example: [0, 8], 4, [0, 4], 2
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        low = 0
        high = x // 2

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1

        return mid - 1 if mid * mid > x else mid


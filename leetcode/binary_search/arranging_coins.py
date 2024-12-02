# Example: [1, 2, 3, 4, 5]
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                right = mid - 1
            else:
                left = mid + 1

        return right


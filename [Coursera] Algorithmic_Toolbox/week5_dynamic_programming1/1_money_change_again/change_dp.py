# Uses python3
import sys

# Bottom's Up Iterative DP
# Time - O(S * n) | Space - O(S)
def get_change(m):
	dp = [float("inf") for i in range(m + 1)]
	dp[0] = 0
	coins = [1, 3, 4]

	for coin in coins:
		for x in range(coin, m + 1):
			dp[x] = min(dp[x], dp[x - coin] + 1)

	return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0 for i in range(n)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10

    return (dp[-1] + dp[-2]) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))

# Uses python3
import sys

'''
    +1  *2  *3
1   0   0   0   =   0
2   0   1   0   =   1
3   0   0   3   =   3
4   0   2   0   =   
5   2   0   1   =   3

'''

# We take operations it took to get 1 less than current number as current minimum ops.
# If current is divisible by 3 or 2, we check if operations to get number by multiplying by 2 or 3 exceed operations used to get by adding 1.
# Accordingly, we update min number of operations and keep a track of the last number before one arithemtic operation (parent)
# Finally, we trace back all parents till we reach 1 and return the reversed list.

# Time Complexity - O(n) | Space Complexity - O(n)
def optimal_sequence(n):
    dp = [0 for i in range(n + 1)]
    parents = [None for i in range(n + 1)]
    sequence = []

    for i in range(1, n + 1):
        current_parent = i - 1
        current_min_ops = dp[i - 1] + 1

        if i % 3 == 0:
            parent = i // 3
            ops = dp[parent] + 1
            if ops < current_min_ops:
                current_parent, current_min_ops = parent, ops

        if i % 2 == 0:
            parent = i // 2
            ops = dp[parent] + 1
            if ops < current_min_ops:
                current_parent, current_min_ops = parent, ops

        dp[i], parents[i] = current_min_ops, current_parent

    sequence = []
    i = n
    while i > 0:
        sequence.append(i)
        i = parents[i]
    sequence.reverse()

    return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

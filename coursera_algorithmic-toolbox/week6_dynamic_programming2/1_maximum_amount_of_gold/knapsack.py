# Uses python3
import sys

'''
Weights -> 1, 4, 8
Total Weight -> 10

	0	1	2	3	4	5	6	7	8	9	10
0	0	0	0	0	0	0	0	0	0	0	0
1	0	1	1	1	1	1	1	1	1	1	1
4	0	1	1	1	4	5	5	5	5	5	5
8	0	1	1	1	4	5	5	5	8	9	9

-> First row is all 0s since no items can be put into a bag of max capacity 0
-> In second row, gold bar with weight 1 can be considered once the bag's capacity is atleast 1 Kg.
Henceforth, since there's only a single bar in consideration, max weight remains unchanged.
-> In third row, we can't consider gold bar of weight 4 Kg till bag's max capacity is atleast 4 Kg.
Thereafter, we have the choice to either not consider 4 Kg bar (take value from previous row i.e 1 Kg in the bag),
or consider it by adding it's weight to the weight of the bag without it. (taking value from (i - weight) column and previous row).
We consider whichever choice gives us max weight.
-> Rest of the rows follow similar pattern and the final cell of the table gives us the solution.
'''

def optimal_weight(W, w):
	dp = [[0 for _ in range(W + 1)] for _ in range(len(w) + 1)]


	for i in range(1, len(w) + 1):
		for j in range(1, W + 1):
			if w[i - 1] > j:
				dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + w[i - 1])

	return dp[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

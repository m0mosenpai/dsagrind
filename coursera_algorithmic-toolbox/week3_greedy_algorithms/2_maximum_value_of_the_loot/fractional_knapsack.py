# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	# Calculate value/weight for all objects and sort them in descending order
	vpw = [(values[i]/weights[i], i) for i in range(len(weights))]
	vpw.sort(reverse = True)
	_sum = 0.

	for _max in vpw:
		# If weight of most valuable object is greater than total capacity, fill knapsack with max fraction of it
		if weights[_max[1]] > capacity:
			_sum += values[_max[1]] * (capacity/weights[_max[1]])
			capacity = 0
			break
		# Otherwise, put in knapsack and consider the next most valuable item
		else:
			_sum += values[_max[1]]
			capacity -= weights[_max[1]]

	return _sum

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

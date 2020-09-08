# Uses python3
import sys

def optimal_summands(n):
	summands = []
	total = n
	for i in range(1, n):
		if total - i == 0:
			summands.append(i)
			break

		if total - i >= i + 1:
			summands.append(i)
			total -= i

	if not summands:
		summands.append(n)

	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

# Uses python3
import sys

# 
def pisanoPeriod(m):
	prev, current = 0, 1
	for i in range(0, m*m):
		prev, current = current, (prev + current) % m

		if (prev == 0 and current == 1):
			return i + 1

def get_fibonacci_huge_naive(n, m):
    pisano = pisanoPeriod(m)
    n = n % pisano

    prev, current = 0, 1
    if n == 0:
    	return 0
    elif n == 1:
    	return 1
    for i in range(n - 1):
    	prev, current = current, prev + current

    return (current % m)


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

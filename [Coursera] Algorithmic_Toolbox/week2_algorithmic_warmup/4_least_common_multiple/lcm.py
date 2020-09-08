# Uses python3
import sys

def lcm_naive(a, b):
	prod = a * b
	while a % b != 0:
		a, b = b, a % b

	return int(prod / b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


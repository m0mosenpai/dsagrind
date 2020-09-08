#Uses python3

import sys

# Concatenates both possible ways to form a number and returns the larger of the 2
def check(digit, maxDigit):
	return int(str(digit) + str(maxDigit) >= str(maxDigit) + str(digit))


def largest_number(a):
	ans = ''
	while a:
		maxDigit = 0
		for digit in a:
			if check(str(digit), str(maxDigit)):
				maxDigit = digit
		ans += str(maxDigit)
		a.remove(maxDigit)

	return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

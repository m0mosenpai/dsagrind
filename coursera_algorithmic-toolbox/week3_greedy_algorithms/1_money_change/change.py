# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]
    denom = 0
    for c in coins:
    	if m >= c:
    		denom += int(m/c)
    		m %= c

    return denom

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

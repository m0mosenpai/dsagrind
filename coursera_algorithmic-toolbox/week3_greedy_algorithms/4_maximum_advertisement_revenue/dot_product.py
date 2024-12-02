#Uses python3

import sys

# Sort and greedy
def max_dot_product(a, b):
    a.sort(reverse = True)
    b.sort(reverse = True)
    _sum = 0
    for i in range(len(a)):
        _sum += (a[i]*b[i])

    return _sum


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    

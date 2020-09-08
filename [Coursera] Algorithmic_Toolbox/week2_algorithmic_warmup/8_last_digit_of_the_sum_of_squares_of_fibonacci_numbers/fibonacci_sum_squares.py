# Uses python3
from sys import stdin

def pisanoPeriod(m):
    prev, current = 0, 1
    for i in range(0, m*m):
        prev, current = current, (prev + current) % m

        if (prev == 0 and current == 1):
            return i + 1

def process(n):
    prev, current = 0, 1
    for i in range(2, n + 1):
        prev, current = current, (prev + current) % 10

    return current

def fibonacci_sum_squares_naive(n):
    pisano = pisanoPeriod(10)
    n_1 = n % pisano
    n_2 = (n + 1) % pisano

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    if n_1 <= 1:
        a = n_1
    else:
        a = process(n_1)

    if n_2 <= 1:
        b = n_2
    else:
        b = process(n_2)

    return (a * b) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))

# Uses python3
import sys

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

    return (current - 1)

def fibonacci_partial_sum_naive(from_, to):
    pisano = pisanoPeriod(100)
    n_1 = (from_ + 1) % pisano
    n_2 = (to + 2) % pisano

    a = process(n_1)
    b = process(n_2)

    if b - a >= 0:
        return b - a
    else:
        return 10 + (b - a)
   
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
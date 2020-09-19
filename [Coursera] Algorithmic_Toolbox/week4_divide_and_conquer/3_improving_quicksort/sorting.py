# Uses python3
import sys
import random

# 3-way partition using Dutch National Flag Problem approach
# O(n) Time | O(1) Space
def partition3(a, l, r):
    pivot = a[l]
    i = l

    while i <= r and l < r:
        if a[i] < pivot:
            a[i], a[l] = a[l], a[i]
            l += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[r] = a[r], a[i]
            r -= 1
        else:
            i += 1

    # The final positions of l and r mark the first and last occurences of the pivot    
    return [l, r]

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m_1, m_2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m_1 - 1);
    randomized_quick_sort(a, m_2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

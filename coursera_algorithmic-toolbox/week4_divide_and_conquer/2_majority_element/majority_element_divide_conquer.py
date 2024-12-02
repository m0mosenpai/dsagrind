# Uses python3
import sys

# O(nlog n) time solution using divide n conquer
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    lm = get_majority_element(a, left, int((left + right - 1)/2))
    rm = get_majority_element(a, int((left + right - 1)/2), right)

    l_cnt = 0
    r_cnt = 0

    for i in range(left, right):
        if a[i] == lm:
            l_cnt += 1
    if l_cnt > (right - left) // 2:
        return lm

    for i in range(left, right):
        if a[i] == rm:
            r_cnt += 1
    if r_cnt > (right - left) // 2:
        return rm

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

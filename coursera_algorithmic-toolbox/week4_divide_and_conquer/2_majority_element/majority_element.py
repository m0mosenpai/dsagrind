# Uses python3
import sys

# O(n) time solution using hashmaps
def get_majority_element(a, left, right):
    a_dict = {}
    for i, n in enumerate(a):
        if n not in a_dict.keys():
            a_dict[n] = 1
        else:
            a_dict[n] += 1

    if max(a_dict.values()) > len(a)/2:
        return 1
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

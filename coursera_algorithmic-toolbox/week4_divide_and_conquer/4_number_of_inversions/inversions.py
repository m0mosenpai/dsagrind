# Uses python3
import sys

# O(nlog n) Time | O(n) Space
# Merge function of merge sort
def merge(a, b, left, ave, right):
    i = left
    j = ave
    k = left
    number_of_inversions = 0

    # Take the min of the min element in each array and append it to b (tmp empty array)
    # Do this till one of the sub-arrays becomes empty
    while i <= ave - 1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            # Since both subarrays are sorted, if anyone element in 2nd subarray is greater than 1st, all others afterwards will be greater as well.
            number_of_inversions += (ave - i)
            b[k] = a[j]
            j += 1

        k += 1

    # Merge the remaining elements of the leftover sub-array, as it is, to b
    while i <= ave - 1:
        b[k] = a[i]
        i += 1
        k += 1

    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1

    # Copy tmp b array to original a array
    for i in range(left, right + 1):
        a[i] = b[i]

    return number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0

    # Keep breaking array into sub-arrays till each sub-array only contains a single element, hence being sorted automatically
    if right <= left:
        return number_of_inversions
    ave = (left + right) // 2

    # Total number of inversions will be inversions in left half + inversions in right half + inversions occuring during merging the 2 halves
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave + 1, right)
    number_of_inversions += merge(a, b, left, ave + 1, right)

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))

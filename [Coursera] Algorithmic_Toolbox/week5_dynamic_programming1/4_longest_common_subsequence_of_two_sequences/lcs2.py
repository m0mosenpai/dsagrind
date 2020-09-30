#Uses python3

import sys

'''
            0      l      lo     lon     long    longe    longes    longest
0           0      0      0       0       0        0        0         0
s           0      0      0       0       0        0        1         1    
st          0      0      0       0       0        0        1         2
sto         0      0      1       1       1        1        1         2
ston        0      0      1       2       2        2        2         2 
stone       0      0      1       2       2        3        3         3

'''

# Time Complexity - O(nm) | Space Complexity - O(nm)
def lcs2(a, b):
    dp = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if b[i - 1] == a[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

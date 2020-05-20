# python3

import sys
import threading

def setHeight(node, parents, heightList):
    # If root node, return 1
    if parents[node] == -1:
        heightList[node] = 1;

    if parents[node] >= 0:
        if heightList[parents[node]] == -1:
            setHeight(parents[node], parents, heightList)
        
        heightList[node] = heightList[parents[node]] + 1


def compute_height(n, parents):
    # print("Parents: {}".format(parents))
    # print("Number of nodes: {}".format(n))
    heightList = [-1 for i in range(n)]

    for i, parent in enumerate(parents):
        setHeight(i, parents, heightList)

    # print("Updated HeightList: {}".format(heightList))
    return max(heightList)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

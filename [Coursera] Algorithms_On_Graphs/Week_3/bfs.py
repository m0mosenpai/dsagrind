#Using python3

import sys

def distance(adj, s, t):
    level = {s: 0}
    lvl = 1
    queue = [s]
    while queue:
        # print("Current Queue: {}".format(queue))
        nextQueue = []
        for vertex in queue:
            # print("Vertex: {}".format(vertex))
            for nbr in adj[vertex]:
                # print("Neighbor: {}".format(nbr))
                if nbr not in level:
                    level[nbr] = lvl
                    # print("{} not found in Level. Assigning level {}".format(nbr, lvl))
                    if nbr == t:
                        return level[nbr]

                    nextQueue.append(nbr)
        queue = nextQueue
        lvl += 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

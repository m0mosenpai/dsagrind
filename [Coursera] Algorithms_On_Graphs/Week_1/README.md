# Week-1
![Q1](https://i.imgur.com/a7fQD29.png)
## Explanation
We are taking each cell of the maze to be a node of an undirected graph. Hence, to check if there is a path from any cell A to any other cell B in the maze, it's equivalent to checking if there's a path between any Node A to any other Node B in an undirected graph. <br>
* We perform a DFS with the root node as Node A.
* Every time we visit an unvisited node, we check if that node is Node A. If it is, we simply return True.
* If it's not, we add it to the list of visited nodes and recursively call our function, passing the current node as the new root node. If the recursive call returns True, we return True as well (If A is connected to C and C is connected to B, then A is connected to B). <br>
![Q2](https://i.imgur.com/9mRj61J.png)
## Explanation
A connected component is a group of connected vertices in a graph, in which any vertex can be reached by any other vertex within the component. Calculating the number of CCs is relatively simple:
* Perform a DFS with every vertex of the graph as the root node.
* After every completed DFS (no more vertices can be reached from the current root node), we increment the number of CCs by 1.
* Next iteration, a new unvisited vertex is taken as the root node and all vertices reachable from that vertex are found, hence forming a separate connected component.

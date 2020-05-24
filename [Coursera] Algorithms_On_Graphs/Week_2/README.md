# Week-2
![Q1](https://i.imgur.com/kKjgn7l.png) <br> <br>
## Explanation
To check cyclic dependencies of a curriculum, we need to make sure that for any Course A, there is no pre-requisite Course B such that pre-requisite of Course A is Course B or any of the courses before it. (A consistency check/ No Cyclic Dependencies). This is equivalent to finding a cycle in a directed graph where each Node is a Course.
* We need to keep a track of all vertices we have visited in current DFS. For this, we'll use a stack.
* Do a DFS with each unvisited vertex of the graph as the root node (To account for disconnected graphs) and every call of DFS, we push on to the stack.
* If a neighbor of the current vertex is already visited AND is found in our recursive stack, we simply return 1, indicating that a cycle is indeed present.
* We return 1 if the subsequent recursive call of DFS also returns 1.
* At the end of each recursive call, we pop from the stack. <br>
![Q2](https://i.imgur.com/oha7kyy.png) <br> <br>
## Explanation
![Q3](https://i.imgur.com/8wFVJGk.png) <br> <br>
## Explanation

#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::pair;

int dfs(vector<vector<int> > &adj, int root, vector<int> &visited, vector<int> &stack) {
  stack.emplace_back(root);
  visited.emplace_back(root);
  // std::cout << "Vertex: " << root << std::endl;
  for (int i = 0; i < adj[root].size(); i++){
 	  // std::cout << "Neighbor: " << adj[root][i] << std::endl;
      if (std::find(visited.begin(), visited.end(), adj[root][i]) == visited.end()){
        // std::cout << "Not in visited. Performing DFS" << std::endl;
        if (dfs(adj, adj[root][i], visited, stack)) return 1;
      }
      else if (std::find(stack.begin(), stack.end(), adj[root][i]) != stack.end()){
      	// std::cout << "Found in recursive stack." << std::endl;
      	return 1;
      }
  }
  stack.pop_back();
  return 0;
}

int acyclic(vector<vector<int> > &adj) {
	vector<int> visited;
	vector<int> stack;
  	for (int vertex = 0; vertex < adj.size(); vertex++){
  		if (dfs(adj, vertex, visited, stack)) return 1;
  	}
  	return 0;
 }

int main() {
  size_t n, m;
  std::cin >> n >> m;
  vector<vector<int> > adj(n, vector<int>());
  for (size_t i = 0; i < m; i++) {
    int x, y;
    std::cin >> x >> y;
    adj[x - 1].push_back(y - 1);
  }
  std::cout << acyclic(adj) << std::endl;
}

#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::pair;

vector<int> visited;

void dfs(vector<vector<int> > &adj, int root){
  visited.emplace_back(root);
  for (int i = 0; i < adj[root].size(); i++){
      if (std::find(visited.begin(), visited.end(), adj[root][i]) == visited.end()){
        dfs(adj, adj[root][i]);
      }
  }
}

int number_of_components(vector<vector<int> > &adj) {
  int res = 0;
  for (int vertex = 0; vertex < adj.size(); vertex++){
    if (std::find(visited.begin(), visited.end(), vertex) == visited.end()){
      dfs(adj, vertex);
      res++; 
    }
  }
  return res;
}

int main() {
  size_t n, m;
  std::cin >> n >> m;
  vector<vector<int> > adj(n, vector<int>());
  for (size_t i = 0; i < m; i++) {
    int x, y;
    std::cin >> x >> y;
    adj[x - 1].push_back(y - 1);
    adj[y - 1].push_back(x - 1);
  }
  std::cout << number_of_components(adj);
}

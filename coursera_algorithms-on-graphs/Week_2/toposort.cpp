#include <iostream>
#include <algorithm>
#include <vector>

using std::vector;
using std::pair;

void dfs(vector<vector<int> > &adj, vector<bool> &used, vector<int> &order, int x) {
  used[x] = true;
  for (int i = 0; i < adj[x].size(); i++){
    // std::cout << "Neighbor: " << adj[x][i] << std::endl;
    if (used[adj[x][i]] == false){
        // std::cout << "Not in used, doing DFS" << std::endl;
        dfs(adj, used, order, adj[x][i]);
        }
    }
  // std::cout << "Inserting " << x << " in order" << std::endl;
  order.emplace_back(x);
}    

vector<int> toposort(vector<vector<int> > adj) {
  vector<bool> used;
  for (int i = 0; i < adj.size(); i++)
      used.emplace_back(false);

  vector<int> order;
  for (int vertex = 0; vertex < adj.size(); vertex++){
      // std::cout << "Vertex: " << vertex << std::endl;
      if (used[vertex] == false){
        dfs(adj, used, order, vertex);
      }
    }

  return order;
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
  vector<int> order = toposort(adj);
  for (int i = order.size() - 1; i >= 0; i--) {
    std::cout << order[i] + 1 << " ";
  }
}

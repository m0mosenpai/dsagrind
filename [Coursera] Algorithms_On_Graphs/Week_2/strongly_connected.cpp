#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using std::vector;
using std::pair;
using std::map;

int count = 0;

void post(map<int, int> &postorder, int i) {
  count++;
  // postorder[i] = count;
  postorder[i] = count;
}

void pre() {
  count++;
}

void dfs(vector<vector<int>> &adj, vector<bool> &scc_visited, int root){
  scc_visited[root] = true;
  // std::cout << "Vertex: " << root << std::endl;
  for (int i = 0; i < adj[root].size(); i++){
    // std::cout << "Neighbor: " << adj[root][i] << std::endl;
    if (scc_visited[adj[root][i]] == false){
        // std::cout << "Not in SCC visited, doing DFS" << std::endl;
        dfs(adj, scc_visited, adj[root][i]);
        }
    }

}

void calculatePostorder(vector<vector<int> > &rev_adj, vector<bool> &visited, map<int, int> &postorder, int root) {
  visited[root] = true;
  pre();
  // std::cout << "Vertex: " << root << " pre: " << count << std::endl;
  for (int i = 0; i < rev_adj[root].size(); i++){
    // std::cout << "Neighbor: " << rev_adj[root][i] << std::endl;
    if (visited[rev_adj[root][i]] == false){
        // std::cout << "Not in visited, doing DFS" << std::endl;
        calculatePostorder(rev_adj, visited, postorder, rev_adj[root][i]);
        }
    }
    post(postorder, root);
    // std::cout << "Vertex: " << root << " post: " << count << std::endl;
}

int number_of_strongly_connected_components(vector<vector<int> > rev_adj, vector<vector<int> > adj) {
  int result = 0;
  // vector<int> postorder(rev_adj.size(), -1);
  map<int, int> postorder;
  vector<bool> visited(rev_adj.size(), false);
  for (int vertex = 0; vertex < rev_adj.size(); vertex++){
      // std::cout << "Vertex: " << vertex << std::endl;
      if (visited[vertex] == false){
        calculatePostorder(rev_adj, visited, postorder, vertex);
      }
    }
  // std::cout << "Postorder: ";
  map<int, int>::iterator itr;
  // for (itr = postorder.begin(); itr != postorder.end(); itr++)
  //     std::cout << itr->second << " ";
  // std::cout << std::endl;

  // std::cout << "------Calculating SCC------" << std::endl;
  vector<bool> scc_visited(rev_adj.size(), false);
  while (postorder.size() != 0){
    int max = -1;
    int maxIdx = -1;
    for (itr = postorder.begin(); itr != postorder.end(); itr++){
      if (itr->second > max){
        max = itr->second;
        maxIdx = itr->first;
      }
    }
    // std::cout << "Max: " << max << " Index: " << maxIdx << std::endl;
    if (scc_visited[maxIdx] == false){
        dfs(adj, scc_visited, maxIdx);
        result++;
      }
    postorder.erase(maxIdx);
  }

  return result;
}

int main() {
  size_t n, m;
  std::cin >> n >> m;
  vector<vector<int> > adj(n, vector<int>());
  vector<vector<int> > rev_adj(n, vector<int>());
  for (size_t i = 0; i < m; i++) {
    int x, y;
    std::cin >> x >> y;
    adj[x - 1].push_back(y - 1);
    rev_adj[y - 1].push_back(x - 1);
  }
  std::cout << number_of_strongly_connected_components(rev_adj, adj) << std::endl;
}

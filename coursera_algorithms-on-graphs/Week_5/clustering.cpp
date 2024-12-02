#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <cmath>
#include <queue>
#include <utility>
#include <unordered_map>
#include <set>

using std::vector;
using std::priority_queue;
using std::pair;
using std::make_pair;
using std::unordered_map;
using std::set;

class DisjointSet {
  public:
  unordered_map<int, int> parent;
    void makeSet(vector<int> &wholeset) {
      for (int i: wholeset)
        parent[i] = i;
    }
    // Find root of the set which has l
    int Find(int l) {
      // If l is the root
      if (parent[l] == l)
        return l;
      // Recursively find parent 
      return Find(parent[l]);
    }
    // Perform union of 2 subsets in m and n
    void Union(int m, int n) {
      int x = Find(m);
      int y = Find(n);
      parent[x] = y;
    }
};

double clustering(vector<int> x, vector<int> y, int k) {
  DisjointSet dis;
  int clusters = x.size();
  // Make a separate disjoint set of each vertex
  for (int i = 0; i < x.size(); i++) {
    vector<int> vertex;
    vertex.emplace_back(i);
    dis.makeSet(vertex);
  }
  // priority_queue<pair<double, pair<int, int>>, vector<pair<double, pair<int, int>>>, std::greater<pair<double, pair<int, int>>>> pQueue;
  vector<pair<double, pair<int, int>>> edges;
  //Calculate weights of all edges and store them in edges vector
  for (int i = 0; i < x.size(); i++) {
    for (int j = i + 1; j < x.size(); j++){
        double weight = sqrt(pow((x[i] - x[j]), 2) + pow((y[i] - y[j]), 2));
        // pQueue.push(make_pair(weight, make_pair(i, j)));
        edges.emplace_back(make_pair(weight, make_pair(i, j)));
    }
  }
  // Sort edges in non-decreasing order
  sort(edges.begin(), edges.end());
  // Empty Disjoint Set for edges
  set<pair<int, int>> edgeSet;

  for (int i = 0; i < edges.size(); i++) {
      // std::cout << "Current Cluster: ";
      // for (auto const &it: dis.parent)
          // std::cout << " " << it.first << ":" << it.second;
      // std::cout << std::endl;
      // std::cout << "Vertex A: " << edges[i].second.first << " Vertex B: " << edges[i].second.second << std::endl;
      if (dis.Find(edges[i].second.first) != dis.Find(edges[i].second.second)){
        // std::cout << "Not in the same set" << std::endl;
        edgeSet.insert(make_pair(edges[i].second.first, edges[i].second.second));

        // std::cout << "Current EdgeSet: ";
        // for (const auto& it: edgeSet)
        //     std::cout << "(" << it.first << "," << it.second << ") ";
        // std::cout << std::endl;

        dis.Union(edges[i].second.first, edges[i].second.second);
        clusters --;
        // std::cout << "Number of clusters: " << clusters << std::endl;
        if (clusters == k - 1){
            return edges[i].first;
          }

      }
  }

  // std::cout << "Final EdgeSet: ";
  // for (const auto& it: edgeSet)
  //     std::cout << "(" << it.first << "," << it.second << ") ";
  // std::cout << std::endl;

  return -1.;
} 

int main() {
  size_t n;
  int k;
  std::cin >> n;
  vector<int> x(n), y(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> x[i] >> y[i];
  }
  std::cin >> k;
  std::cout << std::setprecision(10) << clustering(x, y, k) << std::endl;
}

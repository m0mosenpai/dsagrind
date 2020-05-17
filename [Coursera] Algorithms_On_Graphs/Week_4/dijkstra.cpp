#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Compare {
public:
  bool operator()(pair<int, int> n1, pair<int, int> n2) {
    return n1.first < n2.first;
  }
};

vector<int> dijkstra(vector<vector<int>> &adj, vector<vector<int>> &cost, int start) {
  vector<int> dist(adj.size(), 10000);
  dist[start] = 0;
  priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> h; // dist vertex pair
  pair<int, int> t(dist[start], start);
  h.push(t);
  while(!h.empty()) {
    int front = h.top().second;
    h.pop();
    for(int i = 0; i < adj[front].size(); ++i) {
      if(dist[adj[front][i]] > dist[front] + cost[front][i]) {
        dist[adj[front][i]] = dist[front] + cost[front][i]; // Relax edge
        pair<int, int> tt(dist[adj[front][i]], adj[front][i]);
        h.push(tt);
      }
    }
  }
  return dist;
}

int distance(vector<vector<int>> &adj, vector<vector<int>> &cost, int s, int t) {
  int val = dijkstra(adj, cost, s)[t];
  if(val == 10000) val = -1;
  return val;
}

int main() {
  int n, m;
  std::cin >> n >> m;
  vector<vector<int>> adj(n, vector<int>());
  vector<vector<int>> cost(n, vector<int>());
  for (int i = 0; i < m; i++) {
    int x, y, w;
    std::cin >> x >> y >> w;
    adj[x - 1].push_back(y - 1);
    cost[x - 1].push_back(w);
  }
  int s, t;
  std::cin >> s >> t;
  s--, t--;
  std::cout << distance(adj, cost, s, t) << "\n";
}

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <queue>
#include <utility>

using std::vector;
using std::priority_queue;
using std::pair;
using std::make_pair;

class Compare {
public:
  bool operator()(pair<double, int> n1, pair<double, int> n2) {
    return n1.first < n2.first;
  }
};

double minimum_distance(vector<int> x, vector<int> y) {
  // 0th vertex (x[0], y[0])
  int source = 0;
  double result = 0.;
  vector<double> cost(x.size(), 10000);
  vector<int> parent(x.size(), -1);
  vector<bool> inMST(x.size(), false);
  // costance of 0th vertex to itself
  cost[source] = 0;
  priority_queue<pair<double, int>, vector<pair<double, int>>, std::greater<pair<double, int>>> pQueue;
  pQueue.push(make_pair(0, source));

  while(!pQueue.empty()) {
      // Get vertex with min cost
      int U = pQueue.top().second;
      // std::cout << "Vertex with min cost value: " << pQueue.top().first << " (" << x[U] << "," << y[U] << ")" << std::endl;
      // Pop it from the pQueue and add it to MST
      pQueue.pop();
      inMST[U] = true;

      // std::cout << "inMST List:";
      // for (int i = 0; i < inMST.size(); i++)
      //     std::cout << " " << inMST[i];
      // std::cout << std::endl;

      // Go through all it's neighbors
      for (int i = 0; i < x.size(); i++) {
          // std::cout << "Neighbor: (" << x[i] << "," << y[i] << ")" << std::endl;
          double weight = sqrt(pow((x[i] - x[U]), 2) + pow((y[i] - y[U]), 2));
          // std::cout << "Weight: " << weight << std::endl;
          if (inMST[i] == false && cost[i] > weight) {
              // std::cout << "Not in MST" << std::endl;
              // std::cout << "Old Weight: " << cost[i] << " New Weight: " << weight << std::endl;
              cost[i] = weight;
              parent[i] = U;
              pQueue.push(make_pair(cost[i], i));
          }
      }
  }
  // std::cout << "Final costList:";
  for (int i = 0; i < cost.size(); i++){
      // std::cout << " " << cost[i];
      result += cost[i];
    }

  // std::cout << "Final ParentList:";
  // for (int i = 0; i < parent.size(); i++)
  //     std::cout << " " << parent[i];
  // std::cout << std::endl;

  return result;
} 

int main() {
  size_t n;
  std::cin >> n;
  vector<int> x(n), y(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> x[i] >> y[i];
  }
  std::cout << std::setprecision(10) << minimum_distance(x, y) << std::endl;
}

#include <iostream>
#include <vector>

using namespace std;

int negative_cycle(vector<vector<int>> &adj, vector<vector<int>> &cost) {
	vector<int> dist(adj.size(), 10000);
	dist[0] = 0;
	for(int i = 0; i < adj.size() - 1; ++i) { //Repeat V - 1 loop
		for(int j = 0; j < adj.size(); ++j) {
			for(int k = 0; k < adj[j].size(); ++k) {
				if(dist[adj[j][k]] > dist[j] + cost[j][k]) {
					dist[adj[j][k]] = dist[j] + cost[j][k];
				}
			}
		}
	}
	//1 more iteration to check for negative weight cycle
	int flag = 0;
	for(int j = 0; j < adj.size(); ++j) {
		for(int k = 0; k < adj[j].size(); ++k) {
			if(dist[adj[j][k]] > dist[j] + cost[j][k]) {
				dist[adj[j][k]] = dist[j] + cost[j][k];
				flag = 1;
			}
		}
	}
	return flag;
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
	std::cout << negative_cycle(adj, cost) << "\n";
}

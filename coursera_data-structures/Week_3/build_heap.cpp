#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::swap;
using std::pair;
using std::make_pair;

class HeapBuilder {
 private:
  vector<int> data_;
  vector< pair<int, int> > swaps_;

  void WriteResponse() const {
    cout << swaps_.size() << "\n";
    for (int i = 0; i < swaps_.size(); ++i) {
      cout << swaps_[i].first << " " << swaps_[i].second << "\n";
    }
  }

  int ReadData() {
    int n;
    cin >> n;
    data_.resize(n);
    for(int i = 0; i < n; ++i)
      cin >> data_[i];

    return n;
  }

  void heapify(int n, int i) {
    int smallest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    // If left child of node is 
    if (left < n && data_[left] < data_[smallest])
      smallest = left;
    if (right < n && data_[right] < data_[smallest])
      smallest = right;

    // If smallest is not root
    if (smallest != i) {
      swaps_.emplace_back(make_pair(i, smallest));
      swap(data_[i], data_[smallest]);
      // Recursively call heapify
      heapify(n, smallest);
    }

  }

  void GenerateSwaps(int n) {
    swaps_.clear();
    int startIdx = (n/2) - 1;
    for (int i = startIdx; i >= 0; i--) {
      heapify(n, i);
    }
  }

 public:
  void Solve() {
    int size = ReadData();
    GenerateSwaps(size);
    WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  HeapBuilder heap_builder;
  heap_builder.Solve();
  return 0;
}

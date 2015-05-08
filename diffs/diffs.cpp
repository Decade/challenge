// Idea: There are N number of numbers and a D distance.
//       Find how many of these numbers are D apart from each other.
//       This solution is assuming none of the numbers repeat.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int N, D;
    cin >> N >> D;
    int diffs = 0;
    vector<int> nums;
    for(int i = 0; i < N; ++i){
        int num;
        cin >> num;
        nums.push_back(num);
    }
    sort(nums.begin(),nums.end());
    for(auto num: nums){
        if (binary_search(nums.begin(),nums.end(),num+D))
            ++diffs;
    }
    cout << diffs;
    return 0;
}

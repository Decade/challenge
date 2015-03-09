#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
int main(){
  for(;;){
    int n;
    std::cout << "Enter a number of stuff ";
    std::cin >> n;
    if (n < 1) break;
    auto numbers = std::vector<int>(n);
    for_each(numbers.begin(), numbers.end(),[](int& i){
	std::cout << "Next number ";
	std::cin >> i;
      });
    std::sort(numbers.begin(),numbers.end());
    auto minmax = std::minmax_element(numbers.begin(),numbers.end());
    auto avg = std::accumulate(numbers.begin(), numbers.end(), 0) / (double)numbers.size();
    std::cout << "Min " << *minmax.first << " Max " << *minmax.second 
	      << " Avg " << avg
	      << " Range " << *minmax.second - *minmax.first << std::endl
              << "RMS " << pow(std::accumulate(numbers.begin(), numbers.end(), 0.0,
					       [](double i, double j) { return i + j * j;})/numbers.size(), 0.5) 
	      << " Stdev " << pow(std::accumulate(numbers.begin(), numbers.end(), 0.0,
						  [&](double i, double j){ return i + pow(j - avg, 2);})/numbers.size(),0.5)<< std::endl;
  }
  std::cout << "Bye." << std::endl;
  return 0;
}

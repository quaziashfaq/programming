#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> find_sum_of_combination_of_weights(int number_of_stones, vector<int> stones_weight)
{
  /*
  cout << "In find_sum_of_combination_of_weights function" << endl;
  cout << number_of_stones << endl;
  for (vector<int>::iterator it = stones_weight.begin(); it != stones_weight.end(); ++it){
    cout << *it << ' ';
  }
  cout << endl;

  cout << "Testing: " << (1<<0) << endl;
  */

  vector<int> weights;
  weights.push_back(0);
  for (int i = 0; i < number_of_stones; ++i){
    int next_sum_position_gap = 1 << i;
    for (int j = 0; j < next_sum_position_gap; ++j){
      weights.push_back(weights[j] + stones_weight[i]);
    }
  }

  return weights;
}


int find_min_weight_difference_of_2_piles(vector<int> stones_weight, vector<int> all_possible_stone_piles_weight_sum)
{
  int total_weight = 0;
  for (unsigned int i = 0; i < stones_weight.size(); ++i)
    total_weight += stones_weight[i];

  int minimum_weight_difference = total_weight;
  int diff;

  for (unsigned int i = 0; i < all_possible_stone_piles_weight_sum.size(); ++i){
    diff = total_weight - 2 * all_possible_stone_piles_weight_sum[i];
    diff = abs(diff);
    if (diff < minimum_weight_difference)
      minimum_weight_difference = diff;
  }

  return minimum_weight_difference;
}


int main()
{
  // Testing start
  // int v = 20 * 100000;
  // cout << v << endl;
  // Testing end

  int number;
  cin >> number;
  //cout << number << endl;

  int stone_weight;

  vector<int> stones;
  for (int i = 0; i < number; ++i){
    cin >> stone_weight;
    stones.push_back(stone_weight);
  }

  /*
  for (int i = 0; i < number; ++i)
    cout << stones[i] << ' ';
  cout << endl;
  */

  vector<int> weights = find_sum_of_combination_of_weights(number, stones);
  /*
  for (vector<int>::iterator it = weights.begin(); it != weights.end(); ++it){
    cout << *it << ' ';
  }
  cout << endl;
  cout << "Minimum Difference: ";
  */

  int diff = find_min_weight_difference_of_2_piles(stones, weights);
  cout << diff << endl;
  return 0;
}

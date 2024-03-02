#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int binary_search(vector<long int> a, long int key, int start, int end)
{
  int mid;
  if (start > end)
    return -1;

  while (start <= end){
    mid = (start + end) / 2;
    if (a[mid] == key)
      return mid;
    else if (key < a[mid])
      end = mid - 1;
    else if (key > a[mid])
      start = mid + 1;
    else
      return -1;
  }
  return -1;
}



vector<long> generate_array(int n)
{
  vector<long> a (n, 0);
  a[0] = 1;
  int i = 1;

  /*
    '''
    Here the sequence is 1, 10, 100, 1000, 10000, 100000, ...
    The length of each number is as follows: 1, 2, 3, 4, 5, 6, ...
    So the position of each 1 is as follows: 1, 2, 4, 7, 11, 16, 22
    Therefore we are adding the length of each number to the previous 1's positional value.
    a[0] = 1 --> this is the 1st one
    a[1] = a[0] + 1 = 2
    a[2] = a[1] + 2 = 4
    a[3] = a[2] + 3 = 7
    a[4] = a[3] + 4 = 11
    '''
  */

  while (i < n){
    a[i] = a[i-1] + i;
    i++;
  }
  return a;
}

bool is_value_in_array(vector<long> a, int array_len, long value)
{
  if (binary_search(a, value, 0, array_len-1) == -1)
    return false;
  else
    return true;
}

int main()
{
  string output_string;
  int array_len = 65536;
  vector<long> a = generate_array(array_len);
  bool hasit;
  //long k;
  /*
    int n;
  cin >> n;
  for (int i = 0; i < n; i++){
    cin >> k;
    hasit = is_value_in_array(a, array_len, k);
    if (hasit == true)
      output_string.append("1 ");
    else
      output_string.append("0 ");
  }
  cout << output_string << endl;
  */
  long i, n;
  n = long(pow(2, 31));
  cout << n << endl;

  for (i = 0; i<n; i++){
    hasit = is_value_in_array(a, array_len, i);
    if (hasit == true)
      cout << 1 << " ";
    else
      cout << 0 << " ";
  }
  return 0;
}

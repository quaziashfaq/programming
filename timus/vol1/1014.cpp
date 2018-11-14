#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

vector<int> divide_by_d(int n, int d)
{
  int count = 0;
  int r = n % d;
  while (r == 0 && n > 1){
    count++;
    n /= d;
    r = n % d;
  }
  vector<int> rvalue {n, count};
  return rvalue;
}


int calculate(int n)
{
  if (n == 0)
    cout << 10 << endl;
  else if (n>=1 && n<=9)
    cout << n << endl;
  else{
    vector<int> count_of_divisions (10, 0);
    int nn = n;
    for(int i=9; i>=2; --i){
      vector<int> value = divide_by_d(nn, i);
      nn = value[0];
      count_of_divisions[i] = value[1];
    }

    if (nn == 1){
      for(int i=2; i<10; i++)
        for(int j=0; j<count_of_divisions[i]; j++)
          cout << i;
      cout << endl;
    }
    else {
      cout << -1 << endl;
    }
  }
  return 0;
}

int main()
{
  int n;
  cin >> n;
  calculate(n);
  return 0;
}

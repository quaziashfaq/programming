#include<iostream>
using namespace std;

int a = 1982;
int **z;
int **y;
int ***x;
int ****v;
int ****w;

int **fun1(int *);
int ****fun2(int ***);

int main()
{
    z = fun1(&a);
    cout << z << " "  << **z << '\n';
//     cout << **y << '\n';
    return 0;
}

int **fun1(int *m)
{
    y = &m;
    v = fun2(&y);
    return **v;
}

int ****fun2(int ***n)
{
    w = &n;
    return w;
}

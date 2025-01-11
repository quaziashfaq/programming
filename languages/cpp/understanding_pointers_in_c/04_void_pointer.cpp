#include<iostream>
using namespace std;

int main()
{
    int a = 10;
    void *p1;
    p1 = &a;
    cout << p1 << '\n';
    cout << *(int*)p1 << '\n';


    int *b = NULL;
    cout << "NULL Pointer : " << b << '\n';

    int c = 1000;
    long int diff = &c - &a;
    cout << diff << '\n';

    &a = 10000;
    return 0;
}

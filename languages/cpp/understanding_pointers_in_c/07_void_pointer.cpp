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

    return 0;
}

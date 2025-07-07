#include<iostream>
using namespace std;

void change_value2(int *b);
void change_value1(int *a);

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

//     &a = 10000;

    change_value1(&a);
    cout << a << '\n';
    return 0;
}

void change_value1(int *a)
{
    change_value2(a);
}

void change_value2(int *b)
{
    (*b)++;
}

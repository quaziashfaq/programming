#include<iostream>
using namespace std;

int main()
{
    cout << "NULL : " << NULL << "\n";

//     It will generate an error since NULL is used in arithmetic operation.
//     cout << "10 + NULL : " << 10 + NULL << "\n"; 

    cout << "10 + NULL : " << 10 + int(NULL) << "\n";
    cout << "size of NULL : " << sizeof(NULL) << "\n";
    cout << "size of int: " << sizeof(10) << "\n";
    cout << "size of a string : " << sizeof("a") << "\n";
    cout << "size of an empty string : " << sizeof("") << "\n";

    return 0;

}


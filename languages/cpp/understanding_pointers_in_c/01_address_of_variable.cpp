#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// This function take 3 numbers as input and then print them.
int main() {
    int i = 3;
    int *j;
    j = &i;
    int **k;
    k = &j;
    int ***l;
    l = &k;

    cout << "Value of i: " << i << "\n";
    cout << "Address of i: " << &i << "\n";
    cout << "(points-to (address-of i)) : " << *(&i) << "\n";
    cout << "-----\n";

    cout << "(address-of j): " << &j << "\n";
    cout << "(value of j) : " << j << "\n";
    cout << "(points-to (value-of j)) : " << *j << "\n";
    cout << "-----\n";

    cout << "(address-of k): " << &k << "\n";
    cout << "(value of k) : " << k << "\n";
    cout << "(points-to (value-of k)) : " << *k << "\n";
    cout << "(points-to (points-to (value-of k))) : " << **k << "\n";
    cout << "-----\n";

    cout << "(address-of k): " << &k << "\n";
    cout << "(address-of j): " << &j << " " << k << "\n";
    cout << "(address-of i): " << &i << " " << j << " " << *k << "\n";
    cout << "(value-of i)  : " << i << " " << *(&i) << " " << *j << " " << **(&j) << " " << **k << " " << ***(&k) << "\n"; 
    cout << ***l << " " << ****(&l) << "\n";
    return 0;
}

//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



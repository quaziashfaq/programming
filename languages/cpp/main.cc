#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// This function take 3 numbers as input and then print them.


void do_nothing(int &) {}

int main() {
    cout << "Hello Ash" << endl;

//     int apple {};
//     [[maybe_unused]] int orange {200};
// //     apple {10};
//     cout << "Enter apple count: ";
//     cin >> apple;
//     cout << "Enter orange count: ";
//     cin >> orange;
//     cout << "Apple count: " << apple << '\n';
//     cout << "Orange count: " << orange << '\n';
    int a, b{}, c{};
    do_nothing(a);
    cout << "Default value: " << a << ", " << b << ", and " << c << ".\n";
    //cout << "Enter three numbers: ";
    //cin >> a >> b >> c;
    //cout << "You entered: " << a << ", " << b << ", and " << c << ".\n";

    return 0;
}
//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



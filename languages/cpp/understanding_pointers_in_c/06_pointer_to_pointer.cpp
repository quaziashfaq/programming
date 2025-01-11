#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// Pointer to an array
//
int main() 
{

    int *arrayp[3];
    int a = 10;
    int b = 100;
    int c = 1000;

    arrayp[0] = &a;
    arrayp[1] = &b;
    arrayp[2] = &c;

    int i;
    for (i=0; i<3; i++){
        cout << arrayp[i] << " " << *arrayp[i] << "\n";
    }
    cout << "\n";

    return 0;
}

//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



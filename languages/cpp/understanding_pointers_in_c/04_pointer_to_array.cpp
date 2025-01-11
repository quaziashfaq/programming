#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// Pointer to an array
//
int main() {

    int a[5][2] = {
        {1, 2},
        {3, 4},
        {5, 6},
        {7, 8},
        {9, 10}
    };

//     int **b = a;

    int i, j;
    for (i=0; i<5; i++){
        cout << a[i] << " ";
    }
    cout << "\n";

    for (i=0; i<5; i++){
        cout << "\n";
        for(j=0; j<2; j++)
            cout << *( *(a+i) + j) << " ";
    }
    cout << "\n";
    return 0;
}

//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



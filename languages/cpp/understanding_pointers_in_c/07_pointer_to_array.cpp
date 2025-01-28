#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// Pointer to an array
//
void display(int *b, int array_size)
{
    cout << b << " : ";
    for(int i=0; i<array_size; i++){
        cout << *(b+i) << " ";
    }
    cout << '\n';
    cout << b << " : ";
    for(int i=0; i<array_size; i++){
        cout << *(b++) << " ";
    }
    cout << '\n';
}

void print(int ra[][2], int row, int col)
{
    int i, j;
    for (i=0; i<row; i++){
        cout << ra[i] << " : ";
        for(j=0; j<col; j++)
            cout << ra[i][j] << " ";
        cout << "\n";
    }
}

int main() {

    int a[5][2] = {
        {1, 2},
        {3, 4},
        {5, 6},
        {7, 8},
        {9, 10}
    };

    display(&a[0][0], 10);

    int *b = &a[0][0];

    cout << "\n--- x --- x ---\n";
    int i, j;
//     for (i=0; i<5; i++){
//         cout << a[i] << " ";
//     }
//     cout << "\n";
// 
    for (i=0; i<5; i++){
        cout << a[i] << " : ";
        for(j=0; j<2; j++)
            cout << *( *(a+i) + j) << " ";
        cout << "\n";
    }
    cout << "\n--- x --- x ---\n";
    for (i=0; i<5; i++){
        cout << a[i] << " : ";
        for(j=0; j<2; j++)
            cout << *(b + i*2+j) << " ";
        cout << "\n";
    }



    cout << "\n--- x --- x ---\n";
    int c[3] = {8, 27, 64};
    cout << c << " : \n";
    display(c, 3);


    int *pa;
    pa = (int *)a;
    cout << "\n--- x --- x ---\n";
    for (i=0; i<5; i++){
        cout << (pa + i*2) << " : ";
        for(j=0; j<2; j++)
            cout << *(pa + i*2+j) << " ";
        cout << "\n";
    }
    cout << "\n--- x --- x ---\n";
    display((int *)a, 5*2);
//     display(a, 5*2);

    cout << "\n";

    int (*qa)[2];
    qa = a;
//     int *qaa;
    for (i=0; i<5; i++){
        cout << qa[i] << " : ";
//         qaa = (int *)(qa+i);
        for(j=0; j<2; j++)
//             cout << *(qaa+j) << " "; // this also works
            cout << qa[i][j] << " ";
        cout << "\n";
    }

    cout << "heheheh\n--- x --- x ---\n";
    print(a, 5, 2);

    return 0;
}



//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



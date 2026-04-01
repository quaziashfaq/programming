#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// Pointer to an array
//

void print_bar(int c=60){
    for(int i = 0; i<c; i++) { cout << '-'; }
    cout << '\n';
}

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

//     display(&a[0][0], 10);
//     print_bar();

    


    int i, j;
    for (i=0; i<5; i++){
        // printing address
        cout << a[i] << " : ";
        for(j=0; j<2; j++)
            // printing the value without [] notaiton
            cout << *( *(a+i) + j) << " "; 
        cout << "\n";
    }
    print_bar();



    int *b;
    b = &a[0][0];
//     b = (int *)a;  // it's same as above declaration
    for (i=0; i<5; i++){
        cout << a[i] << " : ";
        for(j=0; j<2; j++)
            // the below address calucaltion is working because
            // array adresses are contiguous in the memory.
            cout << *(b + i*2+j) << " ";
        cout << "\n";
    }



//  The below declaration means it's a single pointer that 
//  points to an entire array of 2 integers.
//  Memory Layout: A single pointer variable. When you increment it (qa + 1),
//  it jumps by the size of the entire array (2 ints), not just one int.
    int (*qa)[2];
    cout << "qa is defined as 'int (*qa)[2]'" << "\n";
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

    print_bar();
//     print(a, 5, 2);

//  This 'pa' is an array of 2 integer pointers.
    int* pa[2];
    int a1 = 100;
    int b1[2] = {1000, 2000};
    pa[0] = &a1; // holding the address value of one integer.
    pa[1] = b1;  // holding the address value of an array.
    cout << *(pa[0]) << endl;
    cout << pa[1][0] << endl; 
    cout << pa[1][1] << endl; 

//     int* (*ra)[2];
//     (*ra)[0] = &a1;
//     (*ra)[1] = b1;

    return 0;
}


//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// Passing the pointer and pointer-to-pointer to function
//
// int swap (int *a, int *b);
// int *return_int_pointer(int *k);
void display(int *n);
void show(int **n);

int main() {
    int a[] = {10, 100, 1000};
    for (int i = 0; i < 3; i++){
        //cout << "a[" << i << "]: " << a[i] << "\n";
        cout << &a[i] << " : ";
        display(&a[i]);
    }
    cout << sizeof (NULL) << endl;
    cout << sizeof ("") << endl;
    cout << sizeof ("ash") << endl;
    return 0;
}

void display(int *n)
{
    show(&n);
}

void show(int **n)
{
    cout << (**n) << "\n";
}



// int swap(int *a, int *b)
// {
//    int t;
//    t = *a;
//    *a = *b;
//    *b = t;
// 
//    return 0;
// }
// 
// 
// int *return_int_pointer(int *a)
// {
//     *a = 300;
//     return a;
// }

//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



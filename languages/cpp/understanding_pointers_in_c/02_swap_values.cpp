#include <iostream>
using namespace std;
//int main(int argc, char * argv[]) {

// This function take 3 numbers as input and then print them.

int swap (int *a, int *b);
int *return_int_pointer(int *k);
int *return_local_int_pointer();
void fun(int **);

int main() {
    int i = 3, j = 30;
    cout << "i: " << i << "\n";
    cout << "j: " << j << "\n";

    swap(&i, &j);
    cout << "i: " << i << "\n";
    cout << "j: " << j << "\n";

    int *k;
    k = return_int_pointer(&i);
    cout << &i << "\n"; 
    cout << k << "\n"; 
    cout << "i: " << i << "\n";
    cout << "*k: " << *k << "\n";

    k = return_local_int_pointer();

//     cout << "Returing a pointer-to-local-variable from another function: " << return_local_int_pointer << "\n";
    cout << "Returing a pointer-to-local-variable from another function: " << k << " : " << *k << "\n";
     
    cout << "-- x -- x --\n";
    int *a;
    fun(&a);
    cout << "*a : " << *a << "\n";

    return 0;

}

void fun(int **b)
{
    static int t = 1982;
    *b = &t;
}

int swap(int *a, int *b)
{
   int t;
   t = *a;
   *a = *b;
   *b = t;

   return 0;
}


int *return_int_pointer(int *a)
{
    *a = 300;
    return a;
}

int *return_local_int_pointer()
{
    static int a = 1982;
    return &a;
}

//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



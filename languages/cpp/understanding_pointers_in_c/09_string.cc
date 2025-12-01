#include <iostream>
#include <cstdlib>
using namespace std;

// String Operations

void print_string(const char *s);
unsigned long int xstrlen(const char *str);
void xstrcpy(char *dst, const char *src);
char *get_string_copy(const char *src);
void simple_string_array_manipulation();
void memory_allocation_for_string();
void array_of_string_pointers();
void array_of_pointers_to_string_pointers();

//xstrchr
//xstrstr
//xstrcmp

int main() {
//     simple_string_array_manipulation();
//     memory_allocation_for_string();
//     array_of_string_pointers();
    array_of_pointers_to_string_pointers();
    return 0;
}


void array_of_pointers_to_string_pointers() {
    const char* names[] = { "imran", "shoma", "aynan" };
    const char** names_ptr[] = {names, names+1, names+2};

    cout << "All the names from the names array" << '\n';
    for(int i=0; i<3; i++)
        print_string(names[i]);

    cout << '\n';
    cout << "Addresses of the 1st character in names[i]" << '\n';
    for(int i=0; i<3; i++)
        printf("%p\n", (void *)&names[i][0]);

    cout << '\n';
    cout << "All the (pointer) values in names[i]" << '\n';
    for(int i=0; i<3; i++)
        printf("%p\n", (void *)names[i]);

    cout << '\n';
    cout << "Addresses of names[i]" << '\n';
    for(int i=0; i<3; i++)
        printf("%p\n", (void *)&names[i]);

    cout << '\n';
    cout << "All the values in names_ptr[i]" << '\n';
    for(int i=0; i<3; i++)
        cout << names_ptr[i] << '\n';

    cout << '\n';
    for(int i=0; i<3; i++)
        cout << *names_ptr[i] << '\n';


    cout << '\n';
    cout << "Addresses of names_ptr[i]" << '\n';
    for(int i=0; i<3; i++)
        printf("%p\n", (void *)&names_ptr[i]);

    cout << '\n';
    const char*** p = names_ptr;
    cout << &p << '\n';
    cout << p << '\n';
    cout << p[2][0] << '\n';
    cout << p[2][-1] << '\n';
    cout << p[2][-2] << '\n';
}

void array_of_string_pointers() {
    char names[2][10] = { "imran", "shoma" };

    /* 
     * both declarations are okay.
     * char *names2[2] = {names[0], names[1]};
     * char *names2[] = {names[0], names[1]};
    */

    char *names2[] = {names[0], names[1]};
    cout << names2[0] << '\n';

    /*
     * Here pointing to string literals with mere 'char * names[]' are throwing errors.
     * So below 2 declarations are wrong:
     * char *names3[] = { "imran", "shoma" };
     * char *names3[2] = { "imran", "shoma" };
     *
     * Therefore, you have to add 'const' to notify that 
     * array of char pointers are pointing to string literals.
     * const char *names3[] = { "imran", "shoma" };
     * const char *names3[2] = { "imran", "shoma" };
     */

    const char *names3[] = { "imran", "shoma" };
    cout << names3[0] << '\n';
    names3[0] = "aynan";
    cout << names3[0] << '\n';
    cout << "Sizeof of names3: " << sizeof(names3) << '\n';

    for(int i=0; i<2; i++){
        cout << names3[i] << "\tlength: " << strlen(names3[i]) << '\n';
    }
}


void simple_string_array_manipulation() {
    char a[] = "Aynan and her father are 'Dushto'";
    cout << 1 + a << ' ' << strlen(a) << '\n';
//     print_string(a); 
    cout << "String length: " << xstrlen(a) << '\n';
}

void memory_allocation_for_string() {
    char a[] = "Aynan and her father are 'Dushto'";
    char *b = get_string_copy(a);
    a[0] = 'T';
//     print_string(b); 
//     print_string(a); 
    char *c = (char *) malloc ((xstrlen(a) + 1) * sizeof(char));
    xstrcpy(c, a);
    print_string(c);

    free(b);
    free(c);
}



void print_string(const char *s) {
//  Both ways of checking if pointer points to '\0' is okay.
//     while (*s) {
    while (*s != '\0') {
        cout << *s << ' ';
        s++;
    }
    cout << '\n';
}

unsigned long int xstrlen(const char *str) {
    unsigned long int count = 0;
    while (*str) { count++; str++; }
    return count;
}

char *get_string_copy(const char *src) {
    unsigned long int srclen = xstrlen(src);
    char *dst = (char *)malloc( (srclen+1) * sizeof(char));
    // dsti is the index of dst. I will move it forward to copy from the source.
    char *dsti = dst;
    while (*src) { *dsti = *src; src++; dsti++; }
    *dsti = '\0';
    return dst;
}

void xstrcpy(char *dst, const char *src) {
    while (*src) {
        *dst = *src;
        dst++;
        src++;
    }
    *dst = '\0';
}
//-Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion -Werror -ggdb -O0 
//



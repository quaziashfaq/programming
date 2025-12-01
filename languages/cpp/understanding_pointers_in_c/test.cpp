#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    cout << "test" << '\n';
    const char *names[] = {"ash", "imu", "tumo"};
    names[1] = "imran";
    cout << names[1] << '\n';
    return 0;
}

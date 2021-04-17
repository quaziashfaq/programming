#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("I will write once since I come beore fork(). My ID is %d.\n", getpid());
    fork();
    printf("My ID is %d. And my parent's ID is %d.\n", getpid(), getppid());

    return 0;
}

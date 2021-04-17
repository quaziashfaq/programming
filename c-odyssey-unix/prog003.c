#include <stdio.h>
#include <unistd.h>

int main()
{
    int pid;
    pid = getpid();
    printf("Process ID is %d\n", pid);
    return 0;
}

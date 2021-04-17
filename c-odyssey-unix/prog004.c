#include <stdio.h>
#include <unistd.h>

int main()
{
    int pid;
    pid = getpid();
    printf("Process ID is %d\n", pid);

    long int i;
    for (i=0; i<400000000; i++);
    return 0;
}

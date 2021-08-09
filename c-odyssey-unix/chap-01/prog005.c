#include <stdio.h>
#include <unistd.h>

int main()
{
    int pid;
    pid = getpid();
    printf("Process ID is %d\n", pid);

    int ppid;
    ppid = getppid();
    printf("Process ID is %d\n", ppid);

    return 0;
}

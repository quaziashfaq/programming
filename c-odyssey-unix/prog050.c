#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    printf("beore exec my pid is %d\n", getpid());
    printf("beore exec my parent pid is %d\n", getppid());

    printf("exec starts\n");
    execl("./ex2", "tototo", (char *) 0);
    printf("This is not going to print");

    return 0;
}

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/* Check the limit of forking processes */
int main()
{
    int i = 10;
    int pid;

    pid = fork();
    if (pid == 0) { //child process
        printf("child starts. i: %d\n", i);
        i += 100;
        printf("before child ends. i: %d\n", i);
    }
    else{
        wait(0);
        printf("In parent, i: %d\n", i);
    }
    return 0;
}

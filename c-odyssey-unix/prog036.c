#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/* Trying to access the same variable in parent process
 * from child process using the pointer. */
/* Even the global variable and it's pointer is dupliacted
 * when the process is forked. */

int i = 10;
int *j = &i;

int main()
{
    int pid;

    pid = fork();
    if (pid == 0) { //child process
        printf("child starts. i: %d\n", *j);
        *j += 100;
        printf("before child ends. i: %d\n", *j);
    }
    else{
        wait(0);
        printf("In parent, i: %d\n", *j);
    }
    return 0;
}

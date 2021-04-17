#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/* Trying to access the same variable in parent process
 * from child process using the pointer.
 * Even global variables are duplicated when proces is forked. */

int i = 10;
int main()
{
//    int *j = &i;
    int pid;

    pid = fork();
    if (pid == 0) { //child process
        printf("child starts. i: %d\n", i);
        //*j += 100;
        i += 100;
        printf("before child ends. i: %d\n", i);
    }
    else{
        wait(0);
        printf("In parent, i: %d\n", i);
    }
    return 0;
}

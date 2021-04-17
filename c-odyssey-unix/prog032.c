#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/* Check the limit of forking processes */
int main()
{
    int i = 1;
    int pid;

    for (;;)
    {
        pid = fork();

        if (pid < 0)
            printf("Maximum number of concurrent processes are %d\n", i);

        if (pid == 0) { //child process
            i++;
            printf("Child starts. ID: %d. Count: %d\n", getpid(), i);
            if (i == 1000)
                exit(0);
        }
        else{
            printf("Child ended. ID: %d. Counting: %d\n", wait(0), i);
            exit(0);
        }
    }
    return 0;
}

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int status;

    if (fork() > 0){
        printf("From parent :: parent PID: %d\n", getpid());
        sleep(10);
        int cpid = wait(&status);
        printf("From parent:: my child pid %d ended.\n", cpid);
        if ((status & 0xff) == 0)
        {
            // programe termintated okay.
            printf("program terminated okay!");
        }
        else if ((status & 0xff) != 0) {
            printf("program terminated abnormally!");
        }

    }
    else {
        printf("From child:: child pid: %d\n", getpid());
        printf("From child:: parent pid: %d\n", getppid());
        printf("%d\n", 10/0);
    }
    return 0;
}

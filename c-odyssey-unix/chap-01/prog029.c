#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main()
{
    int i, pid, status, exitstat, childpid;
    pid = fork();

    if (pid == 0) { //child
        printf("Child starts. ID: %d\n", getpid());
        sleep(15);
        exit(3);
    }
    else { //parent
        printf("Parent starts\n");
        childpid = wait(&status);
        printf("child process with pid %d died.\n", childpid);

        if ((status & 0xff) != 0){
            printf("Exit status from process id %d was %x\n", pid, status);
            printf("Signal interrupted\n");
        }
        else{
            printf("Normal termination\n");
            exitstat = status >> 8;
            //exitstat = (int) status / 256;
            printf("Exit status from %d was %x\n", pid, exitstat);
            //printf("Exit status from %d was %x\n", pid, (int)status);
        }
    }
    return 0;
}

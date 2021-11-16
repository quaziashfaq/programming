#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int i=0, j=0, pid;
    int v;
    pid = fork();
    if (pid == 0){ //child
        printf("Child starts. ID: %d\n", getpid());
        sleep(5);
        printf("Child ends\n");

    }
    else{ //parent
        printf("Parent starts\n");
        //v = wait(0);
        sleep(10);
        printf("child process with pid %d died.\n", wait(0));
        sleep(10);

        printf("Parent ends\n");
    }
    return 0;
}

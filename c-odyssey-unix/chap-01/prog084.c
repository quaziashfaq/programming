#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* Print environment variables */



int main(int argc, char *argv[])
{

    int pid;
    pid = fork();

    if (pid == 0){
        execl("/bin/ls", "ls", "-l", (char *)0);
        printf("Exec did not work properly.\n");
    }
    else{
        wait(0);
        printf("Parent: child eneded\n");
    }
    return 0;
}

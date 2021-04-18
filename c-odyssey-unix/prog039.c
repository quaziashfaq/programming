#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>

/*
 * Sharing the same file descriptor between child and parent process. */

int main()
{
    int fp;
    int pid;
    char buff[11];
    fp = open("atestfile.txt", O_RDONLY, 0666);
o   pid = fork();

    if (pid == 0)  //child process goes first
    {
        printf("Child starts %d\n", getpid());
        printf("%d\n", fp);
        read(fp, buff, 10);
        buff[10] = '\0';
        puts(buff);
        printf("Child is exiting\n");
    }
    else{
        wait(0);
        read(fp, buff, 10);
        buff[10] = '\0';
        puts(buff);
        close(fp);
    }
    return 0;
}

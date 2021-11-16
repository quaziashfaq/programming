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


    printf("%d\n", SEEK_SET);
    printf("%d\n", SEEK_CUR);
    printf("%d\n", SEEK_END);


    fp = open("atestfile.txt", O_RDONLY, 0666);
    pid = fork();


    if (pid == 0)  //child process goes first
    {
        printf("Child starts %d\n", getpid());
        printf("File handle in child process is %ld\n", lseek(fp, 0l, SEEK_CUR));

        read(fp, buff, 10);
        buff[10] = '\0';
        puts(buff);

        printf("File handle in child process is %ld\n", lseek(fp, 0l, SEEK_CUR));
        printf("Child is exiting\n");
    }
    else{
        wait(0);
        printf("File handle in parent process is %ld\n", lseek(fp, 0l, SEEK_CUR));
        close(fp);
    }

    return 0;
}

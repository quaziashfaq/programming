#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>

/*
 * Sharing the same file descriptor between child and parent process.
 *
 * Though the book suggested that child will read 1024 characters.
 * But the testing shows that it only read 10 characters.
 * Then parent reads another 10 characters.
 *
 * In fread function, it will be sizeof(buff)-1
 *
 * */


int main()
{
    FILE *fp;
    int pid;
    char buff[11];

    fp = fopen("atestfile.txt", "r");
    fread(buff, sizeof(buff)-1, 1, fp);
    puts(buff);
    printf("%ld %ld\n", ftell(fp), lseek(fp->_fileno, 0, SEEK_CUR));
    fclose(fp);

/*
    if (pid == 0)  //child process goes first
    {
        printf("\nChild starts %d\n", getpid());
        printf("In child: file pointer is %ld\n", ftell(fp));

        fread(buff, sizeof(buff) - 1, 1, fp);
        buff[10] = '\0';
        printf("child reads: %s\n", buff);
        printf("In child: file pointer is %ld\n", ftell(fp));

        sleep(5);

        printf("After parent is closed In child: file pointer is %ld\n", ftell(fp));

        fread(buff, sizeof(buff) - 1, 1, fp);
        buff[10] = '\0';
        printf("child reads: %s\n", buff);
        printf("In child: file pointer is %ld\n", ftell(fp));

        printf("Child is exiting...\n\n");
    }
    else{
        // no wait for child to complete
        //
        printf("In Parent file pointer is %ld\n", ftell(fp));
        printf("%ld\n", fread(buff, sizeof(buff) - 1 , 1, fp));
        buff[10] = '\0';
        printf("parent  reads %s\n", buff);

        printf("After reading some chars parent file pointer is %ld\n", ftell(fp));

        printf("parent is closing...\n\n");
    }
*/
    return 0;
}

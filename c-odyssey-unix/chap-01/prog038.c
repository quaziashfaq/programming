#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>

/* Trying to access the same variable in parent process
 * from child process using the pointer. */
/* communicating between chlid and parent through files */

int main()
{
    int fp;
    int pid;
    char chr = 'A';
    pid = fork();

    if (pid == 0) { //child process
        printf("Child starts\n");
        fp = open("atestfile.txt", O_CREAT | O_WRONLY, 0666);
        printf("%d\n", fp);
        printf("In child chr is %c\n", chr);
        chr = 'B';
        write(fp, &chr, 1);
        printf("In child after change chr is %c\n", chr);
        printf("Child is exiting\n");
        close(fp);
    }
    else{
        wait(0);
        printf("in parent before opening the file chr: %c\n", chr);
        fp = open("atestfile.txt", O_RDONLY, 0666);
        read(fp, &chr, 1);
        printf("In parent chr is %c\n", chr);
        close(fp);
    }
    return 0;
}

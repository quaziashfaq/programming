#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    int pid;
    FILE *fp;

    pid = fork();
    fp = fopen ("tamper", "a");

    if (pid == 0) {
        fputc('a', fp);
    }
    else {
        fputc('b', fp);
    }
    fclose(fp);
    return 0;
}

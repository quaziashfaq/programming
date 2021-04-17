#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main()
{
    int pid;
    FILE *fp;

    pid = fork();

    if (pid == 0) {
        fp = fopen ("tamper", "w");
        fputc('a', fp);
    }
    else {
        fputc('b', fp);
    }
    fclose(fp);
    return 0;
}

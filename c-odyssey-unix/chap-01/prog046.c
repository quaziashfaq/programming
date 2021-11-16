#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main()
{
    char *p = "hello world";
    int fp;

    printf("%lu\n", strlen(p));
    fp = open("tamper", O_CREAT | O_WRONLY, 0666);
    write(fp, p, 11);
    fork();
    return 0;
}

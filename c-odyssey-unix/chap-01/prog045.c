#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main()
{
    char *p = "hello world";
    FILE *fp;

    printf("%lu\n", strlen(p));
    fp = fopen("tamper", "w");
    fwrite(p, 11, 1, fp);
    fork();
    return 0;
}

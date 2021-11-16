#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* Print environment variables */

int main(int argc, char *argv[], char *envp[])
{
    int i;
    printf("argv values\n");
    for (i=0; argv[i]; i++)
        printf("%s\n", argv[i]);

    printf("envp values\n");
    for (i=0; envp[i]; i++)
        printf("%s\n", envp[i]);
    return 0;
}

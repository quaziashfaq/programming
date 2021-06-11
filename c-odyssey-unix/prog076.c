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
    extern char **environ;

    printf("Printing environ\n");
    for (i=0; environ[i]; i++)
        printf("%s\n", environ[i]);

    printf("\n");
    printf("Printing envp\n");
    for (i=0; envp[i]; i++)
        printf("%s\n", envp[i]);

    printf("\n");
    for (i=0; i<argc; i++)
        printf("%s\n", argv[i]);
    return 0;
}

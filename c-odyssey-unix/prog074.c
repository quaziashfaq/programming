#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* Print environment variables */

extern char **environ;

int main(int argc, char *argv[])
{
    int i;
    int pid = fork();
    if (pid == 0) {
        printf("In child:\n");
        for (i = 0; environ[i]; i++)
            printf("%s\n", environ[i]);
    }

    else{
        wait(0);
        printf("In parent:\n");
        for (i=0; environ[i]; i++)
            printf("%s\n", environ[i]);
    }
    return 0;
}

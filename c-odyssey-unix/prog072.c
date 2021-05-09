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
    for (i=0; envp[i]; i++)
        printf("%s\n", envp[i]);
    return 0;
}

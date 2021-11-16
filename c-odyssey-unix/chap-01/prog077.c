#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* Print environment variables */

char *env[] = {"Hello", "Masud Rana", (char *)0};


int main(int argc, char *argv[])
{
    extern char **environ;
    environ = env;

    printf("Now exec will start\n");
    execl("./ex2.out", "test", (char *)0 );
    perror("");

    return 0;
}

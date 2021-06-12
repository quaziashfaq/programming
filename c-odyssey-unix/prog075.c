#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* Print environment variables */


int main(int argc, char *argv[])
{
    int i;
    char *env[5], *av[3];

    env[0] = "NAME=STEFF";
    env[1] = "COMPANY=PUMA";
    env[2] = "address=rome";
    env[3] = "tel=011011011011";
    env[4] = (char *) 0;

    av[0] = "Testing argc and argv";
    av[1] = "Testing env also";
    av[2] = (char *) 0;

    printf("Executing ex1.out");
    execve("./ex2.out", av, env);
    perror("execve failed");

    return 0;
}

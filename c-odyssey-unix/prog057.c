#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("The cat jumped over the wall");
    fflush(stdout);
    execl("./ex2.out", "ex2", (char *)0);
}

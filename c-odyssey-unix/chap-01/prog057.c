#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("%s\n", argv[0]);
    printf("The cat jumped over the wall\n");
    fflush(stdout);

    //execl("./ex2", "ex2", "My", "name", "is", "ashfaq", (char *)0);

    char *arguments[6];
    arguments[0] = "ex2";
    arguments[1] = "My";
    arguments[2] = "name";
    arguments[3] = "is";
    arguments[4] = "ashfaq";
    arguments[5] = (char *)0;

    //execv("./ex2", arguments);
    execvp("./ex2", arguments);
    //execvp("ls", arguments);
}

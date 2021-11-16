#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    char *temp[5];
    temp[0] = "hello";
    temp[1] = "How";
    temp[2] = "are";
    temp[3] = "you?";
    temp[5] = (char *)0;


    execvp("./ex2.out", temp);
}

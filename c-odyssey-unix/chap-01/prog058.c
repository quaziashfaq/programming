#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("%s\n", argv[0]);
    printf("The clock went dong\n");
    printf("Arguments:\n");
    for (int i = 0; i < argc; i++)
        printf("%s\n", argv[i]);
}

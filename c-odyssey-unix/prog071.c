#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("Args #: %d\n", argc);
    int i = 0;
    for(i=0; i<argc; i++){
        printf("%s ", argv[i]);
    }
    printf("\n");
    return 0;
}

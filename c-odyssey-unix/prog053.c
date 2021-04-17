#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("after exec my pid is %d\n", getpid());
    printf("after exec my parent pid is %d\n", getppid());

    printf("%s\n", argv[0]);
    printf("exec ends\n");
    return 0;
}

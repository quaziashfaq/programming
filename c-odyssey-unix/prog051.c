#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    printf("after exec my pid is %d\n", getpid());
    printf("after exec my parent pid is %d\n", getppid());
    printf()

    printf("exec ends\n");
    return 0;
}

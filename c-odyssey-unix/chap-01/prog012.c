#include <stdio.h>
#include <unistd.h>

int main()
{
    int pid;
    pid = fork();
    if (pid < 0)
        printf("fork failed\n");
    else {
        printf("Fork is successful\n");
    }
    return 0;
}

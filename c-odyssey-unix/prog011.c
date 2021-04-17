#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("I will write once since I come beore fork(). My ID is %d.\n", getpid());
    int pid;
    pid = fork();
    pid = fork();
    pid = fork();
    if (pid == 0){
        printf("I am the true child. My ID is %d. And my parent's ID is %d.\n", getpid(), getppid());
        sleep (20);
        printf("I am the true child. My ID is %d. And my parent's ID is %d.\n", getpid(), getppid());
    }
    else
        printf("I am a parent. My ID is %d. And my parent's ID is %d.\n", getpid(), getppid());

    return 0;
}

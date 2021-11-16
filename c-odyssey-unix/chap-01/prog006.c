#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("I will write once since I come beore fork(). My ID is %d.\n", getpid());
    fork();
    printf("My ID is %d. And my parent's ID is %d.\n", getpid(), getppid());

    return 0;
}


/*
 * Here is the output of the program.
 * $ gcc prog006.c && ./a.out
 * I will write once since I come beore fork(). My ID is 345859.
 * My ID is 345859. And my parent's ID is 288024. <-- Parent process. PID 288024 is the shell.
 * My ID is 345860. And my parent's ID is 345859. <-- Child process
 *
 * $ ps
    PID TTY          TIME CMD
 288024 pts/5    00:00:01 zsh
*/

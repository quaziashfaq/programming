#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/* Dumping cores.
 * The 7th bit of the lower 8 bits of 'status' is turned on when core is dumped.
 * */

int main()
{
    int i, j = 0;
    int pid = fork();
    int status;

    if (pid == 0) // child process
    {
        i = 10 / j;
    }
    else // parent process
    {
        wait(&status);
        if ((status & 0x80) != 0)
            printf("Our core dumped\n");
    }
    return 0;
}

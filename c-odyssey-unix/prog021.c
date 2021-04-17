#include <stdio.h>
#include <unistd.h>

int main()
{
    int i=0, j=0, pid;
    pid = fork();
    if (pid == 0){ //child
        for(i=0; i<500; i++)
            printf("%d\t", i);
    }
    else{ //parent
        for(j=0; j<500; j++)
            printf("%d..\t", j);
    }
    return 0;
}

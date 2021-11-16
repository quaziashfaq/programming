#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

/* Print environment variables */



int main(int argc, char *argv[], char **envp)
{

    extern char **environ;
    int i;
    int pid;
    char *env[3];
    env[0] = "company=ibm";
    env[1] = "city=nyc";
    env[2] = (char *)0;


    pid = fork();

    if (pid == 0){
        environ = env;
        printf("In child\n");
        for (i=0; environ[i]; i++)
            printf("%s\n", environ[i]);

    }
    else{
        wait(0);
        printf("In parent\n");
        for(i=0; environ[i]; i++)
            printf("%s\n", environ[i]);
    }
    return 0;
}

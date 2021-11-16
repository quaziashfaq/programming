#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <time.h>

/* Print environment variables */



int main(int argc, char *argv[])
{

    int pid;
    long int a, b;
    printf("1st arg: %s\n", argv[0]);

    time(&a);
    pid = fork();

    if (pid == 0){
        //execl("/bin/ls", "ls", "-l", (char *)0);
        /*
        ** argv[0] is ./a.out
        ** argv[1] is ls
        ** argv[2] is -l
        **
        ** The function execvp definition is as follows
        ** int execvp(const char *file, char *const argv[]);
        ** const char *file is the actual `ls` file.
        ** char *const argv[] will need a pointer to character array.
        ** That's why the argument passed is &argv[1].
        ** By convention the 1st value will be the executable process name just for the sake of giving the name.
        ** The 2nd argument will be the actual arguments
        **
         */
        execvp(argv[1], &argv[1]);

        perror("Exec did not work properly.\n");
    }
    else{
        wait(0);
        time(&b);
        printf("Parent: child ended\n");
        printf("Time taken: %ld seconds\n", b-a);

    }
    return 0;
}

#include <stdio.h>
#include <unistd.h>

int main()
{
    if (fork() > 0){
        printf("parent\n");
        sleep(50);
    }
    return 0;
}

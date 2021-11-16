#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main()
{
    int i, j = 0;
    i = 10 / j;
    printf("value of i is %d\n", i);
    return 0;
}

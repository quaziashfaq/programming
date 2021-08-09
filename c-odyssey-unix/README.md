# Chapter 1
Unix is a multitasking OS. It slices the CPU time and allocates time to all the running process. It switches between processes. Processes have unique IDs while running. These are called PID (process IDs). 
When CPU switches the processes, it moves out the running process, it's associated variables, data and code out of CPU cache/registers to RAM/disk and brings in another process to run. Once its time is out, the old/new process is switched back to CPU.

`getpid()` function gives the identification number of a process. 

`ps` command output gives the PID, TTY (terimnal), TIME (how long it's running) and CMD (the process name)

``` shmagpie% gcc prog006.c && ./a.out 
I will write once since I come beore fork(). My ID is 345859.
My ID is 345859. And my parent's ID is 288024.
My ID is 345860. And my parent's ID is 345859.

magpie% ps
    PID TTY          TIME CMD
 288024 pts/5    00:00:01 zsh
 345485 pts/5    00:00:58 a.out
 345506 pts/5    00:00:35 a.out
 345520 pts/5    00:00:00 ps
```

`getppid()` gives the PID of the parent of the running process.

## Old school explanation
When we boot the system, a special process called teh `swapper` or `scheduler` is created with a PID of 0. The `swapper` manages memory allocation for process and influences CPU allocation. The `swapper` in turn creates three children: the `process dispatcher`, `vhand` and `bdflush` with ID numbers 1, 2, 3 respectively.

This is done by executing the file init which exists in the `etc` sub-directory. The `process dispatecher` now gives birth to the shell. From now all process inititated by us are children are children of the `shell` and in turn descendents of the process `dispatcher`. This gives rise to a tree-like structure.

UNIX keeps track of all process in an internal data structure called the `process table`. `ps -el` can give a listing the running process table.


`fork()` creates a new process for the calling point. 
The calling process is called the parent process.
The new process is called the child process.
[prog006.c](prog006.c)




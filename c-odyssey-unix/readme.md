# Unix programming

Unix is a multitasking OS. It slices the CPU time and allocates time to all the running process. It switches between processes. Processes have unique IDs while running. These are called PID (process IDs). 
When CPU switches the processes, it moves out the running process, it's associated variables, data and code out of CPU cache/registers to RAM/disk and brings in another process to run. Once its time is out, the old/new process is switched back to CPU.


## Process Id
Every process has a PID.
`getpid()` To get PID 
`getppid()` To get parent's PID

`ps` command output gives the PID, TTY (terimnal), TIME (how long it's running) and CMD (the process name)

- `ps` output of a running process shows as R.
- `ps` output of a sleeping process shows as S.

## Old school explanation
When we boot the system, a special process called teh `swapper` or `scheduler` is created with a PID of 0. The `swapper` manages memory allocation for process and influences CPU allocation. The `swapper` in turn creates three children: the `process dispatcher`, `vhand` and `bdflush` with ID numbers 1, 2, 3 respectively.

This is done by executing the file init which exists in the `etc` sub-directory. The `process dispatecher` now gives birth to the shell. From now all process inititated by us are children are children of the `shell` and in turn descendents of the process `dispatcher`. This gives rise to a tree-like structure.

UNIX keeps track of all process in an internal data structure called the `process table`. `ps -el` can give a listing the running process table.


## Fork
`unistd.h`
Use `fork()` command to create a child process.
Child process will have the exact copy of the parent process. The child process execution will start right after the invocation of fork command.

- `fork()` return value is PID of the child process in the parent process.
- `fork()` return value is 0 in the child process.
- `fork()` return value is -1 if fork fails.

So child process can know about its parent process by the function `getppid()`.
The parent process can know about iss child process by the function `fork()`.

[prog006.c](./chap-01/prog006.c)
[prog008.c](./chap-01/prog008.c)
[prog006.c](./chap-01/prog006.c)

### Orphan process
If parent closes before the child, the child becomes **orphan**. So OS will assign the **init** process ID (generally 1) to be the parent the orpahned child process.

### Zombie process
If child ends before parent process, then child process waits for parent process to completed. Meanwhile the child becomes a Zombie since it wants to end its life in the world but can't leave because parent is still running!
ps output will show the state of child process as Z (Zombie) or defunct.

### Wait
sys/wait.h
The `wait()` function call in the parent waits for its child to complete. If the child completes, it does the burial in the world meaning it removes the child process from the PROCESS TABLE.

- wait(&status) returns the child's PID if there is a child.
- wait(&status) returns the -1 if there is no child.
- status is a 16 bit integer.

If child ends normally, the high order 8-bit is updated and low order 8-bit is zeroed. 
- status & 0xff00 != 0 --> True
- status & 0xff == 0   --> True

If child ends abnormally, the high order 8-bit is zeroed out and low order 8-bit is updated. 
- status & 0xff00 == 0 --> True
- status & 0xff != 0   --> True


## Fork again (1) - Access to variable
Fork creates a copy of the process and runs the copied process as the child of the 1st process (parent).
The child process gets a duplicate copy of all the variables declared in the parent process. 
- Change of value of the variable in the child process **does not change** the value in the parent process.
- Even pointer to variable also gets duplicated. So changing the variable through pointer in child process **does not change** the value in the parent process.
- Even global variable also gets duplicated.
- The address of a variable is same both in child and parent. It means the values are copied back and forth.


## Sharing info between child and parent process.
- Using files


## File low-level operations

```
file_desriptor = open(<filename>, <open_method>, <permission>)
bytes_written = write(file_desrciptor, pointer_to_array, count)
bytes_read = read(file_descriptor, location_pointer_to_store_read_data, count)

position_of_file_handle = lseek(file_descriptor, offset, from_where or whence)
```
- SEEK_SET 0 or starting location
- SEEK_CUR 1 or current location
- SEEK_END 2 or end location


A file, unlike a variable, is never duplicated. File handle is shared between parent and childe processes.
Each process has access to 2 tables.
- **File Descriptor Table** --> This table holds the file descriptor of the file opened by teh parent process. Since this table is duplicated, all files open in the parent process when the function `fork()` is called, are also open in the child.
- **System File Table** --> This table is used to control files. 
  - In this table are stored the file pointer and access mode. 
  - An entry of the opened file is made into this table. Another entry of the same file is made in the file descriptor table. Both these entryies are linked.
  
While each process has its own file descriptor table, thes system file table is global and not duplicated when a process is creaed. Thus, not only the file, but also the file pointer and its access mode, are shared.

## Buffered File operations
```c
File *fp;
fopen(<filename>, "mode-to-open-the-file")
fread(buffer, data_to_read_in_bytes, number_of_times, file_pointer)
total_bytes_read = number_of_times x data_to_read_in_bytes
total_bytes_raed <= size(buffer) - 1 --> True
location_of_file_pointer_in_the_file = ftell(file_pointer);
fwrite's arguments are same as fread

fputc(int, FILE *stream)
```



A example code with shared file pointer between child and parent.

```c
fp = fread(<filename>, "r");
if (fork() == 0){ //child
  fread(10 characters); // will read
  sleep(10);
  fread(10 characters);
}
else{ // parent
  sleep(5);
  fread(10 characters)
}
```
The fread operations are synchronized by using sleep function. It will go like below
1. Parent is sleeping.
2. Child reads 10 characters. Pointer is at position 10. But it has already read 4096 characters in the buffer.
3. Child goes into sleep.
4. Parent reads. But its pointer is standing at 4096. And it reads next 10 character.
5. Child's file pointer is at 10. And it reads the next 10 character and its file pointer's position is at 20.

If we flush after each read like `fflush(fp)` in child process, then buffer will be flushed. When parent reads, its file pointer will be at 10.

## exec () Function
A process can execute another process using `exect()` function. By this, another process overwrites the parent process totally. However, this new process has --
- Has the same PID as the original process
- Has the same parent process PID
- has the current directory
- has the file descriptor tables - if any are open - also remain the same.

### `execl` function:
```c
execl(process_name, comma_separated_process_arguments, NULL pointer);
execl("/usr/bin/ls", "-l", "-r", "/usr/", (char *)0 );
(char *)0 reppresents a NULL pointer.
```

`process_name` is the name of the process, with relative path info or absolute path, to execute.
`comma_separated_process_arguments`: We check how generally a main function is defined:
`int main(int argc, char *argv[])`: The first argument `argv[0]` is always the name of the file which is executed.
The first argument should be the name of the `comma_separated_process_arguments` should be the name of the file that is going to be executed.
`NULL pointer`: To denote the end of function arguments. `(char *)0`

`execl` is the base. The rest of the functions can be understood in the same manner.

### `execv(file_tobe_executed, argument_array)`:
- `file_tobe_executed` has to have relative path or absolute path info.
- `argument_array` will be passed to the main function of the `file_tobe_executed`. 
- The 1st argument of `argument_array` should be the name of the `file_tobe_executed`.
- Its last argument must be null terminator defined as `(char *)0`.


### `execvp(file_tobe_executed, argument_array)`:
- `file_tobe_executed`: `execvp` does not require absolute path or relative path of the `file_tobe_executed` but rather will look for the process in the default paths. 
`argument_array` will be passed to the main function of the `file_tobe_executed`. 
- The 1st argument of `argument_array` should be the name of the `file_tobe_executed`.
- Its last argument must be null terminator defined as `(char *)0`.



## Environment block
I didn't know that you can also pass the environment variables to the main function.
`main(int argc, char *argv[], char *envp[]);`

`envp[]` is array of pointers and by default it points all the variables that are defined in the environment.
There is another way: `extern **environ;` is a pointer to the array of pointers which have point to the environment variables.

During `fork()` a process, the child process has a copy of the variables defined in the parent porcess. Also, the variables in the environment block of the parent process are also duplicated. But after forking, changing of variable in either process does not affect the other. Because the now processes have duplicate copies of environment variables and they are separate.

We can change the environment variables in the child (spawned) process by passing new environment variables. The function to be used is `execve()` 

### `execve(file_tobe_executed, argument-array, new_environment_array)`

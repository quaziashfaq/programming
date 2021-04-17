# Unix programming

## Process Id
Every process has a PID.
To get PID --> use getpid()
To get parent process id --> getppid()

- ps output of a running process shows as R.
- ps output of a sleeping process shows as S.


## Fork
unistd.h
Use fork() command to create a child process.
Child process will have the exact copy of the parent process. The child process execution will start right after the invocation of fork command.

- fork() return value is PID of the child process in the parent process.
- fork() return value is 0 in the parent process.
- fork() return value is -1 if fork fails.

### Orphan process
If parent closes before the child, the child becomes **orphan**. So OS will assign the **init** process ID (generally 1) to be the parent the orpahned child process.

### Zombie process
If child ends before parent process, then child process waits for parent process to completed. Meanwhile the child becomes a Zombie since it wants to end its life in the world but can't leave because parent is still running!
ps output will show the state of child process as Z (Zombie) or defunct.

### Wait
sys/wait.h
The wait function call in the parent waits for its child to complete. If the child completes, it does the burial in the world meaning it removes the child process from the PROCESS TABLE.

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


## File operations

file_desriptor = open(<filename>, <open_method>, <permission>)


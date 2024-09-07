# FazendaTech - Programming Challenge

## 01 - Programming Tools - Solving the problems from [README.md](README.md)

### Problem 01 - Resolving a Git Merge Conflict

### Problem 02 - Linux Commands (Logging)
1. Write a command that runs the binary file and saves its output to a log file.

To solve this for the file [02-logging](./02-logging) I ran the command:
```
01-programming-tools/02-logging >> 01-programming-tools/output.log 2>&1 &
```
This command remains the terminal free to use while the binary is executing.

2. Write a command that runs the binary file and saves its output to a log file, with standard output and standard error in separate files.

To solve this for the file [02-logging](./02-logging) I ran the command:
```
01-programming-tools/02-logging > 01-programming-tools/stdout.log 2> 01-programming-tools/stderr.log
```
This command remains the terminal free to use while the binary is executing.

### Problem 03 - Linux Commands (Killing a "Rogue" Process)
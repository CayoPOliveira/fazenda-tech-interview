# FazendaTech - Programming Challenge

## 01 - Programming Tools - Solving the problems from [README.md](README.md)

### Problem 01 - Resolving a Git Merge Conflict

### Problem 02 - Linux Commands (Logging)
1. Write a command that runs the binary file and saves its output to a log file.

To solve this for the file [02-logging](./02-logging) I changed to dir with `cd 01-programming-tools` and ran the command:
```
./02-logging >> output.log 2>&1 &
```
This command keeps the terminal free to use while the binary executes, and it combines both `stdout` and `stderr` into a single file. If `>>` is replaced with `>`, the file would have two pointers, and it could result in a messy mix of `stdout` and `stderr`.

2. Write a command that runs the binary file and saves its output to a log file, with standard output and standard error in separate files.

To solve this for the file [02-logging](./02-logging) I changed to dir with `cd 01-programming-tools` and ran the command:
```
./02-logging > stdout.log 2> stderr.log &
```
This command keeps the terminal free to use while the binary execute and outputs `stdout` and `stderr` in two separete files.

### Problem 03 - Linux Commands (Killing a "Rogue" Process)

1. Detail the steps you would take to kill the process as quickly as possible, including the commands you would use.

    1. To find the process, I ran the `top` command. If the process is still consuming a lot of CPU, it will appear at the top of the list.
    2. After identifying the PID of the process, I can kill it.
    3. I ran the command `kill <PID>`. If that doesn't work, I use the `-9` flag to forcefully kill it, like this: `kill -9 <PID>`.

    I tested this with the commands of the problem 02.

2. Come up with a bash script that automates killing a process, assuming you know the name of the binary file that's running.

If I know the process name, it's easy to find using the command:

`ps aux | grep [p]rocess-name`

The `[p]` is a trick to avoid listing the grep process itself.

Then I piped the output to `head -n 1` to select the first line, and to extract the second column (the PID), I piped the output to the `awk` command:

`awk '{print $2}'`

<details>
    <summary>Confession</summary>
    <p>I used ChatGPT to discover how to use the `awk` command.</p>
</details>

Finally, I killed the process with:

`kill -9 <PID>`

I created the script [kill-process.sh](./kill-process.sh) for this purpose. To run it, I changed its permission to executable using:
```chmod +x kill-process.sh```

# Command line interface part 1
## Terminals, shells, and prompt
The terminal is a program that opens a window and lets you type commands for the [shell](https://www.gnu.org/software/bash/manual/html_node/What-is-a-shell_003f.html#What-is-a-shell_003f). The shell is simply another program that allows you to interact with the computer through those commands. In these tutorials we’ll be working on [bash](https://www.gnu.org/software/bash/manual/html_node/What-is-Bash_003f.html#What-is-Bash_003f), a commonly used shell program. Bash (and other similar shells) comes installed on most **_Unix-like_** operating systems, including Mac operating systems and various versions of Linux, but not Windows. The **_prompt_** is just a string of text that ‘prompts’ you for input. Its appearance can be customized and expect it to vary from terminal to terminal.
On our Lubuntu virtual machine the prompt has the following components: 

username – your user name

@ (‘at’ sign) – this is just a separator

 hostname – the name of the computer you’re working on

: (colon) – another separator

~/Sandbox – an example of working directory; the directory you are in right now

$ (dollar sign) – signifies that you are in user mode:
```shell
compbiol@compbiol-VirtualBox:~/Sandbox$
```
In these notes, the text that you should see or enter in your terminal window is on highlighted lines. Each new line means that the preceding line has been entered by pressing the `Return` key (Enter).
## File system: root and home, directory tree
All files and folders (we will be calling them directories from now on) are organized in a tree-like structure. The most inclusive directory, the one that contains all other folders is called the **_root_** directory. There is another directory that is special: it is called the **_home_** directory. If the computer operating system was set up to have multiple users, each user would have their own home directory. Every time you open a new terminal window, by default you are put in the home directory of the user you’re logged in as. You can move up and down the directory tree and the shell keeps track of where you are, displaying your working directory in the prompt. Each location on the file system can be specified, just like an address to a place; this 'address' is called the **_path_**. Path also has another meaning, but we will get to that later.

The **_root_** is represented by a forward slash with nothing preceding or following it: `/`

The **_home_** directory is represented by a tilde or user name: `~`

The **_path_** to your working directory is shown at the prompt, following the colon.

Confusingly, the root directory in your virtual machine has another directory called 'home'. This is not the same as the home directory signified by the tilde `~`. Here we will refer to home directory in the latter sense.
## Basic commands to get around the file system: `ls`, `pwd`, `cd`
Typing commands at the prompt is the primary way of interacting with the shell. Commands are case-sensitive and usually have zero tolerance for misspellings. You can delete characters on the command line using `Backspace` and `Delete`, and move back and forth using `←` and `→` arrow keys.
### `ls` (list) – what’s in here?
Type:
```shell
ls
```
Always take a second to review what you wrote and hit the `Return` key (Enter). By default, this command lists all files and directories in your working directory. It then returns to the prompt. You can also make it list contents of a directory specified by a path:
```shell
ls Sandbox
```
Typing ls and other commands calls a computer program, a so-called executable file, which then carries out the functions of the command.
### `pwd` (print working directory) – where am I?
```shell
pwd
/home/compbiol
```
This is another useful command to get oriented. It prints your path from the root directory. If you remember the distinction between home and root directories, the prompt shows you the path starting at your home directory, while pwd prints the complete path starting at the root directory. Paths starting at the root or home are also called **_absolute_** paths.
### `cd` (change directory) – move around
This command allows you to move to a directory different from your current working directory. You type cd followed by a directory name you want to go into. Remember absolute paths? There is also the concept of **_relative paths_**. It just means a path that is relative to where you are right now. Try typing cd followed by space, followed by Sandbox: 
```shell
cd Sandbox
```
`Sandbox/` is a directory in your home directory. The `cd` command should recognize it as a path relative to your working directory if you haven’t moved out of home since starting the terminal. 
Going up a level:
```shell
cd .. 
```
`cd` followed by two full stops or dots) moves you up a level in the directory tree, that is to your parent directory.

You can combine the two dots with a directory name you know is present one level up from your working directory. Try:
```shell
cd Sandbox
cd ../Code
```
The arguments to cd specified above are examples of relative paths. `cd` in the examples above takes only one argument, but other commands often take more arguments. Arguments are separated by a space, like this: `command Argument1 Argument2`. 
Another symbol that `cd` recognizes is the period `.`. It means ‘the current directory’ and is useful in moving down more than one level in the directory tree. `cd Sandbox` and  `cd ./Sandbox` mean the same thing: move to the `Sandbox` directory, which is present in your working directory. You can also give a forward slash following the directory name, as in `cd ./Sandbox/`, but you don’t have to. `cd /Sandbox` won’t work, however:
```shell
cd /Sandbox
bash: cd: /Sandbox: No such file or directory
```
Why? Recall that root directory is specified by a forward slash. This command tells the shell to move to the Sandbox directory in the root directory, but there is no such directory.
We can go to the root directory and see what’s in there:
```shell
cd /
ls
```
There are several folders, including `bin`, which contains most of the executable programs present on the computer, such as bash itself.
To go back to our home directory from here or anywhere else on the system, we have three options. Typing `cd` by itself takes us to the home directory. `cd ~` works as well.
We could also specify the absolute or relative paths, if we remember them (in the case of moving out of the root the relative path is the same as the absolute path):
```shell
cd /home/compbiol
```
Or we can go back to the last directory we visited, which in this case is home:
```
cd -
```
## Creating directories and files, getting help
### `mkdir` (make directories)
Let’s make a new directory. From Sandbox in your home directory, type:
```shell
cd ~/Sandbox
mkdir Directory1
ls
```
Now you should see a new directory named Directory1.
You can make multiple directories in one command line:
```shell
mkdir Directory2 Directory3
ls
```
### `touch` (make an empty file; change time stamp)
`touch` is very similar in its functionality to mkdir but it allows you to create empty files (touch is actually most commonly used to changing the timestamp of a file). 
```shell
touch file1.txt file2.txt image1.jpg image2.jpg
```
### brace expansion
So far this is all basic and may seem tedious compared to the graphical user interface, especially to a newcomer to the command line. In order to appreciate some of the power of the shell, let’s learn about brace expansion. Brace expansion allows you to easily work with many directories and files.
```shell
mkdir Directory{4..10}
ls
```
Brace expansion works on letters, too!
```shell
mkdir Directory{1..3}/Subdir{A..C} 
cd Directory1/
ls
cd ..
```
In Directories 1 through 3 you should see three directories named SubdirA through SubdirC.
 
### tab completion
Typing Directory1/SubdirA every time you want to move into that directory or, worse, jumping even more levels in the directory tree is tedious and error-prone. Fortunately command line interfaces have a tab completion feature. In the Sandbox directory, try typing `cd D`, then press the `Tab` key. The command line should expand to `cd Directory`. Now you just need to add number to the end and `/`. Now press Tab once again. After expanding to Subdir try pressing `Tab` twice more. You should see the available options:
```shell
SubdirA/ SubdirB/ SubdirC/
cd Directory1/SubdirA/
```
Tab completion also works for command names. Try typing `mk`, followed by pressing `Tab` key twice and you should see every executable whose name starts with `mk`.
Creating subdirectories works only if you already have parent directories created. From the Sandbox directory try:
```shell
mkdir Directory{11..15}/Subdir{A..C}
```
This gives us error messages:
```shell
mkdir: cannot create directory 'Directory11/SubdirA': No such file or directory
...
mkdir: cannot create directory 'Directory15/SubdirC': No such file or directory
```
One of the goals of this class is to convince you that the command line interface is very powerful. You should expect that the basic task of creating subdirectories within new parent directories should be trivial. This brings us to getting help.
### `man` (manual pages)
Type:
```shell
man mkdir
```
The program man allows you to access manual pages for programs that support it. Practically all common commands will have a manual, although sometimes its contents can be daunting for new users of the command line. After opening mkdir’s manual you should be able to scroll line by line with `↑` and `↓` arrow keys, scroll page down with the `Space` or `PgDn` keys, and scroll page up with `PgUp`. You exit the manual pages by typing `q`.
From the manual pages for mkdir we learned that it supports a variety of options. Options are most commonly specified by preceding a single letter with a single dash, for example `-v`, or by multiple letters preceded by double dash. An example of the latter is `--help`. Try typing `mkdir`, followed by a space, followed by two dashes and 'help': 
```shell
mkdir --help 
```
Help is an option available for many commands and its output is often more compact than manual pages. It should also automatically return to the prompt after printing out help contents. If help’s output goes beyond your terminal window screen, you can navigate up your terminal window by using the scroll bar on the right or holding down `Ctrl+Shift` keys together with `↑` and `↓` arrow keys.
After looking at the available options to `mkdir`, we see that `-p, --parents` states 'no error if existing, make parent directories as needed'. This sounds like the option we want. You can specify it as a single dash immediately followed by `p` or two dashes and `parents`.
Now you have all the knowledge needed to create files within subdirectories within parent directories. This would be very difficult or time-consuming using graphical user interface. In your Sandbox directory, try to create new directories, named ‘Directory11’ to ‘Directory15’, each with three directories within them, named ‘SubdirA’ through ‘SubdirC’. Then create three empty text files called ‘file-1.txt’ through ‘file-3.txt’ and three empty images ‘image-1.jpg’ through ‘image-3,jpg’ in each Subdir directory. You should be able to do this on two or three command lines, combining option to `mkdir`, brace expansion, and `touch`.
Your commands should look like this. Each touch command here has a single argument:
```shell
mkdir -p Directory{11..15}/Subdir{A..C}
touch Directory{11..15}/Subdir{A..C}/file-{1..3}.txt
touch Directory{11..15}/Subdir{A..C}/image-{1..3}.jpg
```
## command history and more line navigation
If you were able to figure this out and typed two touch on two separate lines, you probably noticed that they were very similar, differing in only a few characters. A useful trick to save you time is accessing recently used commands by hitting the ↑and ↓ arrows while at the prompt to scroll up and down history. Once you have the command you want to repeat or modify, you can move around that line and modify its text as usual. Some useful keyboard shortcuts to move along the line include:
`Ctrl+A` – takes you to the beginning of the line
`Ctrl+E` – takes you to the end of the line
`Ctrl+→` , `Ctrl+←` –   jump left or right one word at a time
Moving up and down one line at a time is inefficient if you are looking for something you typed a long time ago. Fortunately, you can search the command history. Press Ctrl+R to access the search. Now you can type text that you wish to find. We can look for the mkdir calls:
```shell
(reverse-i-search)`mkdir': mkdir -p Directory{11..15}/Subdir{A..C}
```
If there is more than one match for a command containing mkdir, you can scroll through them by hitting `Ctrl+R`  until you find the command you want or by refining the search by typing some additional text, such as option to the command, brace expansion etc. 
### `cp`  (copy) – copying files and directories
Copying files in the command line is easy. You type `cp`, followed by name of the file you want to copy (remember you can use tab completion!), followed by a name of the file that will be created as a copy:
```shell
cp file1.txt file1-backup.txt
```
This command does not work with directories, unless you specify `-r` (recursive) as an option. This will copy a directory together will all its contents, including subdirectories and files:
```shell
cp -r Directory15 Directory15-backup
```
You can also use cp to copy from one path (source) to another (destination). In such cases you may wish to leave the name of the copied file as it was. Remember that your working directory can be specified as a single dot:
```shell
cp Directory15/SubdirB/image-3.jpg .
```
Be careful when copying files! If a file with the same name as the file being copied already exists in your destination, `cp` will just substitute (overwrite) it without any notification. There is no undo feature in the shell, so the overwritten file will be lost forever. You can add `-i` as an option to `cp` for an interactive mode. It will then ask you if you are about to overwrite a file:
```shell
cp -i Directory13/SubdirC/image-3.jpg .
cp: overwrite './image-3.jpg'?
```
The prompt will then wait for you type `y` for yes or `n` for no and press Return. 
Try backing up Sandbox files ‘ants.txt’ and ‘matrix-5214genes.phy’ by copying them in a directory outside Sandbox.
### `mv` (move) – moving and renaming files and directories
Moving of files without copying them is done by `mv`, which can also be used to rename them. It works very similarly to `cp`. You supply it with your source and destination. From `Sandbox/` type:
```shell
mv ants.txt Directory1
mv Directory1/ants.txt .
```
Above we copied the file ‘ants.txt’ to Directory1/ and back to Sandbox/. If you want to rename a file, just give it the same destination with an alternative name as the second argument (i.e. the new name):
```shell
cp ants.txt Directory1
mv Directory1/ants.txt Directory1/formicidae.txt
ls Directory1
```
Move also supports interactive mode (asks you in case of overwriting) with the `-i` option. Mv differs from `cp` in that it works on directories without any additional options.
### `rm` (remove) – removing files and directories
The command `rm` is used to remove files. It’s not like moving things to ‘trash’- once you remove something there is no way to bring it back. It works similar to `cp` or `mv` and has to be supplied with `-r` option to be able to remove directories:
```shell
rm -r Directory2
```
This option is potentially very dangerous, but running it with `-i` in the interactive mode (recall we’ve seen this in cp and mv) will prompt you before removing each element. This obviously wouldn’t be desirable if you are trying to erase many hundreds of files.
Single-character options can usually be combined without the need to add another dash:
```shell
rm -ri Directory3
```
The above will allow you to remove a directory with all its contents, at the same asking for confirmation before execution.
### wildcards
Another powerful feature of the shell is its ability to work with multiple files in a single command. Say you want to copy (or move or remove, etc.) all text files from one directory to another. If all text files follow a simple pattern, for example end in `.txt` (the so-called extension; not to be confused with expansion below), the simplest way to do this is by using the `*` asterisk wildcard.
First, let’s list all text files in one of the directories we created earlier in Sandbox:
```shell
ls -1 Directory11/SubdirB/*txt
```
Supplying `-1` as an option to ls gives each element on one line. You should be able to see three text files (along with their relative paths) which we created earlier. Asterisk in this case means ‘any character matched zero or more times’ and we say that it expands to those characters before executing the command. This is the same concept as in brace expansion we’ve seen earlier. In this case `*` expands to file-1., file-2., etc. Note that this didn’t list the .jpg images we created earlier. Since asterisk expands to any character, using it by itself will list everything in a directory:
```shell
ls -1 Directory11/SubdirB/*
```
You can use the same trick to copy these files to your working directory (signified by a period):
```shell
cp -i Directory11/SubdirB/*txt .
```
`cp -i` here will notify you if you are about to overwrite some files in your working directory.
Try listing, copying, and moving some ‘.jpg’ files around using the asterisk wildcard. 
You can also remove all those folders and files we created in Sandbox throughout this tutorial, but try to leave files ‘ants.txt’ and ‘matrix-5214genes.phy’. If you haven’t already, you can back them up in a directory outside Sandbox.

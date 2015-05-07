# Command line interface part 2

## Locating files and directories in your system 
If you erased all of the folders at the end of the last tutorial, let’s go back and create some empty files and directories again. If you recall, you can search the command line history by either moving up and down with arrow keys, or you can access the history search with `Ctrl + R`. Once you are in the search mode, you can type `mkdir`, `mkdir -p`, `touch` or `{` (because we used brace expansion) or whatever gets you to the command you want. You can cycle back through matches by pressing `Ctrl + R` as many times as you need to find the command you’re looking for. Let’s execute the following commands again:
```shell
mkdir -p Directory{11..15}/Subdir{A..C}
touch Directory{11..15}/Subdir{A..C}/file-{1..3}.txt
touch Directory{11..15}/Subdir{A..C}/image-{1..3}.jpg
### `find` (search for files in a directory hierarchy)
```
The `find` command is a rather sophisticated tool, but its basic functionality is to, unsurprisingly, find things. The interface of `find` is more complicated than that of the other commands we’ve seen so far and is a good introduction to running more complex programs. There are three kinds of arguments that you may want to supply to find:  (1) where to look for something, (2) what to look for, and (3) what to do. All are optional.  From  `Sandbox`, try `find` by itself:
```shell
find
```
The output should look something like this:
```shell
.
./Directory12
./Directory12/SubdirA
./Directory12/SubdirA/file3.txt
./Directory12/SubdirA/image1.jpg
...
```
Without any arguments, `find` uses defaults. This means printing out (the default what to do argument) a list of paths to all files and directories (default what to look for) within the working directory (including the working directory itself, represented by the period at the top of the list; this is the default for where to look). If you specify only one argument, it will be interpreted as the path in which to search (`find` by itself is thus the same as `find .` or, in this example, `find /home/compbiol/Sandbox`). Sometimes this list will be very long and printing it will take a long time, for example when searching from the root directory. You may decide to **_interrupt_** `find` and go back to the command line. You can do this with `Ctrl + C`.
The where to look argument is specified without any special characters or options preceding it, but the other arguments are different. In order for `find` to know that you are specifying other arguments, you need to precede them with the option name. To set the ‘what to look for’ argument, you need to precede it with `-name`:
```shell
find . -name 'image1.jpg'
```
You can use wildcards in the search pattern:
```shell
find . -name 'image*.jpg'
```
You should surround the search pattern with quotes, especially if you are using wildcards or the file name you are trying to find includes spaces or some special (non-alphanumeric) characters. Quoting is important in the shell, and we will spend some time covering it when talking about regular expressions.
`find` by default has the useful ability of reaching down the directory tree and searching within subdirectories. It also supports many other options and even allows you to easily execute other commands on the results of its search. See [here](http://content.hccfl.edu/pollock/Unix/FindCmd.htm) and [here](http://www.grymoire.com/Unix/Find.html) to learn more.
### `locate` (find files by name)
One major drawback to `find` is that it’s slow. If you are looking for a file but you have no idea where it could be located, you need to start at the root. A search like that will take a long time. You may consider `locate` as an alternative. `locate` is extremely fast because it searches through a database of indexed file names on the system. Because the database is updated only periodically, you may not find files that were recently added to your system. `locate` has several options (see `locate --help` or read about them [here](https://www.gnu.org/software/findutils/manual/html_node/find_html/Invoking-locate.html)), but most of the time you just want to search for a particular file name, which will be the only argument:
```shell
locate '*txt'
```
`locate` searches through list of absolute paths for the indexed files, not down a directory tree, like `find` would. If you specify a directory for it, it has to be an absolute path and the search will only be performed in that one directory, but not its subdirectories. However, you can include wildcards that would match them.
Compare the results of locate and find by searching your home directory for: 1) all files ending with the `txt` extension and 2) all files that end with `jpg`.

You code could look like this:
```shell
find ~ -name '*txt'
locate '/home/compbiol/*txt'
find ~ -name '*jpg'
locate '/home/compbiol/*jpg'
```
You should be able to see the files you created today using `find` but not `locate`.
### `less` (viewing text files page by page)
Imagine that you have several huge text files that you want to take a peek at. It takes a long time to open those in a text editor, and your computer runs out of memory after you try to open more than one of them. The command line lets you quickly look into and search through files that are hundreds of megabytes in size.
`less` is an example of a **_pager_**, or program that allows you to scroll through text files page by page, starting from the beginning. The interface is similar to `man`, which also uses a pager. You can exit by typing `q`.
```shell
less ~/Sandbox/ants.txt
```
### `head` and `tail` (print lines from a file)
These two handy commands let you take a look at the beginning or ending of a file. This is useful if you want to just get a sense of what’s in a text file. By default `head` and `tail` will print the first or last, respectively, ten lines. This can be changed by specifying a number preceded by a dash. The other argument will be the name of the file you want to look at:
```shell
head ~/Sandbox/ants.txt
head -50 ~/Sandbox/ants.txt
```
`tail` works in the same way, except that it prints lines from the 'tail' end of a file. It also has a very handy option `-f` for monitoring what is being written to a file in real time. This is useful for figuring out what the latest output from you script/bioinformatics pipeline/phylogenetic analysis program/etc. looks like.
### `cat` (concatenate and print contents)
A popular alternative to a pager (such as `less`) is the command called `cat`. It will print out contents of the entire file to screen and you can specify several options, including printing line numbers with `-n` and highlighting tabs in your file with `-T`. The file `ants.txt` is a moderately-sized file with approximately 150,000 records associated with [ant specimens](http://www.antweb.org/) in California Academy of Sciences and other natural history collections. Each record is a single row (line) with multiple columns separated by tabs. Let’s look at it using `cat`, and then `cat` with combined `-T` and `-n` options:
```shell
cat ~/Sandbox/ants.txt
```
This will run for a while. Interrupt it with `Ctrl + C`.
```shell
cat -Tn ~/Sandbox/ants.txt
```
Again, you can interrupt it with `Ctrl + C`. Note how we can combine `-T` and `-n` options by putting them together, preceded by only one dash (the order doesn't matter; `-nT` means the same). In this case we see that line numbers are added at the beginning of each row (the lines likely won’t fit on your screen and will be **_wrapped_**, appearing across multiple lines of the terminal). The 'tabs' are also highlighted as `^I` (caret followed by capital 'I').
The `cat` command also has another functionality, from which it gets its name: it can concatenate files. We will return to this feature after we talk about redirection and pipes.
### `grep` (print lines matching a pattern) 
A very handy command line program is `grep`. It’s used to search for text patterns and its early precursor was one of the first programs to use regular expressions, the awesome pattern-matching tool you will learn about in the next section. However, you can simply use `grep` to search for any combination of letters within a file. By default, it will print out the whole line that matches and highlight the match itself. 
The file `matrix-5214genes.phy` is a large text file containing many amino acid sequences. If your name is composed of the 20 letters that comprise the amino acid alphabet (ACDEFGHIKLMNPQRSTVWY), you may be able to find it somewhere in this file. Use all uppercase letters. My name matches several times:
```shell
grep 'MAREK' matrix-5214genes.phy
```
Try finding some names, including yours or your friend’s if you can’t find a match.
## Standard input and output: redirection and pipes
In order to take advantage of some of the most useful features of the shell, you should get a better understanding of how input and output of a command line program can interact with each other. In a Unix shell environment, we can talk about [standard streams](http://www.linfo.org/standard_output.html) (sometimes also called channels). You can imagine those as streams of data (for example text) that flow between programs and devices. There are three kinds of these streams: one that goes into a program, called **_standard input_** (stdin for short), one that goes out of a program, called **_standard output_** (stdout), and one that reports any errors that the program might have encountered processing stdin. This last stream is called **_standard error_** (stderr). How does this work in the context of what we’ve seen so far? When we used the `grep` command above, its standard input was the file in which we wanted to find a pattern. The standard output was the matched lines, which were printed on the screen. We didn’t encounter any errors, but stderr would have also been printed to the screen.

A very powerful feature of the shell is the ability to divert or redirect standard streams. Instead of both stdout and stderr going to the screen, you can make them go to a file or another program. Because of this, you are not limited to the single command that does one or two things. You can pass standard streams around between programs, files, and your screen.

There are two ways streams can be redirected, because you need to tell the system whether you are redirecting to or from a file, where the stream is supposed to be written or read, or to an executable program that will process it in some way. We will focus on standard output redirection and will not be concerned about standard error.
### Redirecting output to a file
Say that instead of printing standard output of `grep` to the screen, you want to write it to a file. In order to redirect, you can use the greater-than sign: `>`. Imagine that you want to save your `grep` search results into a new file. To redirect the stream from your screen to a file, following the command and its arguments, add a space, the greater-than sign, another space, and the name of the file you want the output saved into:
```shell
grep 'CAKE' matrix-5214genes.phy
grep 'CAKE' matrix-5214genes.phy > cakes.txt
```
This gave no screen output, but created a new file, called `cakes.txt`, where all the output we would have seen on our terminal screen was written (but without highlighting the matching text).
Be careful when redirecting output: `>` will overwrite a file if there already is one with the same name. You can append to the end of a file with double greater than: `>>`:
```shell
grep 'PIES' matrix-5214genes.phy 
grep 'PIES' matrix-5214genes.phy >> cakes.txt
```
The `cakes.txt` file will now have all the lines containing the word 'CAKE' in them, followed by all lines that matched 'PIES'.
### Redirecting output to an executable
Redirection to another program (e.g. command) is similar to file redirection, but you need to let the shell know that stdout goes to an executable. This is done using the vertical bar on your keyboard, or pipe: `|`.  Let’s look at yet another way of searching through your command history. There is a way to print out your saved command history by simply typing `history`. Now that you know about `grep`, you can redirect the output of `history` to `grep`, which will then know to treat it as stdin (just as if it was a file supplied in an argument):
```shell
history
history | grep 'mkdir'
```
You can combine multiple pipes and file redirections:
```shell
history | grep 'mkdir' | grep '{'
history | grep 'mkdir' | grep '{' > my_braced_mkdir.txt
```
In the first line above, `history` will first send all its entries to `grep`. Then only those containing `mkdir` will be passed on to another `grep` search, which in turn will extract only lines containing opening curly bracket. You can see the output on your screen. In the second line we added a file redirection, so that the output from the second `grep` goes into a file named `my_braced_mkdir.txt`.

The above is a somewhat contrived example, but hopefully by now you can appreciate the usefulness of redirection for building pipelines that achieve more than each of their components. For a more detailed overview of different types of redirection, follow this [link](http://www.tldp.org/LDP/abs/html/io-redirection.html).
How would you combine the ability of ‘cat’ to highlight tabs and numbering lines to look at the last 50 lines of a large file? This should work:
```shell
cat -nT ~/Sandbox/ants.txt | tail -50
```
Remember that `cat` is abbreviated ‘concatenate’. You can easily combine text files and write their output as a separate file:
```shell
cat ants.txt cakes.txt > two_combined.txt
cat *txt > combined_text.txt
```
### `wc` (word count) and `cut` (remove sections from each line)
Two other commands deserve a mention here, as they are useful for looking at file content.
The first one is `wc` and it counts the number of lines, words, and bytes in input:
```shell
wc ~/Sandbox/ants.txt
```
You can restrict the output of `wc` to print only the number of lines by adding `-l` as an option. I use `wc -l` often to see how much was written to a file, check the number of matches, make sure all the files I just moved around are accounted for, etc. Simply pass the output of your pipeline to `wc`:
```shell
ls *txt | wc –l
```
Another command useful for looking at files, and especially table-like data, is `cut`. It takes at least one option and a file or stdin from other command. With its option `-f` you can specify a number of a column in a file and extract just that column. In our `ants.txt` file, the 4th column contains species names for each record (row):
```shell
cut -f 4 ants.txt | tail
```
You can specify multiple columns, ranges, and the type of separator by which the columns are counted. See the manual or help for `cut` and the cheat sheet for this section for more options.

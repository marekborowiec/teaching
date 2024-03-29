# Command line interface part 5
Anther very powerful command is `awk`. It is actually a complete programming language designed for fast and flexible manipulations of text files. Its basic capabilities are similar to `sed` but it often has a more intuitive use. Knowing `awk` better will also allow you to accomplish things more often with one command instead of stringing long pipelines from different commands together. Just like `sed`, `awk` works on files line by line. This brief overview is just to give you an idea about what `awk` is. If you are working with molecular sequence data, you will often find solutions to manipulate sequence files on-line using `awk`, some of them very complex. You will not be able to understand them all right away but the idea is to give you some familiarity with what you may encounter.
Its basic syntax is:
```shell
awk 'pattern { action }' file
``` 
Pattern means "if this line matches some condition..." and actions means "... do something". Pattern and action are optional (you can specify only one if you want to) and by default the pattern matches every line and action is none.
A common action is to print something to the screen (or to output where it can be redirected to another command or file). The following will print the third "column":
```shell
echo 'one two three'
echo 'one two three' | awk '{ print $3 }' 
```
`awk` by default assumes that any whitespace character (space or tab) is the separator. This is why we don't see the correct output when we try to print the "identified by" column of our specimen data file:
```shell
awk '{ print $41 }' ants-na.txt | head
```
There is a special pattern called `BEGIN` that will allow us to modify the default `awk` behavior or execute some action before any lines are read. We can use it to change the default separator/delimiter from any whitespace to specifically the tab, or `\t`:
```shell
awk 'BEGIN { FS = "\t" } ; { print $41 }' ants-na.txt | head
```
Now, that looks much better. `FS` is a variable that in `awk` stands for Field Separator.
There is also a special pattern called `END`. Unsurprisingly, it allows the user to do something *after* all lines have been read. Let's see how it works. With the `ls -l` (that is `-l` for `long`) command we can print the long form of information about out files in the `Sandbox` directory.
```shell
ls -l
```
You will see that there are several things in there and that the fifth column, counted separated by whitespace, has some numbers. Those are number of bytes of memory each file occupies. We can add those numbers using `awk`:
```shell
ls -l | awk '{ sum += $5 } END { print sum }'
```
In this case, we define the variable called `sum` and increment it using the `+=` operator. The increment operator is common in programming and is a short way of writing `z += y` instead `z = z + y`, for example.
Just as the built-in variable `FS` stores the character `awk` uses to separate fields, it has another internal variable called `NR`, which it uses to track the line numbers in file. We can use this to print column averages:
```shell
ls -l | awk '{ sum += $5 } END { print sum / NR }'
```
Remember that we said that we can also match patterns? You can use regular expressions or simple matching before the action enclosed in curly braces like this: `$field ~ /pattern/ { action }`. Let's find all files that have "txt" in their name and print their total size:
```shell
ls -l | awk '$9 ~ /txt/ { sum += $5 } END { print sum }'
```
I personally like to use combination of `awk` and `sed` to rename files in bulk:
```shell
ls *out | awk '{ print "mv "$1" "$1 }' | sed 's/.txt.out/.out/2'
```
Is exactly the same as:
```shell
ls *out | sed -r 's/(.*)/mv \1 \1/g' | sed 's/.txt.out/.out/2'
```
You can filter out records that are above a certain number. The following will show only species names (columns 10 and 11) and elevations (column 26) of records from above 7,500ft:
```shell
awk 'BEGIN { FS = "\t" } ; $26 > 7500 { print $10, $11, $26 }'
```
If you are working with sequence data files, such as `FASTA` and `FASTQ`, `BED`, `SAM`, or `VCF`, you will find [bioawk](https://github.com/lh3/bioawk) very useful and powerful. This is a tool you need to install separately, as it doesn't usually come with standard operating systems. You can find a nice write-up about `bioawk` functionality [here](https://bioinformaticsworkbook.org/Appendix/Unix/bioawk-basics.html) and a brief tutorial [here](https://github.com/vsbuffalo/bioawk-tutorial). 

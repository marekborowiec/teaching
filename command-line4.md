# Command line interface part 4
Today we cover a very powerful command, the stream editor `sed`. It uses a simple programming language, designed for text manipulation and most commonly used for text substitution, selective printing of text, and editing of text files.
In order to fully understand how `sed` works, it is important to review how a command works. When we run `sed` (or any other command), we have a stream of data (standard input) coming from a file or another command. This stream is being taken line by line by `sed`. Then some processing is done on that line. The result of the processing is then printed to standard output. This is repeated for each line of input.
In `sed` the input is not directly modified. Instead, it is first placed in a special storage space called the **_pattern buffer_**. The pattern buffer is loaded directly from the input, and is used to hold the line on which the command(s) is executed. The pattern buffer is emptied as soon as output has been created; the buffer is empty when a new line is read.
In summary,  the `sed` workflow for each line looks like this:

1) Read a line from standard input (file or another command)

2) Place it in pattern buffer

3) Modify pattern buffer accordingly

4) Print pattern buffer to standard output (screen or file or another command)

There is also the 'hold buffer' capacity that keeps the data after the command was executed and its contents can be further manipulated for more complex operations, but we will not use it today.
We will focus on the pattern buffer and text substitution. `sed` is a powerful command and if you are interested in learning more, there some good resources available on-line: a `sed` [tutorial](http://www.tutorialspoint.com/sed/index.htm) and a [series of articles](http://www.thegeekstuff.com/category/sed/page/2/) on `sed` (click on 'NEXT ENTRIES' to see more articles).
### Addresses and patterns; printing in `sed`
Let’s try printing some file contents using `sed`.
```shell
sed -n '500p' ~/Sandbox/ants-na.txt
```
The syntax of printing in `sed` follows simple formula: `sed -n 'ADDRESS'p input_file`. The `-n` option suppresses automatic printing of pattern buffer, so that only the line(s) at the address is printed. Here we printed line number `500`. You can also print ranges:
```shell
sed -n '1,10p' ~/Sandbox/ants-na.txt
```
This is equivalent to `head ~/Sandbox/ants-na.txt`.  

The last line in the file is denoted by `$`.

You can also print lines that match a pattern, either a simple text match or a regular expression:
```shell
sed -n '/Lasius/p' ~/Sandbox/ants-na.txt
```
The syntax is `sed -n '/PATTERN/p' input_file` This mimics `grep 'Lasius' ~/Sandbox/ants.txt`. With `sed`, however, we can easily combine addresses and patterns:
```sed
sed -n '15000,/Lasius/p' ~/Sandbox/ants-na.txt
```
The above prints from line no. 15,000 until it encounters a line that matches characters 'Lasius'.
Similarly to printing, you can delete select lines using `d` instead of `p`. In that case you would want to print the pattern buffer output by leaving out `-n`.
### Text replacement in `sed`
Probably the most common use of `sed` is for replacing text from the command line. 
The general syntax is the following:
```shell
sed options 'ADDRESSs/PATTERN/REPLACEMENT/FLAGS' input_file
```
Note the lowercase `s` between the `ADDRESS` and `/PATTERN/`. Let’s take a look at an example from our `ants-na.txt` file:
```shell
sed -n '/casent/p' ants-na.txt | head -1 
sed -n 's/casent/CASENT/p' ants-na.txt | head -1
```
First, we match the string 'casent' and pipe the output to 'head' so that we get only the first match. You should be able to see that the third column is 'CAS:ANTWEB:casent0000089'. On the next line, we told `sed` to print only modified lines with `-n`. We didn’t specify the address, which makes `sed` go through the entire file. We turned on substitute with `s`, followed by the pattern to find and its replacement. We then told `sed` to print the lines on which replacement occurred and piped stdout to see only the first line. The third column now reads 'CAS:ANTWEB:CASENT0000089'.
By default, `sed` replaces only the first occurrence of pattern on each line. We can use numbers as flags to tell it to modify any given occurrence:
```shell
echo "one one one" 
echo "one one one" | sed 's/one/two/2'
```
Or we can use `g` flag ('global') to modify all occurrences of a pattern on the line:
```shell
echo "one one one" | sed 's/one/two/g'
```
The backreferences from regular expressions are very useful for modifying text. Let’s see how they work doing a batch renaming of files. Let’s start with making some empty files we will be renaming:
```shell
touch file{1..10}.txt.out
```
We want them to have a shorter extension, `.txt` instead of `.txt.out`. We can then list them with `ls`:
```shell
ls *txt.out
```
After pipine the results of `ls` to `sed`, it’s easy to print the rename (`mv`) command for each file:
```shell
ls *txt.out | sed -r 's/(.*)/mv \1 \1/'
```
We use the `-r` option to get a flavor of regex similar to `grep -E`. All we have to do now is modify the second occurrence:
```shell
ls *txt.out | sed -r 's/(.*)/mv \1 \1/' | sed 's/.txt.out/.txt/2'
```
Note that at this point we haven’t renamed any files, but we have a ready list of commands to do so. We can execute each line by simply piping the output of the second `sed` command to `/bin/bash`:
```shell
ls *txt.out | sed -r 's/(.*)/mv \1 \1/' | sed 's/.txt.out/.txt/2' | /bin/bash 
```
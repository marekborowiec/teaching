# Command line interface part 3
## Quoting in shell
Quoting is important in the shell because there is a need to differentiate characters that have to be interpreted literally from characters that have special functions. The latter are often called **_metacharacters_** and we already encountered several, including the space, asterisk `*`, greater-than sign `>`, and pipe `|`; try to remember what each of them means). You can still use all these signs in a sentence, but you need quotes to let the computer know whether you want them interpreted literally, or if you want to, for example, expand some file names. There are many other characters that are special to the shell, and you can find an extensive table [here](http://www.grymoire.com/Unix/Quote.html). In addition, what characters are special and what characters are not depends on the command or even option used. This can get rather confusing, but don’t panic. Let’s go over the major ways to quote text in the shell: double quotes, single quotes, and backslash.
### Double quotes, the so-called weak quotes
You use quotes to **_escape_** special characters. This simply means that you make the computer interpret them literally, stopping them from being special. One way to do this is to use double quotes. `echo` is a command that simple 'echoes' its arguments back and it will be useful in these examples. From your `Sandbox` directory, try:
```shell
echo Why *ants*?
```
If you still have the text file with ant records, this should give you `Why ants.txt`. This is because the asterisk expands to any characters matching a file name. The question mark does that too, but it expands to any one character. To have it read as plain text, we can surround the above with double quotes:
```shell
echo "Why *ants*?"
```
This does the trick. Let’s try another one.
```shell
echo I made some $$$ today
```
Instead of the three dollar signs, the above will give you a number followed by a dollar sign. This happens because the shell interprets the dollar sign as signifying a **_variable_**. A variable is a name that was previously assigned to some other object. An example would be `$SHELL`, which gives you the name of the shell file you’re using (try `echo $SHELL`). In this case the second dollar sign is the name of the variable: the process ID number under which the shell executed your command. No worries, we know double quotes!
```shell
echo "I made some $$$ today"
```
Wait, that didn't work either!
This is because the shell allows you to use variable names within double quotes. It can be convenient when you are writing a computer program and want to escape some text, but still be able to use variables inside of it. To have the above act as a literal string of text, we need to use single quotes. That’s why they are also known as 'strong' quotes.
### Single quotes or the 'strong quotes'
Try:
```shell
echo 'I made some $$$ today'
```
The single quotes worked. Having two kinds of quotes also allows you to quote double quotes inside single quotes, and vice versa:
```shell
echo "This wasn't that hard"
echo 'Very "funny " '
```
The quotes act like switches. The opening quote tells the shell where the escaped text starts, and the closing marks where escaping should stop. This is why it doesn’t make sense for the shell to have only one quote. It will continue prompting you for more input, until you close the quote:
```shell
echo This wasn't that hard
```
This is why you need to keep track of your quotes and, unfortunately, why you cannot use quotes of one kind within quotes of the same kind:
```shell
echo 'This wasn't that hard'
```
The 'switch' behavior of single and double quotes explains why the above won’t work, and also why the below line is equivalent to the earlier example "This wasn't that hard":
```shell
echo 'This wasn'"'"'t that hard'
```
### Backslash quoting
The two examples of quoting above work slightly different from another way to escape characters: the backslash `\`. The backslash simply escaped the character immediately in front of it. It doesn’t mark a start for the whole sequence to be escaped, like the quotes did. It is 'the strongest' type of escape and is useful in certain situations, for example if you need to quote both single and double quotes in one string:
```shell
echo This wasn\'t \"great\"
```
Remember that the space is also a special character? In the above `echo` prints three separate arguments: `This`, followed by `wasn’t`, and `“great”`. We would need to escape the spaces to make it a single string and only one argument:
```shell
echo This\ wasn\'t\ \"great\"
```
This will not work:
```shell
echo 'This wasn\'t that hard'
```
You will be prompted for more input. When you type an additional `'`, the command will print out `This wasn\t that hard`. This is because the first single quote switches on escaping, and because `\` is a quote character different from `'` it is being interpreted literally as a backslash character, not a quote anymore. You could see this when the command executed. Then the second quote `'` turns off quoting. The last quote of the string turns quoting on again, and the command line thinks you wanted to give it additional input to quote.   
## Regular expressions
As we have already learned, one can think of text as literal characters or metacharacters, or characters that have special meaning. Regular expressions, **_regex_** for short, is a system that uses metacharacters to match text patterns of various degrees of complexity. Regex is used by several shell commands and many programming languages. It’s useful to think of it as a powerful search and replace tool.
One important caveat is that regex varies among its implementations, with different metacharacters available in different tools and languages. We will focus on basic regex used by the command line tool `grep` with the option `-E` (also accessible through command `egrep`).
Some graphical-use-interface text editors use regexes and popular ones include TextWrangler (for Macs) and EditPad (for Windows).
### Character classes
The first feature of the regular expression language that we’ll discuss today are character classes. Character classes are delimited by square brackets and mean “match a character that is within (or outside) this set of characters. The class may simply be a list of alternatives. Let’s search through a dictionary file located in `/usr/share/dict/words`:
```shell
grep -E 'mol[td]' /usr/share/dict/words
```
In the above example, the regex comprises literally interpreted, 'ordinary' characters ('m', 'o', and 'l') immediately followed by a character class signifying one character that is either 't' or 'd'. The order within the class does not matter.

There is an important distinction to make here. `grep` by default matches the entire line of text where a pattern is found, but highlights the match of the pattern itself. We can look at the matches by themselves by specifying `grep -Eo`. Realizing what the regular expression actually matches is important, especially as we begin using the matches to replace text. We can also specify ranges within character classes:
```shell
grep -E '[u-z]ing' /usr/share/dict/words
```
This matches any four-letter text starting with letters 'u' through  'z' and ending with 'ing'. Within a character class, most metacharacters are treated literally, however, as we’ve seen in the above example, a dash `-` will be treated as a metacharacter specifying a range. We can make the character class interpret it literally by putting it as the first character in the class.
Using another special character at the beginning of a class, the caret `^`, we can **_negate_** a character class:
```shell
grep -E 'mol[^td]' /usr/share/dict/words
```
This matches `mol` followed by exactly one character that can be anything, except letters 't' or 'd'. To include the caret as a literal character inside a class, put it anywhere except the beginning of the class.
So far we’ve seen character classes that match only one characters. Most often, however, we will want to match multiple characters from within a class. A plus `+` quantifier serves just that purpose:
```shell
grep -E 'casent0732[0-9]+' ~/Sandbox/ants.txt
```
This matched anything that began with the literal string 'casent0732' followed by one or more of digits from 0 through 9.
### Line and word boundaries
Caret has another meaning when used outside character classes: it can signify beginning of line:
```shell
grep -E '^mol[^td]' /usr/share/dict/words
```
Because the dictionary contains one word per line, we can see this matched characters 'mol' at the beginning of a line, followed by one character that is not included in the `[td]` class. Let’s try another one:
```shell
grep -E '^ee[a-z']+' /usr/share/dict/words
```
This matches all text that begins with double 'e' at the beginning of a line, followed by any number of letters and/or single quotes. Note that to include the single quote inside we use double quotes to enclose the expression.
Similarly, to match the end of line we can use dollar sign:
```shell
grep -E "[A-Za-z]+ee$ /usr/share/dict/words
```
This finds all text that begins with any number of letters (including upper-case!) and has double 'e' at the end of the line.
Similarly to beginning and end of line, you can match word boundaries. In this context, a 'word' is any sequence of characters that is composed of letters and/or digits; This is the so-called **_alphanumeric_** text. To signify the beginning of a word use backslash and less-than sign `\<` and backslash with greater-than sign to match the end of a word:
```shell
grep -E 'secondary \<[a-z]+forest\>' ~/Sandbox/ants.txt
```
An alternative is to use forward slash followed by lower-case letter 'b'. `\b` signifies word boundary and will work for both beginning and end of alphanumeric string. This achieves the same as the above:
```shell
grep -E 'secondary \b[a-z]+forest\b' ~/Sandbox/ants.txt
```
Try coming up with a dictionary (`/usr/share/dict/words`) searches for any entire word that 1) begins with double 'o', including apostrophe and an 's', 2) contains double 'o', 3) ends with double 'o' but not apostrophe and an 's'.
Your code could look like this:
```shell
grep -E "^oo[a-z']+" /usr/share/dict/words
grep -E "[A-Za-z]+oo[a-z']+ " /usr/share/dict/words
grep -E '[A-Za-z]+oo$' /usr/share/dict/words
```
### Specifying number of matches
You can tell the expression how many matches of a particular character or set you need. This is done using curly braces:
```shell
grep -E '^[a-z]{2}o{2}[a-z]{2}$' /usr/share/dict/words
```
In the above expression, we match any line that begins with any two letters, followed by exactly two 'o' letters, followed by any two letters, immediately followed by the end of the line. You can also specify ranges of numbers of matches, but instead of separating them with a dash, use a comma, as in `{2,6}`.
### Optional matches
For any character class we can also specify optional matching. Let’s imagine you want to make your pattern more flexible by allowing some pattern to be matched optionally. This would make your expression match cases where a certain pattern matches and where it doesn’t. You can do it by adding a question mark `?` after a single character or character class, or enclosing the optional pattern withparentheses if it contains more than one character or class:
```shell
grep -E "[A-Za-z]+oo('s)?" /usr/share/dict/words
```
This matches entire words ending double 'o' followed by apostrophe and 's' or those that just end with 'oo'. There is no limit to how complex an optional pattern enclosed by parentheses can be. A common use of optional patterns is for separators, such a spaces that may or may not be present in text we want to find:
```shell
echo 'dataset data set' | grep -E 'data set'
echo 'dataset data set' | grep -E 'data ?set'
```
matching any character with period and making matches optional with asterisk
In regular expressions, a period stands for any character:
```shell
echo '123!@#"* one_two THREE' | grep -E 'two...'
```
The above matches any three characters preceded by a space or tab.
In regex, the asterisk can be used to match the item preceding it zero, one, or more number of times. For example, `.*` will match every character:
```shell
echo '123!@#"* one_two THREE' | grep -E '3!.*'
```
In this the asterisk is similar to the plus sign, but it can also mean optional match and signify a pattern that may or may not be found in the expression:
```shell
echo '123!@#"* one_two THREE' | grep -E '3![a-z]+'
```
The above matches nothing, because we don’t have a '3!' followed by letters. However, the following will match '3!' because asterisk makes `[a-z]` optional (matching zero, one, or more times):
```shell
echo '123!@#"* one_two THREE' | grep -E '3![a-z]*'
```
### A side note on globbing vs. regex
It is important to remember that regular expressions are distinct from pattern matching (also known as **_globbing_**) when looking for filenames in the shell. For example, you might have noticed that the meaning of asterisk is different: when expanding filenames in the shell it means 'any character any number of times', whereas in regular expressions it is meaningless when used by itself and has to be preceded by an item (character or character class) to be matched. Other metacharacters used by the command line, such as the pipe `|`, also have different meanings in regex.
### Alternation
Character sets allow you to match alternative characters. With **_alternation_** you can match any number of alternative characters or even text patterns. You can separate them by the familiar vertical bar or pipe `|`. If you want your alternatives to be embedded within a larger expression, you also need to define their scope by parentheses. You can specify any number of alternative matches:
```shell
grep -E 'mol(d|t|e)' /usr/share/dict/words
```
The above is equivalent to:
```shell
grep -E 'mol[etd]' /usr/share/dict/words
```
We can also imagine more sophisticated alternatives:
```shell
grep -Eo 'anic[0-9-]+|inbio([a-z]+)?[0-9]+' ~/Sandbox/ants.txt
```
The above looks for anything that looks like the pattern to the left of the pipe, or anything that matches the pattern to the right of it.
### Shorthand character classes
There are other ways you can specify certain classes. Preceding certain letters with a backslash is a common way to do so. `\w` will match any alphanumeric character and underscores, (think 'w' for word) while uppercase `\W` will match any other character, but not blank characters such as spaces or tabs:
```shell
echo '123!@#"* one_two THREE' | grep -E '\w'
echo '123!@#"* one_two THREE' | grep -E '\W'
```
We can see then that in the above `\w` is the same as specifying a character class `[A-Za-z_]`.
To match a blank character, space or tab, you can use `\s`. Again, the opposite (non-blank) is the uppercase `\S`.
There is another way to use character classes, called 'POSIX bracket expressions' or 'POSIX character classes'. 'POSIX' is a family of standards that Unix operating systems should conform to, and it includes a regex standard. POSIX classes can be useful, as they should work with most tools and operating systems. You can read about them [here](http://www.regular-expressions.info/posixbrackets.html).
### Backreferences
In regular expressions you can signify a pattern enclosed by parentheses using a shorthand called backreference. These are written as a backslash followed by a number; the numbers refer to open parentheses. For example, in expression `(^[a-z]{4})(ing)`, `\1` stands for a four-letter part of a word starting at the beginning of a line, and `\2` stands for `ing`. Backreferences become extremely useful when we want to modify the text, for example substitute or flip matches.
### Escaping characters in regex
Remember that within a character class, or in pattern enclosed within square brackets, metacharacters other than caret `^` and dash `-` are interpreted literally. If you want to be able to match literal strings that mean something to regular expression, such as `+`, you need to precede it with a backslash:
```shell
echo '\1\w[a-z]+' | grep -E '\1\w[a-z]+'
```
The above won’t work because ‘grep’ tries to interpret all these characters as special. You can escape each metacharacter with a backslash to make it work. Think what special characters are present in this expression and see if you can figure out how to escape each.
You code should look like this:
```shell
echo '\1\w[a-z]+' | grep -E '\\1\\w\[a-z\]\+'
```
### Matching newline
In text files, each line is separated from the next using the so-called newline or line break. Being able to match a newline is very useful, because you can write patterns that span across multiple lines. A confusing thing about newlines is that different operating systems handle them in different ways. Simplifying, you can match a newline in text generated on most Unix-like systems (including Linux, Ubuntu, Mac OS) with `\n` and for text written under Windows you need to use `\n\r`. You can read more about the various types of newlines on [Wikipedia](http://en.wikipedia.org/wiki/Newline).

The way that `grep` processes text is not compatible with matching newline characters, but you can do this in TextWrangler or EditPad. I encourage you to install those text editors and try playing around with regular expressions in your own text.


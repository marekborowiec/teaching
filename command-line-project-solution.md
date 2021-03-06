# Project 1 solution
## Question 1 
We encountered a variety of tools to look at file content. In this case, `head`, `less` and `cut` commands are particularly useful. For example, we can use `head -1` to determine what columns there in the data and `cut` to extract just the column(s) of interest.

## Question 2
There are many ways of writing a complex regex like this. You may first want to look for elements common in all patterns. In our case we see that every pattern starts with a ‘P’ and has a string of integers in it. Focusing on the first five patterns we could try:
```shell
grep -oE 'P[SWC# ]+[0-9]+' ~/Sandbox/ants.txt
```
Unfortunately, this proves too general: we match many unwanted patterns, such as 'P 1510' or 'P 25'. 
Another approach could be to move ‘PSW’ before the character class and alternate it with a pattern matching 'Ward Acc.':
```shell
grep -oE '(PSW([C# ]+)?|P\.(S\. )?Ward Acc\. ?)[0-9-]+' ~/Sandbox/ants.txt
```
Note that by adding a dash `-` as the last character of the character class, we made it match digits and/or dashes. You can check how this is handling those 'Ward Acc.' matches by piping the output to `grep "Ward"`. Another way of accounting for the trailing characters after the main string of digits would be to include a shorthand `\S` that matches anything that is not a blank character:
```shell
grep -oE '(PSW([C# ]+)?|P\.(S\. )?Ward Acc\. ?)[0-9]+(\S+)?' ~/Sandbox/ants.txt
```
There are many ways of writing a regular expression that will accomplish the same goal. Usually we need to consider trade-offs between clarity, robustness, and length of the expression. I think the following solution is somewhat easier to understand than what we came up with above:
```shell
grep -oE '(PSW( |C |C #|C#)?|P\.(S\. )?Ward Acc\. ?)[0-9]+(\S+)?' ~/Sandbox/ants.txt
```
It seems more explicit and easy to understand what the above is matching immediately after 'PSW', where we have a simple alternation with four possibilities of a match. In our example both solutions return the same number of matches, but they are not exactly equivalent. For example, the one using character class following 'PSW' will match strings like 'PSW       12345' or 'PSW#####12345', while the one using alternation won't. Can you explain why?
## Question 3
You can use `grep -c` or pipe your `grep -E` results into `wc -l`. The first option counts lines that match the pattern. `wc` will count any line that was passed as input, and so the result will depend on what the input was. With `grep -Eo` you will print each occurrence of a match on a separate line, and if there were lines with more than one match, piping this to `wc` will give you a higher count:
```shell
grep -cE '(PSW([C# ]+)?|P\.(S\. )?Ward Acc\. ?)[0-9-]+' ants.txt
1409
```
Versus:
```shell
grep -oE '(PSW([C# ]+)?|P\.(S\. )?Ward Acc\. ?)[0-9-]+' ants.txt | wc -l
1433
```
This will be true even if you combine options `-o` and `-c` in `grep`: the latter will always count lines that contained a match. This is perhaps a good example of how understanding the subtleties of how each option and command works can matter:
```shell
grep -ocE '(PSW([C# ]+)?|P\.(S\. )?Ward Acc\. ?)[0-9-]+' ants.txt
1409
```

# Project 1: command line and regex
This project will make you put the skills you gained over in the command line tutorial sections 1 through 3.

You will need the `ants.txt` file in your `Sandbox` folder. If you cannot find it or if you have accidentally deleted it, you can find links to them in the README file.

A common task when working with spreadsheets from public data bases is to make them conform to a certain format or standardize some data present within it.
In our file there is a field called 'CollectionCode' that contains codes for unique collection events (no need to worry about what that means!). We are interesting in looking at all the 1000+ collection codes that were assigned by my advisor, Phil Ward. The standard for his collection codes should follow a simple formula: 'PSW' followed by a multi-digit number, occasionally with additional numbers or other characters at the end, separated by period '.' or dash '-'.
This is the most common way these collection codes are represented in our file, but unfortunately some have been entered in different formats:

`PSW13860`
`PSW 8027-11`
`PSWC 15335`
`PSWC #15335`
`PSWC#15723`
`P.S. Ward Acc.1017`
`P.Ward Acc. 1812`
`P.S. Ward Acc. 1144`

This means that searching for `PSW[0-9]+` won't work for all codes. We would like to standardize all references to those codes so that they follow the same format as the first example above. Eventually, we would like to have 'PSW 8027-11' read as 'PSW8027-11' (no space between 'PSW' and the digits), and 'P.Ward Acc. 1812' read as 'PSW1812'. The first step is to match all these variable formats. What would your `grep -E` regex to match the alternatives look like? Note that the number portion of the collection code will be different for each record. In this exercise all you need to know is that you are looking for a pattern matching any of the possibilities above (and no other text, such as 'PSWC' by itself: hint!), but you should be able to demonstrate that you know how to look at the actual data. Try to answer the following by typing your code under each question:

1) How would you go about looking at the data before tackling the regular expression? What commands would you use?

2) What would your `grep -E` regex to match the alternative codes look like? Hints: an effective expression would use alternation, optional matching, escaping characters within the expression, and character classes. You can try to also match any string following optional `-` or `.` sometimes present after the first set of digits (e.g. '8027-11') but you don't need to. The blank characters are all spaces.

3) How would you check how many matches your regex finds? The solution should be matching 1409 lines where these codes occur.

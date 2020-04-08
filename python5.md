# Review of command line input with sys.argv
We briefly reviewed how `sys.argv` works. In order to use that function, you need to import module `sys` by adding `import sys` at the beginning of your Python program. Then, you can use it to get a list of arguments you give on the command line:
```python
# argv.py
import sys

list_of_arguments = sys.argv
print(list_of_arguments)
```
If you call this program as `python3 argv.py yes no 1` from command line and hit return, it will see a list `['argv.py', 'yes', 'no', '1']`. Note that you don't *need* to make a variable for list of arguments, you could simply do `print(sys.argv)` directly for the same purpose but it will help you and others reading your code to use meaningful variable names.
Once you define some variables based on indices of `sys.argv` list, for example:
```python

in_file_name = sys.argv[1]
out_file_name - sys.argv[2]
match_word = sys.argv[3]
```
You need to call your script with *all* of these arguments (3 in this case) or you will be trying to access non-existent list indices and get `IndexError: list index out of range`.
# Tuples
We have mentioned tuples a couple of times in passing. Tuples in Python are a type of data very similar to lists. You also define them like a list, but use parentheses instead of square brackets:
```python
my_tuple = (1, "two", 3.0)
my_list = [1, "two", 3.0]
```
The main difference here is that tuples are a *immutable* data type, meaning they cannot be modified after construction. For example, you can modify a list in place by assigning a new value to an index:
```python
my_list[0] = 55
print(my_list)
output>>> [55, "two", 3.0]
```
Here we didn't create a new list, we just changed a value inside an existing list object. You can still access individual values of a tuple with indices, like `my_tuple[0]` but you cannot assign a new value:
```python
my_tuple[0] = 55
output>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
Tuples also lack methods that can modify them in place, such as `.append()` which we used for lists. Every time you want to modify a tuple, you need to create a new tuple object. The reason for immutable data types is, in short, to make sure the object you made will always stay the same. This may be important in some applications.
# Format strings
Earlier we learned about string concatenation using `+` signs. This works okay for many simple purposes but there is a more elegant and flexible way to work with strings, the built-in string method `.format()`. We won't cover it in great detail because you completed an online tutorial the explained most of its capacitis. The thing to remember here is that you can use it to combine strings and easily plug in variables or even list elements into strings as long as these variables are string objects themselves. We will be using it again next week.
# More functions
In the past weeks we created a short program that 1) read input text file, 2) searched for lines in that file that matched some characters and 3) printed those lines into a new file. The first few lines defined variables that will be defined by input on command line:
```python
#! /usr/bin/env python3

import sys

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]
match_word = sys.argv[3]

```
It then defines a function that opens the input file and returns a list of lines in that file:
```python
def get_input_file_lines(in_fn):
	# create file object using string of input file name 
	in_file = open(in_fn, "r")
	# use method to get list of lines from file object
	in_file_lines = in_file.readlidefnes()
	# close input file
	in_file.close()
	# return the list of lines
	return in_file_lines
```
A function that gets only lines matching a pattern:
```python
def get_matching_lines(list_of_lines, pattern):
	# define empty list for matching lines
	matches = []
	# for each line in list of lines
	for line in list_of_lines:
		# check if pattern was found
		if pattern in line:
			# if it is found, grow list of matching lines
			matches.append(line)
	# return new list containing only matching lines 
	return matches
```
And one that writes a new file:
```python
def write_matching_lines(matching_lines, out_file_name):
	# create new file object for output file in "write" mode
	out_file = open(out_file_name, 'w')
	# because we use .write() method later, we need to convert
	# list of lines into a single string first 
	output = ''.join(matching_lines)
	# write a big string with all lines all at once
	out_file.write(output)
	# close output file
	out_file.close()
```
Followed by three lines that call these functions"
```python
# function calls
lines = get_input_file_lines(in_file_name)
matches = get_matching_lines(lines, match_word)
write_matching_lines(matches, out_file_name)
```
Today we want to add some other functionality, namely being able to work with individual columns of data, not just lines. We can take advantage of our knowledge that columns in our file `ants-na.txt` are separated by the `tab` character. We also know that our file has a header, the first line that contains information about what each column represents. We could look at it using the command line tool `head -1` but because there are so many fields it is hard to see what is going on. We would instead like to know what index we could assign to a given column. For that we need to first come up with some code to split each individual line into fields using the `tab` separator. We can do it by applying the string method `.split('\t')` to our line, which returns a list of stings separated at places where the character in the argument occurred:
```python
list_of_columns = line.split('\t')
```
We can wrap this into a neat function:
```python
def split_line_into_columns(line):
	# strip line (string) of unnecessary newline characters,
	# then split line at tab characters
	# and put the results in a list
	list_of_columns = line.strip('\n').split('\t')
	# return the list of split fields / columns
	return list_of_columns
```
Now we want to also know the index of each column and print it in a way that is visually easy to interpret. We can make another function that will take use of column splitting specifically for the purpose of printing header fields, line by line, with corresponding indices:
```python
def print_header_indices(line):
	# split line into columns
	list_of_columns = split_line_into_columns(line)
	# for each print column contents: index
	for index, column in enumerate(list_of_columns):
		print('{}:{}'.format(column, index))
```
Now we can use this function by modifying our `get_matching_lines()` function to also print header indices:
```python
def get_matching_lines(list_of_lines, pattern):
	matches = []
	# take first line of file to process
	print_header_indices(list_of_lines[0])
	for line in list_of_lines:
		if pattern in line:
			matches.append(line)
	return matches
```
This gave us output that is much more informative. Now we can go ahead and start selecting columns that are relevant to us. We can do this in a separate function or keep modifying our `split_line_into_columns()` function.
```python
def split_line_into_columns(line):
	list_of_columns = line.strip('\n').split('\t')
	# access different columns by index
	lat = list_of_columns[21]
	lon = list_of_columns[22]
	species = list_of_columns[9]
	locality = list_of_columns[16]
	elevation = list_of_columns[25]
	# pretty-print information we're interested in 
	print('Species:{} Locality:{} Lat:{} Long:{} Elevation:{}'.format(
		species, locality, lat, lon, elevation
		))
	return list_of_columns
```
You can now call this function at the end of the script on either all lines in a loop, or just the lines that match your pattern, or you can insert the call to it into `get_matching_lines().` Possibilities are endless!
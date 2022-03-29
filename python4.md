
### Writing files
Now that we have some content that we extracted from our file, we can save it in another file. Writing files in Python is very similar to opening them, as you also need to create a file object with `open()`, write to that object with `.write()`, and close the output file with `.close()`.

We already learned that the function `open()` takes a file name as the argument, but it can actually take a second argument that determines its action. By default, the second argument is `"r"`, for "read" and that is why we didn't have to specify when we were getting file contents. Our line
```python
# create file object
in_file = open("ants-na.txt")
```
is equivalent to
```python
# create file object
in_file = open("ants-na.txt", "r")
```
There are two other common ways in which `open()` is used:
```python
# this will create new file or overwrite if name exists 
out_file = open("new_file.txt", "w")
# this will append text to end of existing file
out_file = open("old_file.txt", "a")
```
Now that you have a file object for your output, you need to `.write()` its contents, much like you read them in a case of getting input:
```python
contents = "hello world!"
out_file.write(contents)
```
Write takes only strings as input, so you need to first convert whatever you want to write (integers, list, etc.) into a string. Unfortunately, if you convert a list, for example, to a string using the familiar `str()` function, it will contain all the unnecessary special characters used in the list, including quotes, commas, and square brackets. A more elegant way of joining list elements that are themselves strings is done using the `.join()` method for strings. To join your list use:
```python
# join list into string
some_list = ['one', '2', 'three']
output = ' '.join(some_list)
```
In `.join()` you apply the function on a separator and supply the list or other sequence as an argument. You can join elements in your list using any separator, which in the example above is `' '` or a single space. You can use any character or string as the delimiter for `.join()`.  

Finally, you want to close your `out_file`:
```python
# close output file
out_file.close()
``` 
## Importing modules and using command line arguments
Just as you can supply arguments to the command (e.g. file name, number of lines printed), you can make your program take arguments while it's being run from the command line. This makes your program more flexible. Before we are ready to work with the arguments, however, we need to know what modules are all about.
### Modules in Python
Multiple tools that are common in every Python program, such as functions and methods working on strings and integers, are available by default in any Python program. These functions and methods are understood by the interpreter because every time you run a program, the code that does the heavy lifting behind the functions is loaded into the interpreter along with your script. For the reasons of efficiency, this core of code imported by default is limited, but Python still gives you access to more specialized tools if you need them. This is where the **__modules__** come in. Python is installed with a series of code chunks that can be imported into your program and allow you to use additional functions and methods. You can import modules by putting `import name_of_module` at the beginning of your script. For example, to use the Python regular expression tools, you need to insert this statement somewhere near the beginning of your script:
```python
import re
```
### Command line arguments in Python
In order for your script to understand command line arguments, you need the `sys` module. The `sys` module is a collection of methods that interact with system-specific variables on your computer.
Let's open our `file_input.py` script and import this module at the beginning, after the shebang line but before you create your file object:
```python
#! /usr/bin/env python3

# file_input.py by Your Name

import sys

# create file object
in_file = open("ants-na.txt")
```
Now you can use the `argv` method that is available from the `sys` module. It parses command line arguments and allows you to store them in variables. The way that arguments are separated is always by spaces on the command line and you can access the arguments through `sys.argv[index]`. The argument at index `0` is always your script name (in our example this will be `file_input.py`), but the arguments starting at index `1` can be assigned to variables. Let's try to make our script read file name from the command line:
```python
import sys

# define the first argument as file name
in_file_name = sys.argv[1]
# create file object
in_file = open(in_file_name) # <=== we substitute 'ants-na.txt' with the argument
```
Now if we try to simply run our script as before, it will throw an error:
```shell
python3 file_input.py
Traceback (most recent call last):
  File "./file_input.py", line 8, in <module>
    file_name = sys.argv[1]
IndexError: list index out of range
```
It's because the script now expects one additional argument following the script name. Let's try again:
```shell
python3 file_input.py ants-na.txt
```
The above will work and have the same effect as our old script in which the name of the input file was **__hardcoded__** or, in other words, fixed by being defined inside the program. You can see how this form of input gives your programs more flexibility. You don't need to change the source code every time you want to apply the same task to a different file.
You can add as many command line arguments as you like. Try to modify your code so that it takes a second argument defining the name of the ouput file. That is, instead of printing the results to `Moscow_matches.txt`, your program should write a file whose name is the second argument (`sys.argv[2]`) given to your script.
Your final script from the tutorial above could look like this:
```python
#! /usr/bin/env python3

# file_input.py by Your Name

import sys

# define the first argument as file name
in_file_name = sys.argv[1]
# define the second argument as output file name
out_file_name = sys.argv[2]
# create file object
in_file = open(in_file_name)
# read in file contents as list of strings (lines)
in_file_list = in_file.readlines()
# what to look for
match = "Moscow"
# empty list where matching lines will be appended
matching_lines = []
 
# loop over all elements in list
for line in in_file_list:
    # if line contains match, append it to matching_lines
    if match in line:
        matching_lines.append(line)

# print list with matching lines
print(matching_lines)
# join list into string
output = ''.join(matching_lines)
# close input file
in_file.close()
# open output file
out_file = open(out_file_name, "w")
# write matching lines to output file
out_file.write(output)
# close output file
out_file.close()
```
### Writing your own Python functions
You encountered several functions available in the "standard Python library", such as `len()`, `int()`, `open()`. What are functions and why do they exist? The why seems pretty obvious: these functions enable basic operations someone writing code would want to perform on their data. And why would you want to write your own functions? There are many advantages. Functions allow you to re-use code in a script without having to copy and paste, which is also useful because if you need to modify something, you just need to do it once. Breaking code up into functions also makes it easier to solve larger problems because it allows independent work on different functionalities. But what are these functions? There is nothing magical about them. All you have to do to make a function is to use special syntax similar to that of a loop:
```python
def do_awesome(arguments):
    # do amazing things
    return some_variable
```
Our code above used for reading, matching, and writing lines to a new file can be rewritten into functions. What could be our function(s)? We have different options. For example, we could write one function to read input from file, match lines we want it to, and write the file with matching lines. We could also split this code into multiple functions: one to read a file, second to find matching lines, and third to write the new file. Writing smaller functions is generally better because it makes the code more readable and your program is more flexible. Let's try to apply both approaches. 
To wrap most of the functionality of your script into one function you can simply do this:
```python
#! /usr/bin/env python3

# file_input.py by Your Name

import sys

# define the first argument as file name
in_file_name = sys.argv[1]
# define the second argument as output file name
out_file_name = sys.argv[2]

# define one, large function that does all the work 
def process_file(in_file_name, out_file_name):
    # create file object
    in_file = open(in_file_name)
    # read in file contents as list of strings (lines)
    in_file_list = in_file.readlines()
    # what to look for
    match = "Moscow"
    # empty list where matching lines will be appended
    matching_lines = []
     
    # loop over all elements in list
    for line in in_file_list:
        # if line contains match, append it to matching_lines
        if match in line:
            matching_lines.append(line)

    # print list with matching lines
    print(matching_lines)
    # join list into string
    output = ''.join(matching_lines)
    # close input file
    in_file.close()
    # open output file
    out_file = open(out_file_name, "w")
    # write matching lines to output file
    out_file.write(output)
    # close output file
    out_file.close()

process_file(in_file_name, out_file_name)
```
The difference between how this code runs is that it only defines a function but does not make any action. In order for this program to do anything you also need to call the function at the end with `process_file(in_file_name, out_file_name)`
Now consider code that splits the functionality into three different functions:
```python
#! /usr/bin/env python3

import sys

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]
match_word = sys.argv[3]

def get_input_file_lines(in_file_name):
    in_file = open(in_file_name, "r")
    # read in file contents as list of strings (lines)
    in_file_lines = in_file.readlines()
    in_file.close()
    return in_file_lines

def get_matching_lines(list_of_lines, match):
    # empty list where matching lines will be appended
    matching_lines = [] 
    # loop over all elements in list
    for line in list_of_lines:
        # if line contains match, append it to matching_lines
        if match in line:
            matching_lines.append(line)
    return matching_lines

def write_matching_lines(matching_lines, out_file_name):
    # join list into string
    output = ''.join(matching_lines)
    # open output file
    out_file = open(out_file_name, "w")
    # write matching lines to output file
    out_file.write(output)
    # close output file
    out_file.close()

lines = get_input_file_lines(in_file_name)
matches = get_matching_lines(lines, match_word)
write_matching_lines(matches, out_file_name)
```

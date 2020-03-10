# PYTHON PROGRAMMING PART 3

## Conditional statements
Sometimes we want certain action to be performed if a condition is met. This is where Boolean values and `if`, `else`, and `elif` statements come into play. Let's put to use an `if` statement inside a loop to check (five times) if a plant name is in the dictionary and print out the family it belongs to. We will use the function `input()` to get input from the program's user.
```python
# ask five times for a plant name
for i in range(3):
    # input asks for user input and saves it in a variable
    name = input("Please input a plant name:\n")
    # check if the name is in keys of dictionary
    # if evaluated to True, print a statement
    if name in taxonomy.keys():
        print(name + " belongs to the family " + taxonomy[name])
    # if the above returns False, print a different statement
    else:
        print("I'm sorry, the name wasn't found.")
```
Note how anything evaluated inside an `if` statement also has to be indented. 

We can use a `break` statement to break out of the loop if we want to ask only until a name is found:
```python
    if name in taxonomy.keys():
        print(name + " belongs to the family " + taxonomy[name])
        break                                                     # <=== added break statement
    # if the above returns False, print a different statement
    else:
        print("I'm sorry, the name wasn't found.")
```
You can use the `elif` statement (short for 'else if') to give more than two options to your loop. Let's also check for family names:
```python
    if name in taxonomy.keys():
        print(name + " belongs to the family " + taxonomy[name])
        break
    # print this if input is a family name
    elif name in taxonomy.values():                               # <=== added elif statement
        print(name + " is a family name. Please input a species name.") 
    # if the above returns False, print a different statement
    else:
        print("I'm sorry, the name wasn't found.")
```
Instead of the `if name in` statement we could have asked whether the input is not a part the list by using `if name not in`. `if`, `elif`, and `else` statements can also be combined with Boolean comparison operators (see table in the previous tutorial).

## `while` loops
Another kind of loop that is worth mentioning is a `while` loop. This loop runs until a condition is false:
```python
bytes = 2
while bytes < 8000:
    print(bytes * 2)
    bytes = bytes * 2 
```
In this loop we initiated a variable with the integer 2, then put a `while` statement that returns `True` while the value of `bytes` is less than 8000. We then increase the value of bytes by multiplying it by 2. Once `bytes` is more than 8000, the loop exits.

It is relatively easy to create a `while` loop that always evaluates to `True` and therefore never stops. If you create a loop like that, you can interrupt the program from the command line with `Ctrl + C`. For example, we can change the value of `bytes` and `while` condition, we can easily create an infinite loop:
```python
bytes = 512
while bytes > 500:
    print(bytes * 2)
    bytes = bytes * 2
```
The computer starts printing very big numbers really quickly and you need to interrupt. This is because when the `while` loop with this condition and starting value would never return `False`.

## User input
While discussing loops and flow control we encountered the `input()` function that made our program prompt for user input that can be stored as a variable. Today we will learn more about ways in which your program can take input by reading from files and understanding command line arguments.

## Reading from and writing to files
Much of the time you want your script to perform some operations on contents of a text file, such as the DNA sequence alignment or specimen data files we worked with on the command line. 

Python offers a relatively simple way of getting file contents that involves three steps: 

1) opening the file and getting a file object, 
2) reading in its contents, and 
3) closing the file.

### Getting a file object
Let's open our `Gedit` text editor, put a shebang followed by the directory to our Python3 interpreter,
```python
#! /usr/bin/env python3
```
and save the file as `file_input.py` in `Sandbox`. You can add a comment that tells you what file you are currently looking at:
```python
#! /usr/bin/env python3

# file_input.py by Your Name
```
The first step to read in the file contents and get a file object is accomplished with the function `open()`, to which you pass the name of the input file. You should store the file object, that is the result of calling `open()`, in a variable. Let's try opening the `ants.txt` file we have in our `Sandbox` directory. You can supply an absolute path to the function or just the name of the file if you know you will be calling your script from the same directory as the input file. Add the following to your script:
```python
# create file object
in_file = open("ants.txt")
```
The above will call `open()` on a file `ants.txt` and store a file object in the `in_file` variable. Remember that because we are only giving the file name and not it's absolute path, it is important to run this script from the same directory as the input file. 

### Reading file contents and closing
The file object created by `open()` has its own methods, just like string, integer, or Boolean value objects. Python gives you more than one option to read in text file contents. You can store them as a single long string with each newline represented by `\n` or you can read lines into a list of lines. Reading into a string is accomplished with `.read()` and reading into a list of lines is accomplished with `.readlines()`. Let's read in the file contents as a string and loop over its elements:
```python
# read in file contents as string
in_file_string = in_file.read()

# loop over each character in string
for i in in_file_string:
    print(i)

# close file
in_file.close()
```
It is good practice to close the file object using the `.close()` method after you are done with it. This potentially helps free resources and protects your program from certain unwanted behaviors. Save and run your script. You should see that the loop is printing one by one every character in the file; you can interrupt it with `Ctrl + C`. This is the behavior we saw earlier when looping over strings. The `.read()` method is useful when you don't want to repeat operations on each line of a file but rather perform some function that applies to the file as a whole.

An alternative to `.read()` is the `.readlines` method, returning a list of lines in a file, each of which is a string. Comment out the `in_file_string` variable because it's impossible to read data from a file object more than once and add a new variable `in_file_list` that uses `.readlines()`. You can comment out or the string loop from the previous example so that your program uses the newly created list of lines to loop over instead:
```python
# read in file contents as string
#in_file_string = in_file.read()
# read in file contents as list of strings (lines)
in_file_list = in_file.readlines()

# loop over all characters in string
#for i in in_file_string:
#    print(i)

# loop over all elements in list
for line in in_file_list:
    print(i)

in_file.close()
```
### Putting file input to work
Now that you know the basics of opening and closing files, you can use that knowledge to perform some simple operations on the file contents. Let's try to use our knowledge of the for loop to print every line that contains the text `Yolo` in it. Modify your loop to read:
```python
# loop over all elements in list
for line in in_file_list:
    # if line contains 'Yolo', print it
    if "Yolo" in line:
        print(line)
```
This will start printing all the lines that match that particular string. How would you modify the code so that when a line does not match, the program would print "Line did not match"?

Your code could look like this:
```python
# loop over all elements in list
for line in in_file_list:
    # if line contains 'Yolo', print it
    if "Yolo" in line:
        print(line)
    else:
        print("Line did not match")
```
In this example the vast majority of lines do not match "Yolo". If you run it you will see thousands of "Line did not match" messages printed to your screen, but the purpose is to practice some more flow control.

You could further modify this code to assign the strings into variables before use. Generally it is good practice to use variables as much as you can, especially if you ever anticipate using a particular value more than once in your code. If you later need to change that value, you just need to reassign the original variable instead of going through the many lines of code and tweaking each line on which the value is used to reflect the change:
```python
# what to look for
match = "Yolo"
# what to print if match not found
message = "Line did not match"

# loop over all elements in list
for line in in_file_list:
    # if line contains match, print it
    if match in line:
        print(line)
    else:
        print(message)
```
Let's say you want to store the lines that matched in the previous example in a list. You know the `.append()` method that you could use to append the every time it matches in the loop. However, first you need to create an empty list outside of the loop to append values to it inside the loop. Try to fill in code inside the loop yourself:
```python
# what to look for
match = "Yolo"
# what to print if match not found
message = "Line did not match"
# empty list where matching lines will be appended
matching_lines = []
 
# loop over all elements in list
for line in in_file_list:
    # if line contains match, append it to matching_lines
    ...
    ...
```
The code inside your `for` loop should look like this:
```python
# loop over all elements in list
for line in in_file_list:
    # if line contains match, append it to matching_lines
    if match in line:
        matching_lines.append(line)
```
You can print this list to verify that the code works. Add the following after the loop:
```python
# print list with matching lines
print(matching_lines)
```
Remember that this line has no indent because we are going to print the list only after the loop has finished. If you place it within an indented block for the `for` loop, it will print the list at every run of the loop. Printing output after you introduced a new piece of code is a way of checking if the program still works as expected.

Your script should now look like this:
 ```python
#! /usr/bin/env python3

# file_input.py by Your Name

# create file object
in_file = open("ants.txt")
# read in file contents as list of strings (lines)
in_file_list = in_file.readlines()
# what to look for
match = "Yolo"
# what to print if match not found
message = "Line did not match"
# empty list where matching lines will be appended
matching_lines = []
 
# loop over all elements in list
for line in in_file_list:
    # if line contains match, append it to matching_lines
    if match in line:
        matching_lines.append(line)

# print list with matching lines
print(matching_lines)

# close input file
in_file.close()
```

### Writing files
Now that we have some content that we extracted from our file, we can save it in another file. Writing files in Python is very similar to opening them, as you also need to create a file object with `open()`, write to that object with `.write()`, and close the output file with `.close()`.

We already learned that the function `open()` takes a file name as the argument, but it can actually take a second argument that determines its action. By default, the second argument is `"r"`, for "read" and that is why we didn't have to specify when we were getting file contents. Our line
```python
# create file object
in_file = open("ants.txt")
```
is equivalent to
```python
# create file object
in_file = open("ants.txt", "r")
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
out_file.write(contents)
```
Note that here you don't need to save the written contents in a new variable; the `out_file` object is populated with text in place. Write takes only strings as input, so you need to first convert your list of matches into a string. Unfortunately, if you convert a list to a string using the familiar `str()` function, it will contain all the unnecessary special characters used in the list, including quotes, commas, and square brackets. A more elegant way of joining list elements that are themselves strings is done using the `.join()` method. The use of this method is somewhat different from other functions that we used so far. To join your list use:
```python
# join list into string
output = ''.join(matching_lines)
```
In `.join()` you apply the function on a separator and supply the list or other sequence as an argument. You can join elements in your list using any separator, which in the example above is `''` or none. This is fine in our case since the strings in our list already have `\n` newline characters at the end, so the output will be properly formatted. However, you can use any character or string as the delimiter for `.join()`.  

Finally, you want to close your `out_file`:
```python
# close output file
out_file.close()
``` 
Try saving the contents of your list of matching lines into a new file called "Yolo_matches.txt". 

The last several lines of your code should now look like this:
```python
# print list with matching lines
print(matching_lines)
# join list into string
output = ''.join(matching_lines)
# close input file
in_file.close()
# open output file
out_file = open("Yolo_matches.txt", "w")
# write matching lines to output file
out_file.write(output)
# close output file
out_file.close()
```
You can turn off printing of the list by commenting it out or move the print statement after joining the list to see how it looks before it's written to the ouput file. Take a look at your newly created `Yolo_matches.txt` file, either using the command line or just opening it in `Gedit`.
## Importing modules and using command line arguments
Just as you can supply arguments to the Unix command (e.g. file name, number of lines printed), you can make your program take arguments while it's being run from the command line. This makes your program more flexible. Before we are ready to work with the arguments, however, we need to know what modules are all about.
### Modules in Python
Multiple tools that are common in every Python program, such as functions and methods working on strings and integers, are available by default in any Python program. These functions and methods are understood by the interpreter because every time you run a program, the code that does the heavy lifting behind the functions is loaded into the interpreter along with your script. For the reasons of efficiency, this core of code imported by default is limited, but Python still gives you access to more specialized tools if you need them. This is where **__modules__** come in. Python is installed with a series of code chunks that can be imported into your program and allow you to use additional functions and methods. You can import modules by putting `import name_of_module` at the beginning of your script. For example, to use the Python regular expression tools, you need to insert this statement somewhere near the beginning of your script:
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
in_file = open("ants.txt")
```
Now you can use the `argv` method that is available from the `sys` module. It parses command line arguments and allows you to store them in variables. The way that arguments are separated is always by spaces on the command line and you can access the arguments through `sys.argv[index]`. The argument at index `0` is always your script name (in our example this will be `file_input.py`), but the arguments starting at index `1` can be assigned to variables. Let's try to make our script read file name from the command line:
```python
import sys

# define the first argument as file name
file_name = sys.argv[1]
# create file object
in_file = open(file_name) # <=== we substitute 'ants.txt' with the argument
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
python3 file_input.py ants.txt
```
The above will work and have the same effect as our old script in which the name of the input file was **__hardcoded__** or, in other words, fixed by being defined inside the program. You can see how this form of input gives your programs more flexibility. You don't need to change the source code every time you want to apply the same task to a different file.

You can add as many command line arguments as you like. Try to modify your code so that it takes a second argument defining the name of the ouput file. That is, instead of printing the results to `Yolo_matches.txt`, your program should write a file whose name is the second argument (`sys.argv[2]`) given to your script.

Your final script from the tutorial above could look like this:

```python
#! /usr/bin/env python3

# file_input.py by Your Name

import sys

# define the first argument as file name
file_name = sys.argv[1]
# define the second argument as output file name
out_file_name = sys.argv[2]
# create file object
in_file = open(file_name)
# read in file contents as list of strings (lines)
in_file_list = in_file.readlines()
# what to look for
match = "Yolo"
# what to print if match not found
message = "Line did not match"
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


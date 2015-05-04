# PYTHON PROGRAMMING

## What is Python and why learn it?
All programming languages are formal sets of instructions that are used to control the behavior of a computer. These instructions are commonly referred to as code. The code is just plain text that people can write and understand, but which can also be translated into a language that computer processor can directly understand. Under the hood, every application that you use to interact with your computer such as your text editor, operating system, or favorite computer game was written as code.

Python is a general-purpose language that is gaining popularity as the language of choice for beginner scientific programmers: it is relatively easy to learn, has an ever-growing base of resources and a large community of users. Popular programs written in Python include Dropbox, the interface of Youtube, Instagram, and many Google apps. Python programs can be very concise and often have fewer lines of code than similar programs in other languages. Python is also rapidly gaining ground in bioinformatics and biology, slowly replacing another popular general-use language called "Perl". The Python community is currently transitioning from an older version of the language, Python 2, into Python version 3. There are several differences between the two, and here we will focus on Python 3.

Learning the basics of a programming language gives you flexibility in analyzing and interacting with your data and empowers you to harness the awesome power of your computer. In the coming five meetings we will learn the basic building blocks of a Python program. There are already excellent resources out there aimed specifically at teching Python to biologists and I encourage you to check out those mentioned on our Resources page.   

## Python's interactive interpreter
Your Python code can be a simple text file or it can be entered on an interactive interpreter that comes with the language. The interpreter shows you a prompt when it is wating for input and has the interface similar to the command line. The instructions you type in it are read and translated for the computer on the go. We will start working with the interpreter, in later sessions moving to a text file to save our code. Let’s enter the interpreter by typing `python3`  and pressing Return. You should see something like this:
```Python
Python 3.4.2 (default, Oct  8 2014, 13:18:07) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The prompt has changed its appearance to the three greater-than signs `>>>`. The first thing we will learn in Python is to print some text. Type:
```Python
>>> print("Work is for people who don't know how to code")
```
Again, just as in the shell, correct spelling, parentheses, and quotes are important. The `print()` statement represents a function that prints whatever we put in between the parentheses to the screen.

## Variables
A very important basic concept in programming is that of a variable. Variables are names that represent some other entities. You can think of a variable as a kind of box that stores data. A simple example would be to store some text in a variable and then print it:
```Python
>>> greeting = "Hello!"
>>> print(greeting)
```
There are several things to discuss here. First, there are some rules that govern variable names. They can only be composed of letters, numbers, and underscores. They cannot start with a number, and cannot be certain words that have special meanings, for example "True" or "False". The recommended practice is to name variables in all lowercase, with words separated by an underscore in multi-word names: "my_variable", "number_of_sequences" etc. In the code above, we put the value `Hello!` into a variable called `greeting` by using the equal `=` sign. This is how values are **_assigned_** to variables.

## Data types: strings
Python recognizes various types of data. This is because certain operations make sense for one kind of data but not others. For example, division and substraction are great for numbers but are not applicable to text. As biologists, we are often interested in manipulating data that programmers call **__strings__**. Strings are just sequences of characters and are a good representation for, for example, DNA or amino acid sequence data. You can of strings as plain text. In Python, we let the computer know that the text we are writing is a string by enclosing it in quotes (double or single). In the example above, we used the string `Hello!`. Python has certain functions that can be applied to the most common data types, and we will begin with exploring the ones available for strings.
You can **_concatenate_** (put together) strings by using the `+` operator:
```Python
>>> my_intron = "ATATTT"
>>> print(my_intron)
ATATTT
>>> my_exon = "GCGCCC"
>>> my_sequence = my_intron + my_exon
>>> print(my_sequence)
ATATTTGCGCCC
```
In the above we created two variables containing strings, that we subsequently concatenated and assigned to a third variable. You can combine strings that are not assigned into variables and those that are by using the same syntax:
```Python
>>> print("My sequence is: " + my_sequence)
My sequence is: ATATTTGCGCCC
```
Python has built-in functions that are useful for manipulating strings. Python functions can be used on different data types, and a simple function that is often used with strings is `len()`:
```Python
>>> len(my_sequence)
12
```
Later we will see `len()` applied to other data types.
You can also do operations that are specific to a particular data type. These are called **__methods__**, and are applied slightly differently from functions. We use them by first assigning our data to a variable and then following the variable name by a period `.`, followed by the method's name and parentheses:
```Python
>>> print(my_sequence.lower())
atatttgcgccc
>>> print(my_sequence)
ATATTTGCGCCC
```
In the above we applied the method `lower()` to our `my_sequence` variable and the `print()` function on the results of that method. Note that the contents of our variable `my_sequence` were not changed. We can change the contents, or **__overwrite__** a variable by assigning a new value to its name:
```Python
>>> my_sequence = my_sequence.lower()
>>> print(my_sequence)
atatttgcgccc
```
Strings have many methods and function that can be applied to them. You can find a list of all the methods in the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). It is likely that at first you will find those pages too technical, but as you learn more about how Python works they will become the first place to look for help when working on a problem. Let's try a couple more `str` methods.
Similarly to the `lower()` methods, there is a way to convert strings to uppercase:
```Python
>>> print(my_sequence)
atatttgcgccc
>>> print(my_sequence.upper())
ATATTTGCGCCC
```
You can also count the occurrence of a character or a substring in a string with `count()`:
```Python
>>> my_sequence.count('t')
4
>>> my_sequence.count('g')
2
>>> my_sequence.count('at')
2
>>> my_sequence.count('atatt')
1
>>> my_sequence.count('atattx')
0
```
And replace or translate characters using `replace()`. Replace has a bit more sophisticated interface, since you need to tell this function what characters to substitute. The general syntax is `replace(old, new)`:
```Python
>>> print(my_sequence)
atatttgcgccc
>>> print(my_sequence.replace("t", "g"))
agaggggcgccc
```
Again, remember that by using a function or method on a variable we are not changing its contents.

Remember the `count()` method? Let's try to print its output in a more informative way:
```Python
>>> print("There are " +  my_sequence.count('a') + " occurrences of 'a' in your sequence")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```
What is this about? We know that we can concatenate strings with the plus sign, so why does this not work? The error above tells us where something went wrong  (line 1 of <stdin>) and what was the error (TypeError: Can't convert 'int' object to str implicitly). The error tells us that there was a "int" object that could not be converted to a "str", the Python's shorthand for string. Turns out that the output of the `count()` method is not a string but a different data type, an **__integer__** or `int`. We will explain how Python handles number in a separate section, but for now its enough to say that integers are simply "whole" numbers, those without fractional components.
We can make the above work by converting the integer output of `count()` into a string. This is done using the `str()` function:
```Python
>>> print("There are " +  str(my_sequence.count('a')) + " occurrences of 'a' in your sequence")
There are 2 occurrences of 'a' in your sequence
```
We have now converted the output of `count()` into a string by enclosing the call to that function within parentheses of the `str()` function. We could make this a bit more readable by first assigning the string with our count to a variable. This will also enable us to reuse that value later without the need to type two nested functions:
```Python
>>> my_a_count = str(my_sequence.count('a'))
>>> print("There are " +  my_a_count + " occurrences of 'a' in your sequence")
There are 2 occurrences of 'a' in your sequence
``` 
We don't need to repeat the `str()` function here because `my_a_count` is already a string.
Try writing some code that counts all bases (A,C,G, and T) in the following string: "ATAATTGATAGTATGCTACC".
Your code cold look like this:
```Python3

```


## Data types: integers and floats

# PYTHON PROGRAMMING

## What is Python and why learn it?
All programming languages are formal sets of instructions that are used to control the behavior of a computer. These instructions are commonly referred to as code. The code is just plain text that people can write and understand, but which can also be translated into a language that computer processor can directly understand. Under the hood, every application that you use to interact with your computer such as your text editor, operating system, or favorite computer game was written as code. Short programs containing code are often called **_scripts_** and the activity of writing them is scrpting.

Python is a general-purpose language that is gaining popularity as the language of choice for beginner scientific programmers: it is relatively easy to learn, has an ever-growing base of resources and a large community of users. Popular programs written in Python include Dropbox, the interface of Youtube, Instagram, and many Google apps. Python programs can be very concise and often have fewer lines of code than similar programs in other languages. Python is also rapidly gaining ground in bioinformatics and biology, slowly replacing another popular general-use language called "Perl". The Python community is currently transitioning from an older version of the language, Python 2, into Python version 3. There are several differences between the two, and here we will focus on Python 3.

Learning the basics of a programming language gives you flexibility in analyzing and interacting with your data and empowers you to harness the awesome power of your computer. In the coming five meetings we will learn the basic building blocks of a Python program. There are already excellent resources out there aimed specifically at teching Python to biologists and I encourage you to check out those mentioned on our Resources page.   

## Python's interactive interpreter
Your Python code can be a simple text file or it can be entered on an interactive interpreter that comes with the language. The interpreter shows you a prompt when it is wating for input and has the interface similar to the command line. The instructions you type in it are read and translated for the computer on the go. We will start working with the interpreter, in later sessions moving to a text file to save our code. Let’s enter the interpreter by typing `python3`  and pressing `Return`. You should see something like this:
```python
Python 3.4.2 (default, Oct  8 2014, 13:18:07) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The prompt has changed its appearance to the three greater-than signs `>>>`. The first thing we will learn in Python is to print some text. Type:
```python
>>> # this is a conceited remark
>>> print("Work is for people who don't know how to code")
```
Anything that starts with `#` is ignored and acts as a comment. Comments are an important in scripting, as they can help the future you and others to understand your code. The `print()` statement represents a function that prints whatever we put in between the parentheses to the screen. As in the Bash shell, you can go back to the previous command by pressing the up arrow key. Again, just as in the shell, correct spelling, parentheses, and quotes are important. You can exit the interactive interpreter by typing `quit()`.

## Variables
A very important basic concept in programming is that of a **_variable_**. Variables are names given to some other entities. You can think of a variable as a kind of box that stores data. A simple example would be to store some text in a variable and then print it:
```python
>>> greeting = "Hello!"
>>> print(greeting)
```
There are several things to discuss here. First, there are certain rules you need to follow when giving names to variables. They can only be composed of letters, numbers, and underscores. They cannot start with a number and be certain words that have special meanings, for example `True` or `False`. The recommended practice is to name variables in all lowercase, with words separated by an underscore in multi-word names: `my_variable`, `number_of_sequences` etc. It is also good to name your variables in a way that conveys information. Names like `x` or `Bb` are not very useful and will make your code difficult to understand.

In the code above, we put the value `Hello!` into a variable called `greeting` by using the equal `=` sign. This is how values are **_assigned_** to variables.

## Data types: strings
Python recognizes various types of data. This is because certain operations make sense for one kind of data but not others. For example, division and substraction are great for numbers but are not applicable to text. As biologists, we are often interested in manipulating data that programmers call **_strings_**. Strings are just sequences of characters and are a good representation for, for example, DNA or amino acid sequence data. You can think of strings as plain, literal text. In Python, we let the computer know that the text we are writing is a string by enclosing it in quotes (double or single). In the example above, we used the string `Hello!`. 

Python has certain operations that can be applied to strings. 

You can **_concatenate_** (put together) strings by using the plus `+` operator:
```python
>>> my_intron = "ATATTT"
>>> print(my_intron)
ATATTT
>>> my_exon = "GCGCCC"
>>> my_sequence = my_intron + my_exon
>>> print(my_sequence)
ATATTTGCGCCC
```
In the above we created two variables containing strings, that we subsequently concatenated and assigned to a third variable. 

You can combine strings that are not assigned into variables and those that are by using the same syntax:
```python
>>> print("My sequence is: " + my_sequence)
My sequence is: ATATTTGCGCCC
```
Python has built-in functions that are useful for manipulating strings. A function can usually applied to multiple data types, and a simple function that is often used with strings is `len()`:
```python
>>> len(my_sequence)
12
```
Later we will see `len()` used for other data types.
You can also do operations that are specific to a particular data type. These are called **_methods_**, and are applied slightly differently from functions. We use them by first assigning our data to a variable and then following the variable name by a period `.`, followed by the method's name and parentheses:
```python
>>> print(my_sequence.lower())
atatttgcgccc
>>> print(my_sequence)
ATATTTGCGCCC
```
In the above we applied the method `lower()` to our `my_sequence` variable and the `print()` function on the results of that method. Note that the contents of our variable `my_sequence` were not changed. We can change the contents, or **_overwrite_** a variable by assigning a new value to its name:
```python
>>> my_sequence = my_sequence.lower()
>>> print(my_sequence)
atatttgcgccc
```
Strings have many methods and function that can be applied to them. You can find a list of all the methods in the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). It is likely that at first you will find those pages too technical, but as you learn more about how Python works they will become the first place to look for help when working on a problem. Let's try a couple more `str` methods.

Similarly to the `lower()` methods, there is a way to convert strings to uppercase:
```python
>>> print(my_sequence)
atatttgcgccc
>>> print(my_sequence.upper())
ATATTTGCGCCC
```
You can also count the occurrence of a character or a substring in a string with `count()`:
```python
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
You can replace or translate characters using `replace()`. Replace has a bit more sophisticated interface, since you need to tell this function what characters to substitute. The general syntax is `replace(old, new)`:
```python
>>> print(my_sequence)
atatttgcgccc
>>> print(my_sequence.replace("t", "g"))
agaggggcgccc
```
Remember that by simply using a function or method on a variable we are not changing its contents.

Remember the `count()` method? Let's try to print its output in a more informative way:
```python
>>> print("There are " +  my_sequence.count('a') + " occurrences of 'a' in your sequence")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```
What is this about? We know that we can concatenate strings with the plus sign, so why does this not work? The error above tells us where something went wrong `(line 1 of <stdin>)` and what was the error `(TypeError: Can't convert 'int' object to str implicitly)`. The error tells us that there was a "int" object that could not be converted to a `str`, the Python's shorthand for string. Turns out that the output of the `count()` method is not a string but a different data type, an **_integer_** or `int`. We will explain how Python handles number in a separate section, but for now its enough to say that integers are simply "whole" numbers, those without fractional components.
We can make the above work by converting the integer output of `count()` into a string. This is done using the `str()` function:
```python
>>> print("There are " +  str(my_sequence.count('a')) + " occurrences of 'a' in your sequence")
There are 2 occurrences of 'a' in your sequence
```
We have now converted the output of `count()` into a string by enclosing the call to that function within parentheses of the `str()` function. We could make this a bit more readable by first assigning the string with our count to a variable. This will also enable us to reuse that value later without the need to type two nested functions:
```python
>>> my_a_count = str(my_sequence.count('a'))
>>> print("There are " +  my_a_count + " occurrences of 'a' in your sequence")
There are 2 occurrences of 'a' in your sequence
``` 
We don't need to repeat the `str()` function here because `my_a_count` is already a string.
Try writing some code that counts all bases (A, C, G, and T) in the following string: "ATAATTGATAGTATGCTACC".
Your code cold look like this:
```python
>>> my_seq = "ATAATTGATAGTATGCTACC"
>>> my_A_count = my_seq.count("A")
>>> print(my_A_count)
>>> my_C_count = my_seq.count("C")
>>> print(my_C_count)
>>> my_G_count = my_seq.count("G")
>>> print(my_G_count)
>>> my_T_count = my_seq.count("T")
>>> print(my_T_count)
```

## Data types: integers and floats
We alluded to other types above and now we will talk more about the two variables used to handle numbers: integers and floats. The integers represent "whole" numbers, or those without fractional component, while "floats" are used to store numbers with fractional components. We have already met integers and we saw that the output of the `len()` function is an integer. The number 10 is an example of integer, but 10.0 is a float. Why this difference? This is because fractional numbers represented in computer memory differently from whole numbers. Let's try assigning some integers, floats, and strings to variables:
```python
>>> my_num1 = 9
>>> my_num2 = 3.1415
>>> my_num3 = "3.1415"
```
We can find out what kinds of data is in a variable with the `type()` function:
```python
>>> type(my_num1)
<class 'int'>
>>> type(my_num2)
<class 'float'>
>>> type(my_num3)
<class 'str'>
```
Note that by putting the last number in quotes we made it a string. If we don't do that, Python will recognize that we are assigning numbers to the variable. In general, you don't need to be too concerned with the integer/float difference in much of your Python scripting, but you need to remember about it when trying to convert data types:
```python
>>> my_num3 = int(my_num3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.1415'
```
You will get an error if you try to convert a string that looks like a float into an integer, but you can convert it into a float (try it!), which then allows you to use the variable like a number.
You can perform all standard types of mathematical expressions on floats and integers:
```python
>>> 4 + 4
8
>>> 4 * 4
16
>>> 4 - 4
0
>>> 4 / 4
1.0
>>> 4 ** 4
256
>>> my_num1 * my_num2
28.273500000000002
```
To better understand how the code you type is interpreted it is important to highlight here the concept of an expression. The math above are simple examples of expressions. Python tries to **_evaluate_** each expression until it becomes a single value. Python expressions using numbers behave according to the rules of mathematical expressions, that is they follow the order of operations where exponents `**` are evaluated first, followed by multiplication with `*` and division `/`, finally followed by addition `+` and subtraction `-` (all evaluated from left to right). A simple mathematical expression will be evaluated piece by piece until it returns a single value:
```python
2 * 2 - (2 + 2) / 5
2 * 2 -    4    / 5
  4   -    4    / 5
  4   -    0.8
 3.2
```
It is helpful to realize that other statements we write in Python behave in a similar way. In an earlier example we saw
```python
print("There are " +  str(my_sequence.count('a')) + " occurrences of 'a' in your sequence")
```
We can think of this code as an expression being evaluated until it returns a single value:
```python
print("There are " +  str(my_sequence.count('a')) + " occurrences of 'a' in your sequence")
print("There are " +  str(           2          ) + " occurrences of 'a' in your sequence")
print("There are " +                "2"           + " occurrences of 'a' in your sequence")
print("There are 2"                  +              " occurrences of 'a' in your sequence")
print("There are 2 occurrences of 'a' in your sequence")
There are 2 occurrences of 'a' in your sequence
```
## Data types: Boolean values
There is another important data type in Python: Boolean values (named after mathematician George Boole). You may remember when we mentioned that a variable name cannot be `True` or `False`. This is because those are keywords used for the two possible Boolean values. We assign them without using quotes:
```python
>>> something = True
>>> print(something)
True
>>> True = "123"
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
```
Boolean values are used to compare statements and will be especially important when we will be talking about flow control, that is  code that can behave differently depending on whether a condition is `True` or `False`. Just as in mathematical expressions, there are special operators that are used to compare values:

|operator  |meaning                   |
| :------: | ------------------------ |
| ==       | equal to                 |
| !=       | not equal to             |
| <        | less than                |
| >        | greater than             |
| <=       | less than or equal to    |
| >=       | greater than or equal to |

Let's try some expressions that will evaluate to `True` or `False`:
```python
>>> 2 == 2
True
>>> 2 != 2
False
>>> 5 > 15
False
>>> "x" != "z"
True
```
## More on strings
There are a couple more things about formatting strings that will be useful. Just as in the shell, you can add special characters to your strings and have strings that span multiple lines:
```python
>>> print("This is a multiline\nstring.")
This is a multiline
string.
```
As you may remember from the command line tutorials, the `\n` character signifies newline. Another way to specify multiline strings is just enclose them in three quote signs `"`:
```python
>>> print("""This is a multiline
... string""")
This is a multiline
string
```
The above is also useful for multiline comments explaining your code.

You can access certain characters or subsets of a string using Python's **_indexing_** system. Try:
```python
>>> my_seq = "ATAATTGATAGTATGCTACC"
>>> my_seq[0]
'A'
>>> my_seq[0:5]
'ATAAT'
>>> my_seq[:5]
'ATAAT'
>>> my_seq[5:]
'TGATAGTATGCTACC'
>>> my_seq[5:7]
'TG'
```
As you can see, the indexing system in Python works somewhat different from our concept of what would be the ordering of elements in a set: `my_seq[0]` means "**first** character of my_seq", `my_seq[0:5]` means "characters first to **fourth** (5 - 1) of my_seq", and `my_seq[5:]` means "characters **fifth** to the end of my_seq". In other words, indexing in Python starts with zero and is first-inclusive but last-exclusive. This should help visualize how elements of a string are counted:
```
"A  T  A  A  T  T  G  A  T  A  G  T  A  T  G  C  T  A  C  C"
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
```

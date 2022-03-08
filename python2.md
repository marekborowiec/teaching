# PYTHON PROGRAMMING PART 2

## Lists
Last week we talked about data types in Python and discussed strings, integers, floats, and Booleans. Today we will start off with lists. Lists simply store multiple objects. Just as we can assign values to strings by putting them in quotes, we can assign values to a list by putting them inside square brackets:
```python
>>> list1 = ['hello!']
>>> print(list1)
['hello!']
```
We can put zero, (empty `[]`), one, or multiple values in a list and they can be of different types.
```python
>>> list1 = ['hello!', 123, True]
>>> print(list1)
['hello!', 123, True]
```
Accessing elements in a list uses the same indexing scheme that we now know from strings:
```python
>>> list1[1]
123
>>> list1[1:3]
[123, True]
>>> list1[1:2]
[123]
```
You can see that using these indices we can create sublists from our original list. You would do this by assigning your sublist to a new variable:
```python
>>> list2 = list1[1:]
```
Because we have taken a _slice_ from the original list, this action is often called **_slicing_**.
You can also lookup the index of an item using the `index()` method:
```python
>>> list1.index('hello!')
0
```
The index printed will be the first occurrence of this element and you won't see other indices if the value is repeated in your list.

You can also change values at particular index by reassigning them:
```python
>>> print(list1)
['hello!', 123, True]
>>> list1[0] = 'goodbye!'
>>> print(list1)
['goodbye!', 123, True]
```
We already learned that the `len()` function gives the length of a string. Let's give it a try with our list:
```python
>>> len(list1)
3
```
You can add new elements to the end of a list by using the `append()` function:
```python
>>> list1.append(321)
>>> print(list1)
['goodbye!', 123, True, 321]
```
Notice how reassigning items and appending them modified the existing list **_in place_**. This is different from slicing, where we needed to save our slice in a new variable to use it later.
To add an item at a particular item, use the `insert()` method:
```python
>>> print(list1)
['goodbye!', 123, True, 321]
>>> list1.insert(2, False)
>>> print(list1)
['goodbye!', 123, False, True, 321]
```
We need to supply `insert()` with the index at which to add an item and the value of the item itself. Not how the list was modified in place again.

Deleting elements from lists can be accomplished in two ways. We can delete value by index with the `del` statement:
```python
>>> print(list1)
['goodbye!', 123, False, True, 321]
>>> del list1[2]
>>> print(list1)
['goodbye!', 123, True, 321]
```
Alternatively, we can delete the first item (just like `index()`) of a certain value with the `remove()` method:
```python
>>> print(list1)
['goodbye!', 123, True, 321]
>>> list1.remove('goodbye!')
>>> print(list1)
[123, True, 321]
```
You are not limited to holding a single value at each position in the list. You can also create lists of lists:
```python
>>> list_of_lists = [["A","C","G"],["A","T","C"],["A","G","G"]]
```
This kind of structure is similar to an array or a matrix, and you can access elements by their coordinates. If we imagine this list of lists as a grid,
```python
list_of_lists = [["A","C","G"],
                 ["A","T","C"],
                 ["A","G","G"]]
```
we can see that each element will be identified by its coordinates:
```python
>>> list_of_lists[0][0]
'A'
>>> list_of_lists[0][1]
'C'
>>> list_of_lists[2][2]
'G'
>>> list_of_lists[1][1]
'T'
```
In the example above we accessed the upper left value with the `[0][0]` index and lower right value with the `[2][2]` index.

How would you make and access items in a list of lists of lists? Try adding new elements to existing lists within the list and lists to the main list.

One final feature to mention here is the `list()` method, which is used to convert other data types into lists, similarly to `int()` or `str()` methods we already encountered. For example, you can convert a string into a list, like so:
```python
hello = 'hello!'
print(hello)
hello!
list(hello)
['h', 'e', 'l', 'l', 'o', '!']
```

## Dictionaries
Dictionaries are similar to lists because they can hold mutliple values. Dictionaries, however, have a way of indexing each value by a key that can be a string or an integer. When creating a dictionary, you need to assign both keys and values. The general syntax is that the key-value assosciation is indicated by the colon `:`, the pairs of key-value are separated by commas `,`, and the dictionary is enclosed in curly brackets `{}`:
```python
>>> my_pets = {'dog' : 'black','cat' : 'red', 'ant' : 'yellow'}
```
You can get all values or keys of a dictionary using the `keys()` and `values()` methods, respectively:
```python
>>> my_pets.keys()
dict_keys(['dog', 'ant', 'cat'])
>>> my_pets.values()
dict_values(['black', 'yellow', 'red'])
```
The values returned are list-like, but are not true lists: you cannot use the familiar list methods on them directly. However, you can also convert these objects into true lists with the `list()` function. You can also use them in loops, at which we will look at shortly.
In dictionaries, you access a value by using its key:
```python 
>>> my_pets['dog']
'black'
>>> my_pets['ant']
'yellow'
>>> my_pets['yellow']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'yellow'
>>> my_pets[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
```
The first error above shows that we cannot access a key in a doctionary the same way as we can access a value.The second error above shows that you cannot access a dictionary value by its index. In fact, dictionary data in Python is not ordered. Because of this, accessing a dictionary with an index number does not make sense. Another important thing to remember about dictionaries is that while values can be repeated within a dictionary, all keys must be unique.

```python
>>> pets = list(my_pets.keys())
>>> pets
['dog', 'ant', 'cat']
>>> colors = list(my_pets.values())
>>> colors
['black', 'yellow', 'red']
``` 
Try to make your own dictionary and play around with accessing its values by key and printing them all at once. 

## Loops and flow control 
Flow control is a collective name for all the ways we can make our program do things differently, depending on a condition. Loops are used to execute a piece of code over and over on some objects, such as items in a list. These concepts are common to virtually every programming language, and all you need to know to use them outside of Python is the syntax specific to the language.

### `for` loops

One of the most useful concepts that a biologist learns in programming is that of a `for` loop. Loops allow you to repeat actions and the `for` loop is likely the one you will be using the most often.
Before we start writing loops, let's open a text editor and write our first script. Sublime Text is a good general editor avaliable for all operating systems. You should have an icon of this program on the desktop of your virtual machine. Open it now with a double-click. You can also start it from the command line and simultaneously creating a file by typing `subl for_loop.py` at the command line. Be sure to exit Python interpreter with `quit()` first!

By opening a file with the `.py` extension, Sublime Text recognized that it's going to be a Python script and turned on **_syntax highlighting_**. This is a very useful feature that will help you orient around your code and make sure you have closing quotes and parentheses.
Start with the so-called **_shebang_**:
```python
#! /usr/bin/env python3
```
This line tells the computer where to look for the program that will execute the script. Next, let's create some variables that we can loop through:

```python
seq = "ACGT"

plants = ['flax', 'rose', 'buttercup']

families = ['Linaceae', 'Rosaceae', 'Ranunculaceae']
```
Next, let's try our first loop. In Python you can loop directly on string characters. The `for` loop syntax in Python looks like this:
```python
# this will print all characters in seq
for letter in seq:
    print(letter)
```
We first put the `for` statement, followed by the variable `letter`, statement `in`, and the variable name `seq`. Then we added a colon `:`, pressed `Return`, and we saw that the editor automatically **_indented_** the next line by one tab. The indented block is the code that will be execute over and over with the loop for all items in the `seq` variable. In most languages this indentation inside loop is a convention that is supposed to make code more readable and the content of the loop is signified by some additional symbols, but in Python the indentation itself (preceded by a colon `:`) determines loop contents.
Note the variable `letter`. Normally we wouldn't use a variable name that was not previously defined, but in loops a variable that is equivalent to each item in a collection looped over is created 'on the go'. We could have named it something else and in explanations of loop syntax you will sometimes see the generic `i` (`for i in ...`) in that place.

It's time to execute our first Python script. Save your file and move back to the terminal window. Hot tip: on PC you can switch between windows with `ALT+TAB` and on Mac with `ALT+SHIFT+TAB`. Run your script:
```shell
python3 for_loop.py
```
This should have printed all elements of your `seq` variable on separate lines (`print()` adds a newline after each execution by default). Let's go back to our script and try something else. `for` loops are useful to accomplish something a certain number of times. You can use the function `range()` in your loop to do this. `range()` takes two integers: one for the beginning and one for the end of a range. If you want to count from zero you can only give one integer, which will be interpreted as the end of the range.
```python
# this will print seq 5 times
for i in range(5):
    print(seq + " sequence printed times " + str(i))
```
Our program now executes two loops. The second loop prints your `seq` variable, followed by some text, followed by the current count in the range function. The count is done from zero but you can make it look more natural by adding `1` to `i`:
```python
# this will print seq 5 times
for i in range(5):
    print(seq + " sequence printed times " + str(i + 1))
```
Remember that you need to save the file before execution for any changes to take effect.
Let's comment out the two loops we just wrote with triple `"""` at the beginning and the end:
```python
"""
# this will print all characters in seq
for letter in seq:
    print(letter)

# this will print seq 5 times
for i in range(5):
    print(seq + " sequence printed times " + str(i + 1))
"""
```
If you remember from the previous tutorial, the triple quotes are used for multiline comments and comments are ignored in program execution. Below the commented-out text let's write a `for` loop that goes through the plants in our lists and prints the family they belong to. Note that this will only be possible if items in both lists are in corresponding order:
```python
# this will iterate over values from one list and find
# values of the same index in another list
for plant in plants:
    print(plant + " is in the family " + families[plants.index(plant)])
```
Just as in the string, the loop knows to treat each object in the list as a separate item. We took advantage of the fact that there is a one-to-one correspondence of indices in both lists, but it seems like this kind of data would be better stored as a dictionary, with plants as keys and families as values. Comment out the loop lines and create a new dictionary:
```python
taxonomy = {'flax' : 'Linaceae', 'rose' : 'Rosaceae', 'buttercup' : 'Ranunculaceae'}
```
Remember when we were talking about the methods available for dictionaries? There is another very useful method, `items()` that allows us to loop through key and value simultaneously:  
```python
for key, value in taxonomy.items():
    print(key + " is in the family " + value)
```

# PYTHON PROGRAMMING PART 2

## Lists
Last week we talked about data types in Python and discussed strings, integers, floats, and Booleans. Today we will start off with lists. Lists simply store multiple objects of other kinds of data. Just as we can assign values to strings by putting them in quotes, we can assign values to a list by putting them inside square brackets:
```python
>>> list1 = ['hello!']
>>> print(list1)
['hello!']
```
We can put zero, (empty `[]`), one or multiple values in a list and they do not have to be all of the same type.
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
Alternatively, we can delete the first item of a certain value with `remove()`:
```python
>>> print(list1)
['goodbye!', 123, True, 321]
>>> list1.remove('goodbye!')
>>> print(list1)
[123, True, 321]
```


## Dictionaries

## Flow control 


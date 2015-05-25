# Project 1: Python scripting
This project will help you practice the Python scripting skills you learned in the tutorials.

You will need a an [example file](https://raw.githubusercontent.com/marekborowiec/teaching/master/files/ponerine.phy) that represents a DNA sequence alignment for multiple ant species. You can copy and paste the contents at this link.

The file has two major components:

1) A header that shows the number of sequences followed by sequence length (here 138 and 4845, respectively). In a sequence alignment all sequences have the same length.

2) Multiple lines that contain a name of a species and its sequence, separated by spaces.

Each sequence is actually composed of 7 different genes and your task is to write a program that splits the sequence into multiple files, each with the same set of taxa but with sequences from only one gene.

These gene partitions are as follows:
```
Wg = 1-451
LWR = 452-918
CAD = 919-2440
EF1aF1 = 2441-2799
EF1aF2 = 2800-3316
AbdA = 3317-3946
r28S = 3947-4845
```
The above means that the 'Wg' gene is represented by sequence characters 1 through 451 and the 'r28S' gene is represented by characters 3947 through 4845 out of the total 4845 bases in the example file.

For each gene you need to write a file (which you could call `Wg.phy`, `LWR.phy`, etc. for example) that has:

1) a header line with the number of taxa and the length of the sequence and

2) all 138 taxa and corresponding sequences. The taxa and sequences don't need to be [justified](http://en.wikipedia.org/wiki/Typographic_alignment), you can siply separate them by two spaces in your output.

You will need to use your knowledge of lists, dictionaries, loops, reading and writing files, and string splitting and slicing to write this program.

Hints:

If you want to skip a line (such as a header) in processing a file, you can keep track of the numbers of lines with a counter:
```python
line_counter = 1

for line in in_file_lines:
    if line_counter > 1:
        ... do something
    line_counter += 1
```
The above loop will skip the first line when processing with 'do something' because at its first iteration the counter is set to `1` and the `if` statement returns `False`. At the end of the first line the loop will add `1` to `line_counter` and thus every following line will be processed.

The `.split()` method called with no arguments (i.e `string.split()`) splits by one or more empty characters. This is what you will want.

String slicing is what you can use to split the sequences into chunks corresponding to each gene. Remember about indexing when slicing: first inclusive but last exclusive. Also remember thar 'Python counts from zero'. Example slice for LWR: `[451:918]`.

Dictionaries are a good structure for storing { 'taxon' : 'sequence' } data.

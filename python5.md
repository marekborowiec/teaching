# PYTHON PROGRAMMING PART 4
## Bringing it all together: creating a KML file
Now that you know the basics of Python's syntax, you are ready to apply this knowledge to reformat a file. The KML format is a [markup language](http://en.wikipedia.org/wiki/Markup_language) that is used to annotate data to be visualized in Google Earth. In this tutorial we will create a Python program that converts a subset of the data in our example `ants.txt` file to a format that can be displayed in Google Earth. There are several on-line tools to convert spreadsheets into KML files, but writing your own script is a good exercise and will make you use many of the basic concepts you've learned so far. You can find the complete script written for this tutorial under `antweb_to_kml.py` and also towards the end of this page. The final KML output is in `ants.kml`. 
### The basics of KML
A simple KML document contains header (opening) lines, the so-called placemark, and closing lines:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
<Placemark>
  <name>New York City</name>
  <description>New York City</description>
  <Point>
    <coordinates>-74.006393,40.714172,0</coordinates>
  </Point>
</Placemark>
</Document>
</kml>
```
In the example above there are three header lines and two closing lines, and one placemark block that corresponds to one data point that is displayed in Google Earth. Note that the placemark block provides longitude first, then latitude, and finally altitude. You can see that the symbols `<`, `>`, and `/` have special meaning in KML, so beware of those in the data you want to use inside of it.

### Thinking about a programming project

We want to take the data on specimen code, genus, species, and coordinates from our input data file (`ants.txt`) and write a placemark block to create a point for each record. 

We have stated our goal above, so now let's pause briefly to identify the possible steps towards the solution of our problem. One of the most important skills in programming is the ability to break down complex problems into smaller chunks that can be easily tackled when considered separately.

At the general level, we need to:

1) open the input file and get data from it,

2) parse it somehow and extract only the parts that we need, 

3) package it into the KML format,

4) and write this format into a new file.

### Getting input

We already know how to open a file, so let's start by creating a new Python script `antweb_to_kml.py` that opens the `ants.txt` file and reads its contents. We will want to process the contents line by line, so let's use the `.readlines()` method:
```python
#! /usr/bin/env python3

# antweb_to_kml.py by Your Name
# this script converts data from the example file
# 'ants.txt' to a kml format.

# create file object
in_file = open("ants.txt")

# read in file contents as list of strings (lines)
in_file_lines = in_file.readlines()
```

### Parsing and extracting data

Now we need to look at our `ants.txt` file to remind ourselves about its structure. You should now know how to use `less` or other command line tools to examine this file. It has a header that shows a total of 33 fields. We are interested in `SpecimenCode`, `Genus`, `Species`, and of course `LocLatitude` and `LocLongitude`. These fields correspond to numbers 1, 3, 4, and 28 and 29, respectively. The fact that they are tab separated is crucial.

You could imagine a solution with the Unix `cut` command, but let's try to come up with one in Python that does not require rewriting of the input file. We already know about the method `.split()` that will cut up a string using a separator and return a list of strings. In our case the separator is the tab, which can be represented by `"\t"`. Once you have a list of strings, you can assign the elements you are interested in to variables.

How would you construct a loop that goes over each line of the input file, splits it by tabs, and prints out only the desired fields? Remember that list elements are counted from zero.

Below your code to open and read in file contents, add:
```python
for line in in_file_lines:
    split_line = line.split("\t")
    specimen_code = split_line[0]
    genus = split_line[2]
    species = split_line[3]
    latitude = split_line[27]
    longitude = split_line[28]
    print(specimen_code, genus, species, latitude, longitude, sep=" ")
```
On the last line we used a `sep=` argument to the `print()` function to specify what is supposed to be printed between the variables. An alternative syntax that you are already familiar with would be `genus + " " + species + " " + ...`, which with this many separators would make for a long line of code.
 
Lastly, don't forget to close the input file:
```python
in_file.close()
```
Save this and try running the script in your `Sandbox` directory. You should see that it runs fine until right after line with `casent0162159`. The error says that you are trying to access a list index (`[2]`) that does not exist. You can use `grep -A1 "casent0162159"` on the `ants.txt` file to see what's one line after the one where our program trips. This reveals that the problem is caused by an empty line. In processing large amounts of data it is common to deal with formatting problems like this, so it's a good opportunity to think about how we can deal with them. In general you often have to choose between two alternatives: fixing the file or making your code more robust to exceptions. In this case, you could use `sed` to get rid of all the empty lines in `ants.txt` before running your script again or make your Python program ignore them. Either approach may be more appropriate depending on the goals of your program.

For our purposes let's assume that any line that does not have all the elements after splitting by tabs is not properly formatted and we should ignore it. How would you code that?

First we can check how many elements there are in each line after we split it. Add a `print()` function to your loop to see how long the list resulting from calling `.split()` is for each line:
```python
for line in in_file_lines:
    split_line = line.split("\t")
    
    print(len(split_line))  # <=== print function added

    specimen_code = split_line[0]
        ...
```
You can use `head` and `tail` to limit the output of the program. You should be able to see that the header line is 33 elements-long, most data rows have 34 elements, and the empty lines like the one at the end of the file give only 1 element. Since we are not interested in headers, let's focus on the lines that give us 34 a list of elements.  
We can add an `if` statement inside our `for` loop to check whether the output of `.split()` gives us the desired number of elements:

```python
for line in in_file_lines:
    split_line = line.split("\t")
    #print(len(split_line))
    if len(split_line) == 34:
        specimen_code = split_line[0]
        ...
```
Now the code runs all the way through the file. We have accomplished two of the four major tasks we outlined at the outset of our programming project. 

### Formatting `KML` output

Now the next thing to do is to plug in the information we extract from each line into a placemark string. Let's take another look at a placemark string from an example KML file. We can copy and paste it into our program and save it as a variable:
```python
for line in in_file_lines:
    ...

    placemark = """<Placemark>
  <name>New York City</name>
  <description>New York City</description>
  <Point>
    <coordinates>-74.006393,40.714172,0</coordinates>
  </Point>
</Placemark>"""
```
Instead of `New York` we would like to name our point using the `SpecimenCode` field from our input file and in the description we want to have the `Genus` and `Species` fields. We also need the coordinates. One way to do this would be to use the syntax for string concatenation, where variables and text can be joined using the plus `+` signs. With a long, multiline string like the placemark, however, this solution is not very elegant:
```python
    placemark = """<Placemark>
  <name>""" + specimen_code + """</name>
  <description>""" + genus + " " + species + """</description>
  ...
```
A better way is to use the `.format()` method. This function provides a variety of tools for formatting strings and a common use of it is plugging variables into a string. `.format()` uses curly brackets `{}` inside the target string to indicate places where a variable will be inserted. Let's try rewriting our `placemark` string with the proper `.format()` syntax:
```python
    placemark = """<Placemark>
  <name>{}</name>
  <description>{} {}</description>
  <Point>
    <coordinates>{},{},0</coordinates>
  </Point>
</Placemark>""".format(specimen_code, genus, species, longitude, latitude)
```
Remember that KML wants logitude first and then latitude. We didn't use altitude from our data, so we just leave it at `0` here. Knowing other tricks of the `.format()` method is very useful; you can read about them [here](https://mkaz.com/2012/10/10/python-string-format/).

Now we can modify our loop to print the placemark string for each line:
```python
for line in in_file_lines:
    split_line = line.split("\t")
    #print(len(split_line))
    if len(split_line) == 34:
        specimen_code = split_line[0]
        genus = split_line[2]
        species = split_line[3]
        latitude = split_line[27]
        longitude = split_line[28]

        placemark = """<Placemark>
  <name>{}</name>
  <description>{} {}</description>
  <Point>
    <coordinates>{},{},0</coordinates>
  </Point>
</Placemark>""".format(specimen_code, genus, species, latitude, longitude)

        print(placemark)

in_file.close()
```
Remember about the indentation: the assignment of `placemark` variable needs to be inside the `if` statement, that is 8 spaces from the left. Because we are defining a multiline string however, the text within the assigned value does not have to be indented. The `print()` function has to be indented to within `if` as well. Save your script and run it to see if it works. You should see a placemark string printed for each line of data. You can interrupt the program with `Ctrl + C`.

Once we have the placemark strings ready we can add the header and closing lines before and after our loop:
```python
# read in file contents as list of strings (lines)
in_file_lines = in_file.readlines()

header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>"""

for line in in_file_lines:
    ...

ending = """</Document>
</kml>"""
```

### Writing the results to an output file

Now we have accomplshed three out of four stages outlined for our project: we have loaded our data in, parsed it and extracted the information we desired, and defined strings that give us the desired KML output. Now all we need to do is to write all these elements to some kind of output. We will need to open a new file from writing, have our script write the header lines first, then all of the placemark strings, followed by the closing lines. Because these elements need to be written in different times of the script's execution, we will use the `.write()` method three times: before the loop, inside the loop, and after the loop has finished. Finally, we will close our output file. Your code should look like this:
```python
#! /usr/bin/env python3

# antweb_to_kml.py by Your Name
# this script converts data from the example file
# 'ants.txt' to a kml format.

# create file object for input
in_file = open("ants.txt")

# read in file contents as list of strings (lines)
in_file_lines = in_file.readlines()

# create file object for ouput
out_file = open("ants.kml", "w")

# define header lines
header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>"""

# write header to ouput
out_file.write(header)

# loop over each line of input
for line in in_file_lines:
    # split line by tabs
    split_line = line.split("\t")
    #print(len(split_line))
    # check if line has all the elements
    # and define variables needed for placemark
    if len(split_line) == 34:
        specimen_code = split_line[0]
        genus = split_line[2]
        species = split_line[3]
        latitude = split_line[27]
        longitude = split_line[28]
        # define and format the placemark string
        placemark = """
<Placemark>
  <name>{}</name>
  <description>{} {}</description>
  <Point>
    <coordinates>{},{},0</coordinates>
  </Point>
</Placemark>""".format(specimen_code, genus, species, longitude, latitude)
        # print the placemark string
        #print(placemark)
        # write placemark from each line to output
        out_file.write(placemark)

# define closing lines
ending = """</Document>
</kml>"""
# write closing lines to output
out_file.write(ending)
# close input file
in_file.close()
# close output file
out_file.close()
```
You can now run the code and see that it produces output in mere seconds. Try to open the file in GoogleEarth by going to File -> Open and getting the `ants.kml` file. It is a large file with some 150,000 records, so it may take a while to load.

You will notice that there are points at 0, 0 degrees latitude and logitude. This is because some records in the data base were not georeferenced and have no values (empty strings for `longitude` and `latitude`). How would you modify your code to not include those records? How about getting only the first **n** lines (say, 10,000) or even random **n** lines? After these Python tutorials you should be able to answer these questions using either the knowledge from previous lessons or after getting some on-line help.

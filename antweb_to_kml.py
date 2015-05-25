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

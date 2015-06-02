#! /usr/bin/env python3

# split_by_gene.py
# this script parses example DNA sequence alignment
# and returns files corresponding to partitions

# create file object
in_file = open("ponerine.phy")

# read in file contents as list of strings (lines)
in_file_lines = in_file.readlines()

# create empty dictionaries for each gene
# keep commented out positions for each gene for reference
Wg = {} # 1-451
LWR = {} # 452-918
CAD = {} # 919-2440
EF1aF1 = {} # 2441-2799
EF1aF2 = {} # 2800-3316
AbdA = {} # 3317-3946
r28S = {} # 3947-4845

# initiate line counter
line_counter = 1

# loop over lines
for line in in_file_lines:

    # skip header
    if line_counter > 1:

        # get list of two strings:
        # [taxon, sequence]
        tax_seq = line.split()
        taxon = tax_seq[0]
        seq = tax_seq[1]

        # append taxon-sequence pairs to dicts
        Wg[taxon] = seq[0:451]
        LWR[taxon] = seq[451:918]
        CAD[taxon] = seq[918:2440]
        EF1aF1[taxon] = seq[2440:2799]
        EF1aF2[taxon] = seq[2799:3316]
        AbdA[taxon] = seq[3316:3946]
        r28S[taxon] = seq[3946:4845]

    # update line counter
    line_counter += 1

# define a dictionary with name : dictionary pairs for all genes
gene_dict = { "Wg" : Wg, "LWR": LWR, "CAD" : CAD, "EF1aF1" : EF1aF1, "EF1aF2" : EF1aF2, "AbdA" : AbdA, "r28S" : r28S }

# first loop over the names and dict objects to write headers
for name, gene in gene_dict.items():

    # get file name and open for writing
    file_name = name + ".phy"
    out_file = open(file_name, "w")

    # no. of taxa is just dict length
    no_taxa = len(gene)
    # sequence length can by of any taxon: all lengths are the same
    # getting length of a value from a dictionary is tricky:
    seq_length = len(gene[list(gene.keys())[0]])

    # a simpler but less robust solution would be 
    # to access any taxon present in all files:
    # seq_length = len(gene[Acromyrmex_versicolor])

    # define header and remember about adding newline
    header = str(no_taxa) + " " + str(seq_length) + "\n"

    # write header
    out_file.write(header)

    # now for each gene within gene_dict loop over 
    # taxon, sequence pairs to write the data
    # you cannot sort a dictionary, but you can sort elements
    # in a list-like object returned by the '.items()' 
    # method with 'sorted()'
    for taxon, sequence in sorted(gene.items()):

        # for each write the taxon, sequence, and newline
        out_file.write(taxon + "  " + sequence + "\n")

    # close the file at each loop iteration
    out_file.close()

# close input file
in_file.close()

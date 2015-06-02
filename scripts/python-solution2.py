#! /usr/bin/env python3

# A compact solution using lists submitted by Nicole Soltis

# create file object
in_file = open("ponerine.phy")

# read in the data
in_file_lines = in_file.readlines()

# create a list with all gene names
gene_name = ["Wg","LWR","CAD","EF1aF1","EF1aF2","AbdA","r28S"]

# create two lists with start and end positions
# note that the indices for all three lists need to be aligned
# i.e. gene_name[0] corresponds to the start of Wg
# at gene_start[0] and end at gene_end[0]
gene_start = [0,451,918,2440,2799,3316,3946]
gene_end = [451,918,2440,2799,3316,3946,4845]

# use a loop that runs for as many times as there are elements in your gene names list
for i in range(len(gene_name)):

    # create output file object using the gene name string
    # at current index with extension appended to the end
    out_file = open(gene_name[i] + ".phy", "w")

    # define header for output file
    header = "138 " + str(gene_end[i] - gene_start[i]) + "\n"

    # write header to output file
    out_file.write(header)

    # start a nested loop that loops over all lines in the input
    # since the in_file_lines is a list, 
    # you can use indexing here, too!
    for line in in_file_lines[1:]:
        # get list of two strings
        tax_seq = line.split()
        # get species name and sequence
        taxon = tax_seq[0]
        sequence = tax_seq[1]

        # use indexing to access the positions depending on which
        # iterations of the loop ("i") you are in
        gene = sequence[gene_start[i]:gene_end[i]]

        # write the output file
        out_file.write(taxon + "  " + gene + "\n") 

    # close the output file within outer loop
    out_file.close()

# close input file
in_file.close()

import numpy as np
import random as rdm

"""
Write a python function to select a random subset of a set of nucleotide sequences from an excel file.
Input: A .txt file containing nucleotide sequences and a size
Output: The subset of size given by the user.

# find participating countries for the nucleotide
#  sequences

# parse to separate the sequences based on geographic location

# count the total number of available sequences from each geographic location

# pick a subset that is proportional to the size of the number of available sequences for each
# geographic location

# randomly choose a list of n elements for a given geographic location, say 1/4 or 50% of total sequences
# at a given location

# put them into a file (again, for each data set) or into separate files for subsequent analysis
"""

def random_subset(txt_file, size):
    # make a list of all the data for each row
    data_set = []
    with open(txt_file, 'r') as f:
        for line in f:
            data_set.append(line)

    # Build an empty list
    subset = []

    # while len(subset) < size, get a random row i from the data set list set,
    # swap i with the last element of "set"
    # append i to subset
    # remove i from "set" so we don't add it to subset again
    # repeat until len(subset) == size
    while len(subset) < size:
        index = rdm.randint(0, len(data_set)) # need to swap with data_set[len(data_set)-1]

    return subset

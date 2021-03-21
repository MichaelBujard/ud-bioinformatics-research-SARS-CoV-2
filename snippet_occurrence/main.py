import math
import os
import numpy as np
import Bio
from Bio import SeqIO
import re

"""
It might be better to use a matrix. numpy might come in handy. 
Dr. Toby, what do you think?This is a  snippetOccurrenceMap (In java, but implemented in Python).
The oracle official website has information about datatypes. 
In Python, HashMaps are "dictionaries" and arraylists are just "arrays". 
So, the code will be a dictionary of strings (sequence IDs. Let's call the 
IDs at this layer X) mapped to an array of dictionaries. Each item in the
 list is another "nested" dictionary. Each nested dictionary maps the sequence
  being compared to the current sequence ID to another dictionary. This last 
  dictionary keeps track of all the amino acids that are different at any index 
  from the original ID (the IDs labelled X) . e.g. in the last inner layer, the dictionary
 maps an amino acid "a" to the index where it is found in the sequence that is different
  from the X ID sequence.
"""

########################################
# GET THE .FASTA FILE AS A STRING
########################################

FILEPATH = "22-sgp-protein-seqs-from-any100.fas"

# open file at path
file = open(FILEPATH, "r")
# store as string
seq_str = file.read()
# close file after getting string content
file.close()


############################################
# FUNCTION DEFINITIONS
############################################

def get_ID_sequence_map(string):
    """
    :param string: the input file as a string
    :return: a map of key, value pairs.
    key = accession ID,
    value = protein sequence belonging to the accession ID
    """
    string_queue = string.splitlines()      # treat the input string as a queue of lines...
    seq_map = {}                            # this is the map that will have the ID mapped with its sequence
    ids = []                                # this is an array that holds the ID values as a temporary structure.

    # The ith sequence in
    # sequences (below) will be mapped to the ith ID in IDs (above)
    sequences = []                          # This stores the ith sequence for all i in sequence
    a_sequence = ''                         # this is a sequence to append to the list

    while bool(string_queue):
        front = string_queue.pop(0)
        front_first_word = front.split(' ')[0]

        if front_first_word[0] == '>':
            ids.append(front_first_word[1:])    # get the ID without the '>' character
            sequences.append(a_sequence)
            a_sequence = ''                     # we've reached a header, so start a fresh sequence
        else:
            a_sequence += front                 # this is not a header. Append line to sequence
            if not bool(string_queue):
                sequences.append(a_sequence)    # if the queue is empty now, before terminating the loop, append

    # get rid of the first null string appended to sequence list.
    # the step above appends a null string in the first element of the sequences list. Remove it.
    sequences.pop(0)

    for index in range(len(ids)):
        seq_map[ids[index]] = sequences[index]  # map ID to its corresponding sequence

    return seq_map


def map_snippet_occurrence(sequence_map):
    """
    :param sequence_map: the map of sequence IDs and their corresponding sequences
    :return: a map of sequence IDs with their corresponding lists of "snippet occurrences"
    snippet occurrence: a mismatch at the ith amino acid. We save the accession ID, index, amino acid where the
    mismatch happens in the sequence and append it to a list of such occurrences for the ID.
    """

    s_o_map = {}
    seq = sequence_map.items()              # for ease of use

    for accession_id, id_sequence in seq:  # for each <ID, sequence> in the file,
        s_o_value = []  # this is an empty list, an initial value for snippet occurrences in the map
        for i in range(len(id_sequence)):  # for each amino acid in the sequence,
            amino_one = id_sequence[i]  # get the ith amino acid in the sequence and save it
            for other_id, other_seq in seq:  # for every other sequence (it would be better not to include cur)
                if len(id_sequence) == len(other_seq):  # they can be compared if they're the same length
                    a_two = other_seq[i]  # we assume that, for every sequence, the length of the sequences
                    if amino_one != a_two:  # will be the same, so that the ith aa of seq1 should be the ith aa
                        s_o_value.append((other_id, a_two, i))  # of seq2 unless there was mutation
        s_o_map[accession_id] = s_o_value  # outside of the loops, we have maximally populated the array
        #  of snippet occurrences corresponding to the current sequence
        s_o_value = []  # so clear the temporary value and reiterate
        # need to check that we've already compared the sequences...

    return s_o_map



###################################
# MAIN METHOD
###################################

if __name__ == '__main__':
    ID_String = get_ID_sequence_map(seq_str)
    print(ID_String)

    snippet_map = map_snippet_occurrence(ID_String)

    print(snippet_map)

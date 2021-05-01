"""
Michael Bujard
March 22, 2021
Snippet occurrence functions for aligned sequence analysis.
Note:
1) This code assumes that data is saved in a .fasta format and that
headers have the accession ID at the beginning.
2) This code assumes that multiple sequence alignment has been done on the .fasta file, because
the code only allows sequences of the same length to be compared to check for snippet occurrence
"""

import numpy as np
import sys
import os
from pipenv.vendor.distlib.compat import raw_input
import random


########################################
# GET THE .FASTA FILE AS A STRING
########################################

#FILEPATH = "22-sgp-protein-seqs-from-any100.fas"

# open file at path
#file = open(FILEPATH, "r")
# store as string
#seq_str = file.read()
# close file after getting string content
#file.close()


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
    s_o_map = {}                                # value to return
    seq_list = list(sequence_map)

    for i in range(0, len(sequence_map)):
        i_key = seq_list[i]                     # get the key of the KVP in the dictionary, key of A
        i_val = sequence_map.get(seq_list[i])   # --//--  value ---------//-------------  , value of A
        value = {}                              # initialize the value to map to the ID (key) of A
        for j in range(i, len(sequence_map)):   # compare A with every ofther KVP B in the file
            if i != j:                          # avoid comparing a sequence with itself
                j_key = seq_list[j]                     # get the key of the KVP in the dictionary, key of B
                j_val = sequence_map.get(seq_list[j])   # --//--  value ---------//-------------  , value of B
                snippet_occurrences = {}        # now initialize the value to map to the ID (key) of B
                # compare the sequences
                if len(i_val) == len(j_val):  # make sure strings are comparable (same length)
                    for i in range(len(i_val)):  # for each amino acid
                        if i_val[i] != j_val[i]:  # if there is a mismatch at the ith aa,
                            snippet_occurrences[i_val[i], j_val[i]] = i  # save the snippet occurrence
                value[j_key] = snippet_occurrences  # save the snippet occurrences from comparing A to B
                s_o_map[i_key] = value  # map key of A to value dictionary
    return s_o_map


def snippet_occurrences_between_two_sequences(map, a, b):
    """
    :param map: the dictionary that maps sequence ID a to the map of sequence IDs b to snippet occurrences
    :param a: the first sequence, corresponding to the key in the s_o_map 
    :param b: the sequence corresponding to the key of the value map, where the value map is mapped to the key a
    :return: the snippet_occurrences map generated by comparing sequence A to sequence B in s_o_map
    """
    if map[a].get(b) is None:
        return map[b][a]
    return map[a][b]

def ratio_of_snippet_occurrences_to_sequence_length(map, a, b):
    """
    :param map: the dictionary that maps sequence ID a to the map of sequence IDs b to snippet occurrences
    :param a: the first sequence, corresponding to the key in the s_o_map 
    :param b: the sequence corresponding to the key of the value map, where the value map is mapped to the key a
    :return: the ratio between the number of snippet occurrences to the length of the sequence a
    (compared to b)
    """
    n = len(snippet_occurrences_between_two_sequences(map, a, b))  # number of snippet occurrences
    m = len(map)
    return n / m


###################################
# MAIN METHOD
###################################

if __name__ == '__main__':

    # Introduce the program
    print("Super Subset Selector takes the file path of a *.acc file containing an accession list.\n"
          "This program also takes a positive integer to specify the size of the accession list subset. \n"
          "This program returns a file containing an accession list subset of the size given.\n"
          "\nPlease press the \"spacebar\" and \"enter\" to continue, or \"q\" to quit.\n")

    # this flag becomes false when we want to quit the program
    main_flag = True

    while main_flag:

        # status flags to control flow of execution
        entry_flag = False
        exit_flag = False

        while not entry_flag:
            key = input()
            if (key == " "):
                entry_flag = True
            elif (key == "q"):
                print("Goodbye!\n")
                quit()
            else:
                print("\nPlease press the \"spacebar\" and \"enter\" to continue.\n")

        USER_INPUT_PATH = raw_input("Please input the path of the accession list: \n")

        assert os.path.exists(USER_INPUT_PATH), "The program did not find the file at, " + str(USER_INPUT_PATH)
        FILE = open(USER_INPUT_PATH, 'r')
        print("Hooray we found your file!")
        print("The program is fetching snippet occurrence stats about your input file.\n")

        # stuff you do with the file goes here
        # FILE is the file
        # FILE contains the accession list, and nothing else.
        # This accession list is obtained from the website mentioned in comments above.
        # This is a constant because we do not want the file to change while selecting a subset from the file!

        # store input file as a string
        seq_str = FILE.read()
        # close file after getting string content
        FILE.close()

        snippet_map = get_ID_sequence_map(seq_str)
        s_o_map = map_snippet_occurrence(snippet_map)

        print(snippet_map)
        print(snippet_occurrences_between_two_sequences(s_o_map, '_QRU91014.1', '_QRU91938.1'))
        print(s_o_map)
        print(snippet_occurrences_between_two_sequences(s_o_map, '_QRU91938.1', '_QRU91014.1'))
        print(ratio_of_snippet_occurrences_to_sequence_length(s_o_map, '_QRU91938.1', '_QRU91014.1'))

        print("Do you want to run Snippet Occurrence for another file? Type Y\\N:\n")
        while not exit_flag:
            exit_input = input()
            if exit_input == 'Y':
                exit_flag = True
            elif exit_input == 'N':
                exit_flag = True
                main_flag = False
            elif exit_input == 'q':
                quit()
            else:
                print("I don't recognize that input. Do you want to rerun Snippet Occurrence? Please type Y\\N:")
"""
Write a python program that takes input
Input: A dataset such as one found on
https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049
Input: Also, a given sample size

See: https://thispointer.com/5-different-ways-to-read-a-file-line-by-line-in-python/

and produces Output: A random sampling of the input dataset of size sample_size

The input is? A bunch of .FASTA files.
and An integer, size, that gives the size of the output subset of sequences.
"""

import numpy as np
import sys
import os
from pipenv.vendor.distlib.compat import raw_input
import random


def subset_selector(file, subset_size):
    """
    :param file: the file from which to select a subset of accession values
    :param size: the size of the subset of accession values
    :return: a subset of the accession values
    """

    # subset_size starts out as a string when we first get it from user input, so
    # cast it as an integer
    subset_size_as_integer = int(subset_size)

    # declare and initialize the subset to return
    subset_list = list()

    # Put all the lines from the input file into a list, the accession list
    list_of_lines = list()

    with file:  # with the file that has been opened outside the scope of this function declaration,
        for line in file:  # for every line in the input file
            list_of_lines.append(line.strip())  # append the line to the accession list

    # declare and initialize variable list_of_lines_length to keep track of the highest index value in range for
    # the accession list
    list_of_lines_length = len(list_of_lines)

    # declare and initialize a list of random numbers with values in range [0, list_of_lines_length))
    # this list of random numbers are random index values that will each point to a random line of the file,
    # which corresponds to a random accession in the accession list
    random_indices = random.sample(range(0, list_of_lines_length), subset_size_as_integer)

    for i in random_indices:  # for each element in the list of randomized indices of the accession list,
        subset_list.append(list_of_lines[i])  # append a random entry in the accession list to the subset

    return subset_list  # return the subset


# Press the green button in the gutter to run the script.
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




        SUBSET_SIZE = input("Please input the size of the accession sublist: \n")

        # Input specifies location of the file
        USER_INPUT_PATH = raw_input("Please input the path of the accession list: \n")

        assert os.path.exists(USER_INPUT_PATH), "The program did not find the file at, " + str(USER_INPUT_PATH)
        FILE = open(USER_INPUT_PATH, 'r+')
        print("Hooray we found your file!")
        print("The program is fetching a subset accession list of size " + str(SUBSET_SIZE) + " for you.\n")
        # stuff you do with the file goes here
        # FILE is the file
        # FILE contains the accession list, and nothing else.
        # This accession list is obtained from the website mentioned in comments above.
        # This is a constant because we do not want the file to change while selecting a subset from the file!

        print(subset_selector(FILE, SUBSET_SIZE))

        FILE.close()

        print("We found a subset for you. Do you want another? Type Y\\N:\n")
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
                print("I didn't recognize that input. Do you need another subset? Please type Y\\N:")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

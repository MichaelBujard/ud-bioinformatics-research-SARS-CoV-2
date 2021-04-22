import os
import sys

new_file = open("data_parsed.txt", "w")

with open("data.txt") as file:
    new_file = open("data_parsed.txt", "w")
    for line in file:
        new_file.write(line.replace("snippet occurrences between ", "").replace(" and", "").replace(" are ", ""))
file.close()

# we have finished reading from the original file from the data dump.
# Now, the new file, i.e. data_parsed.txt or "new_file" is still open.
# we need to close it.
new_file.close()

"""
with open("data_parsed.txt", "w") as new_file: # open the file for writing
    for line in lines:
        first_outer_accessionID, second_outer_accessionID = line.split()[0], line.split()[1]
        for inner_line in new_file:
            first_inner_accessionID, second_inner_accessionID = inner_line.split()[0], inner_line.split[1]
            if first_outer_accessionID == second_inner_accessionID:
                if second_outer_accessionID == first_inner_accessionID:
"""

new_file = open("data_parsed.txt", "r")
file = open("data.txt", "r")
new_file.seek(0)
file.seek(0)
new_file_content = new_file.read()
file_content = file.read()
new_file.close()
file.close()

print(file_content)
print(new_file_content)


# OK, we have parsed the data a little and put it into another file.
# Now we need to parse the data further by removing duplicate entries.

# now, we need to open the new file (redundant, but I'm not sure yet how else to do it)
# and then loop over twice to remove duplicate entries.

a_file = open("data_parsed.txt", "r")
lines = a_file.readlines()
a_file.close()

new_file = open("data_parsed_no_repeats.csv", "w")
new_file.write("SEQUENCE_PAIRS" + "," + "AA_MISMATCHES" + "\n")
for i in range(len(lines)):
    line_lst = lines[i].strip("\n").split()
    #print("outer loop", line_lst)
    first_outr_accn_id, second_outr_accn_id = line_lst[0], line_lst[1]
    for j in range(i, len(lines)):
        if i != j:
            inner_line_lst = lines[j].strip("\n").split()
            first_innr_accn_id, second_innr_accn_id = inner_line_lst[0], inner_line_lst[1]
            if first_outr_accn_id == second_innr_accn_id:
                if second_outr_accn_id == first_innr_accn_id:
                    if lines[i].strip("\n").split()[2] != '0':
                        lst = lines[i].strip("\n").split()
                        new_file.write(lst[0] + "_" + lst[1] + "," + lst[2] + "\n")



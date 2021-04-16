import os
import sys

new_file = open("data_parsed.txt", "w")

with open("data.txt") as file:
    new_file = open("data_parsed.txt", "w")
    for line in file:
        new_file.write(line.replace("snippet occurrences between ", "").replace(" and", "").replace(" are ", ""))
new_file.close()
file.close()

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

"""
Script for fetching data from the internet


1. read in text files
2. concatenate files into one?
3. remove grammar
4. set all words to lowercase
5. separate by ' ' to produce a list

"""
import os
filenames = os.listdir('inaugural/')
# print (filenames)

def get_text():
    with open('concatenated.txt', 'w') as outfile:
        for fname in filenames:
            path = 'inaugural/' + fname
            with open(path) as infile:
                for line in infile:
                    outfile.write(line)

def set_text():
    open_file = open('concatenated.txt')
    return open_file
    # print (base_text)

print (set_text())

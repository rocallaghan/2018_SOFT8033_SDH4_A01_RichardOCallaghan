#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs




# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def process_line(line):
    # 1. We get rid of the end line character
    line = line.replace('\n', '')

    # 2. We strip any white character at the end
    line = line.rstrip()
    line = line.rstrip('\t')

    # 3. We strip any white character at the begining
    line = line.strip()
    line = line.strip('\t')

    # 4. We split the info by tabulators or white spaces
    line = line.replace('\t', ' ')
    words = line.split(' ')

    

    return words

def get_index_in_alphabet(letter):
    # 1. We put an index of -1 by default
    index = -1

    # 2. If the letter is an uppercase or lowercase letter, we update index to its position in the alphabet
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        index = ord(letter) - ord('a')
    if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
        index = ord(letter) - ord('A')

    # 3. We return the index
    return index

def my_map(input_stream, languages, num_top_entries, output_stream):
    lista = []
    i = 0
    diction = {}
    for line in input_stream:
        word_list = line.split(" ")
        if((word_list[0][:2] == languages[0]) or (word_list[0][:2] == languages[1]) or (word_list[0][:2] == languages[2])):
            i = i+1
            lista.append( [word_list[0], word_list[1], int(word_list[2])] )
            lista.sort
        
    for words in lista:
        if words[0] in diction:
            diction[words[0]].append([words[1],words[2]])
        else:
            diction[words[0]] = [[words[1],words[2]]]
            
    for i in diction:
        for index in range(0,5):
            if len(diction[i]) > index:
                diction[i].sort(key=lambda x: x[1], reverse=True)
                output_stream.write(i + "\t" + diction[i][index][0] + "," + str(diction[i][index][1]) + "\n")
    pass

    

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, languages, num_top_entries):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug == True:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout
    print(my_output_stream)
    # We launch the Map program
    my_map(my_input_stream, languages, num_top_entries, my_output_stream)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Input parameters
    debug = True

    i_file_name = "pageviews-20180219-100000_0.txt"
    o_file_name = "mapResult.txt"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, languages, num_top_entries)




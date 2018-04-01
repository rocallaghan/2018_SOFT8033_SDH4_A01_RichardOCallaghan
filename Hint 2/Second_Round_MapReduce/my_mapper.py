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
def my_map(input_stream, per_language_or_project, output_stream):
        lista = []
        total = 0
        dict = {}

        for text_line in input_stream:
            single = text_line.split()
            term = single[0];
            
            if '.' in term:
                term = single[0].split('.')[1]
                if per_language_or_project == True:
                    term = single[0].split('.')[0]
            elif not per_language_or_project:
                term = "wikipedia"
            if term not in dict:
                dict[term] = 0
            try:
                dict[term] += int(single[-2])
            except:
                dict[term] += int(single[1])
        for key in dict:
            output_stream.write(key + "\t" + str(dict[key]) + "\n")
     
        pass


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, per_language_or_project):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug == True:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # We launch the Map program
    my_map(my_input_stream, per_language_or_project, my_output_stream)

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

    per_language_or_project = True # True for language and False for project

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, per_language_or_project)

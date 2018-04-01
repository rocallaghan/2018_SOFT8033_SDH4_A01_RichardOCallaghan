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

def splitdata(x):
  splitter = x.split(" ")
  res = splitter[0]+"\t("+splitter[1]+", "+splitter[2]+")"
  return result

def sorter(x):
  split = x.split("\t")
  return split[0]
# ------------------------------------------
# FUNCTION my_sort
# ------------------------------------------
def finalsorting(x):
  res = []
  for i in range(0,num_top_entries):
    res.append(("",0))
  for ele in x:
    split = ele.split(", ")
    pageViews =int(split[1].replace(")","",1)) 
    if  pageViews > res[4][1]:
      pageNameSplit=split[0].split("\t")
      pageName=pageNameSplit[1].replace("(","",1)
      res[4]=(pageName,pageViews)
      res.sort(key=lambda value:value[1],reverse=True)
  return res  

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(dataset_dir, o_file_dir, languages, num_top_entries):
    # 1. We remove the solution directory, to rewrite into it
    dbutils.fs.rm(o_file_dir, True)

    filesin = sc.textFile(dataset_dir)
    parseddata = filesin.map(splitdata)
    sorteddata = parseddata.groupBy(sorter)
    finaldata = sorteddata.mapValues(finalsorting)
    finaldata.saveAsTextFile(output)
    

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    dataset_dir = "/FileStore/tables/A01_my_dataset/"
    o_file_dir = "/FileStore/tables/A01_my_result/"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    my_main(dataset_dir, o_file_dir, languages, num_top_entries)
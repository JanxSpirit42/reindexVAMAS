# reindexVAMAS
A script to re-order VAMAS blocks for use in XPS Analysis software such as CasaXPS, no more manually setting blocks!

## Description:
   This script will read a ESCA VAMAS file (.vms) and attempt to re-index the blocks so that each element 
   region and survey of the same pass energy for a sample is on the same row. It is very limited and will only
   work for VAMAS files where every scan set up is similar, so have a little play. It works well when you have
   hundreds scans and have to manually set the index of each block to the same row for each sample.
   David O'Connor 2018

## Comments:
  v0.3 is set up so that you can run it from CMD in windows. 
  Make sure python is added to the console path.
  Python Version: 3.6.1
  
## Instructions for use:
  1. Put the .vms file you want to reindex into the same folder as VAMASreindex_v0.3.py
  2. Open up the command line, then navigate to the folder the file is in using the "cd" command, "dir" and tab will help.
  3. Yype the following in: python VAMASreindex_v0.3.py YOURFILENAME.vms

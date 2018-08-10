# reindexVAMAS
A python script to re-order VAMAS blocks for use in XPS Analysis software such as CasaXPS, no more manually setting blocks!

## Description:
   This script will read a ESCA VAMAS file (.vms) and attempt to re-index the blocks so that each element 
   region and survey of the same pass energy for a sample is on the same row. It is very limited and will only
   work for VAMAS files where every scan set up is similar, so have a little play. It works well when you have
   hundreds scans and have to manually set the index of each block to the same row for each sample.
   
## Comments:
  v0.4 is set up so that you can compile it with pyinstaller and run a standalone .exe
  Python Version: 3.6.1<br />
  
## Instructions for use:
  1. Put the .vms file you want to reindex into the same folder as VAMASreindex_v0.4.exe
  2. Run the application
  3. Type the file name in to be reindexed into the window
 

#   This script will read a ESCA VAMAS file (.vms) and attempt to re-index the blocks so that each element 
#   region and survey of the same pass energy for a sample is on the same row. It is very limited and will only
#   work for VAMAS files where every scan set up is similar, so have a little play. It works well when you have
#   hundreds scans and have to manually set the index of each block to the same row for each sample.
#   David O'Connor 2018

import sys


#   CMD line parameters and function:
if len(sys.argv) != 2:
    print('Needs an input file name')
    exit(1)
    
inputFile = sys.argv[1]
outputFile = 'ReIndexed_'+inputFile

#   Main block:
lines = [line.rstrip('\r\n') for line in open (inputFile)]

currentIndex = 0
blockLabel = ''

for index, line in enumerate(lines):

    #    XPS is 15 lines after a new scan starts, this potentially changes so for now you may need to open your
    #   .vms files in word and work out if it is also 15lines or a different amount.
    if line == 'XPS':
        #   Find the name of the scan
        label = lines[index-10]     
        
        if blockLabel == '':         
            blockLabel = label
        #   Iterate the row index
        if blockLabel == label:
            currentIndex += 2
            scanIteration = '0'             # e.g. 1: O 1s, 2: O 1s
        #   For the special case where multiple pass energy scans have been run on the same region e.g "O 1s",
        #    "1: O 1s", "2: O 1s" 
        else:
            split = label.partition(':')    # If the label has a ':' in it split it into a [3]  
            
            try:
                #   Check for colon, check there is a number to the left of the colon, check the number isn't
                #   already the scan iteration
                if split[1] == ':' and int(split[0]) and split[0] != scanIteration:     
                    scanIteration = split[0]
                    currentIndex += 2
            except:
                pass                        
        lines[index+1]=currentIndex

#   Write new file
outputFile=open(outputFile,'w')
#   Add CR and LF to the new file
for line in lines:                          
    outputFile.write('%s\r\n' % line)   
        

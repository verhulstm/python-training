#------------------------------------------------------------------------------
#           Name: search_directory.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use os.path.walk()
#                 and a call-back function to recursively walk through a 
#                 directory hierarchy and list everything found.
#------------------------------------------------------------------------------

import os

#------------------------------------------------------------------------------
# Name: directoryWalker()
# Desc: Call-back function for use with os.path.walk()
#------------------------------------------------------------------------------
def directoryWalker( unused, dirName, nameList ):
    
    print "Entering new directory: " + dirName
    
    for entry in nameList:
	print "    " + os.path.join( dirName, entry ) # Append path to file name and print
        
    print " "

#------------------------------------------------------------------------------
# Script entry point...
#------------------------------------------------------------------------------

if __name__ == '__main__':
    
    os.path.walk( os.curdir, directoryWalker, None )

    raw_input( '\n\nPress Enter to exit...' )

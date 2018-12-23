#------------------------------------------------------------------------------
#           Name: string_split.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to split a string into
#                 tokens based on some delimiter like a comma.
#------------------------------------------------------------------------------

import string

str = "one,two,three,four,five"

print "str = " + str
print

tokens = string.split( str, ',' )

for i in range( len(tokens) ):
    print "token %d = %s" % ( i, tokens[i] )

raw_input( '\n\nPress Enter to exit...' )

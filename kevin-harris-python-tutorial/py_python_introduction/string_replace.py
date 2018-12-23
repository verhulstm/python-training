#------------------------------------------------------------------------------
#           Name: string_replace.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to 
#------------------------------------------------------------------------------

import string

str = 'one two three four'

print "Before: " + str

str = string.replace( str, 'one', '1' )
str = string.replace( str, 'two', '2' )
str = string.replace( str, 'three', '3' )
str = string.replace( str, 'four', '4' )

print "After: " +  str

raw_input( '\n\nPress Enter to exit...' )

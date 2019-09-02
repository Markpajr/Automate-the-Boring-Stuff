# DONE: Write a function that does the same as strip()
# DONE: Include 2 arguements. If only the string is passed, strip white spaces
#       Else strip characters specified in second arguement


import re

# Creates strip function


def nstrip(strip_string, strip_char=''):
    # if a strip_char has been provided, use this first regex
    if strip_char != '':
        # Regex checks either the beginning for atleast 1 strip_char (+), then any character(*)
        # Or the end, atleast 1 (+) strip_char preceded by any character (*)
        stripRegex = re.compile(r'^[' + strip_char + ']*|[' + strip_char + ']*$')
        # Prints strip_string, substituting '' for the preceding regex matches
        print(stripRegex.sub('', strip_string))
    else:
        # Creates regex searching for spaces at the beginning or end
        emptyRegex = re.compile(r'^(\s)*|(\s)*$')
        # Prints the strip_string substituting '' for the spaces
        print(emptyRegex.sub('', strip_string))


nstrip('%%%This is a test%%%', '%')
nstrip('     This is a test        ')

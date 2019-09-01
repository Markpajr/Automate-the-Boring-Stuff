'This is bob\'s mother'  # \ Before the single quote is used as an "Escape character" to allow the single quote to be part of the string without causing an error
# \n can be used to add a new line
print('Hello\nHow are you?')

# Triple quotes can also be used for new lines

print('''Hello,
How are you doing?
I am doing fine, what bout you?''')

# In/Not In and indexing can be used on strings as well
hi = 'hello how are you'
hi[6]  # This returns the letter h at the 6th index of the string
'how' in hi  # This returns True because How is in the string hi
'h' not in hi

# String values are immunable and can't be modified in place. When you use methods on a string, the original string is not changed

stringtest = 'Hello World!'
print(stringtest.upper())  # Returns the string in all uppercase
print(stringtest.lower())  # Returns the string in all lowercase

# String method .islower()/.isupper() returns boolean values based on the case of the string

# Additional boolean string methods are:
# isaplha() string contains only letters
# isalnum() letters and numbers
# isdecimal() numbers
# isspace() whitespace
# istitle() title characters eg. Hello

# .startswith is boolean for starting characters of a strings
# Similarly, endswith can be used for ending

# join method is called on a string, passed a list of string, and creates one string using the called string a separator
','.join(['cats', 'rats', 'bats'])
# split method splits a string into a list based on the character called
'this is a sentance'.split()

#rjust/ljust inserts spaces to left or right justify a string, making it's total length = to whats passed to the methods
'Hello'.rjust(15)

'Mark'.center(20, '=')

# strip method removes whitespace or fill characters from each side of the string
# replace can replace parts of a string like find and replace


# Conversion splicers can be used to more easily concatenate complex strings

name = 'Mark'
place = 'main street'
time = '6pm'
food = 'pizza'

'Hello %s, you are invited to a party at %s on %s. Please bring %s.' % (name, time, place, food)

# Regular expressions can be used to easily find patterns instead of writing complex code

import re
message = 'Call me at 742-242-1231 tomorrow, or at my office line: 129-313-4524'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # r is raw string format so the regex can use backslashes without creating a new line
mo = phoneNumRegex.search(message)  # Search finds the first matching string
print(mo.group())  # Group method returns the matched object found by search method

print(phoneNumRegex.findall(message))  # Findall returns a list of found strings
# Findall returns a list of tuples if used on any regex that has 2 or more groups in it

# Regex definitions can be grouped to allow separation of the search strings
phonenumregex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phonenumregex2.search('My number is 415-444-5555')
mo2.group(1)
mo2.group(2)

# The pipe character | can be used to separate partial matches

batRegex = re.compile(r'bat(man|mobile|copter|arang|bat)')
mobat = batRegex.search('The batmobile')
mobat.group()


# ? Says match preceding group either 0 or 1 time
batmanRegex = re.compile(r'bat(wo)?man')

# ? Can be used to create optional parts of the regex search
# For example, r'(\d\d\d)?-\d\d\d-\d\d\d\d' returns a phone number with or without an area code

# * says match 0 or more times

# + means match 1 or more, requires group preceding to appear atleast once

# {x} can be used to match exactly x number of times
# {x,y} can be used to match a range with a min x and max y times

# Python by default does "Greedy" matching, to match the longest possible string. To do a non-greedy match, put a ? after the {3,5} to match the smallest possible string
digitRegex = re.compile(r'(\d){3,5}')
md = digitRegex.search('1234567890')
print(md.group())

# The Following are common character classes that can be used to make Regex functions
# \d Any Numeric Diget from 0-9
# \D Any character that is NOT a numeric digit from 0-9
# \w Any letter, numeric digit, or underscore character ("Word characters")
# \W Any character that is NOT a letter, numeric digit, or underscor character
# \s Any space, tab, or newline character
# \S Any character that is NOT a space, tab, or newline character

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4calling birds, 3 french hens, 2 turles doves, and 1 partridge in a pear tree'

# Following regex fines 1 or more number, a space, then 1 or more letters
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall(lyrics)

# You can also create custome regex character classes using []
# Can also insert ranges this way, ie [a-z] would return all lowercase letters
# [a-fA-F] would return all lowercase and capital letters a through f

vowelRegex = re.compile(r'[aeiouAEIOU]')  # Gives all vowels

vowelRegex.findall(lyrics)

# ^ Can be used to create a negative character class, returning the opposite

consenantRegex = re.compile(r'[^aeiouAEIOU]')  # Finds any non aeiou characters

# If you use ^ at the beginning of a regex, it requires the returned value to be at the beginning of the search term
beginswithHelloRegex = re.compile(r'^Hello')

beginswithHelloRegex.search('Hello how are you?')

beginswithHelloRegex.search('He said Hello') == None

# Similarly, using $ at the end of a regex returns only values that end in the regex

endswithWorldRegex = re.compile(r'world!$')

endswithWorldRegex.search("Hello world!")

# . can be used as a wildcard to return any character except for new line \n
# .* Can be used to find anything

name = 'First Name: Jack Last Name: Johnson'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

nameRegex.findall(name)

# re.compile(r'.*',re.DOTALL) The second arguement, re.DOTALL, can be used to make the . match everything, including new lines

# Similar to re.DOTALL, re.IGNORECASE can be used to perform case insensitive matching

# sub() can be used as find and replace

agentRegex = re.compile(r'Agent \w+')
agents = 'Agent bob shot Agent alice in the foot in front of Agent john'
agentRegex.findall(agents)
agentRegex.sub('Redacted', agents)

# Grouping can be used with the Sub method and \groupnumber to return the group referenced in the substitution
agentsRegex = re.compile(r'Agent (\w)\w*')
agentss = 'Agent bob shot Agent alice in the foot in front of Agent john'
agentsRegex.findall(agentss)
agentsRegex.sub(r'Agent \1', agentss)

# re.VERBOSE mode can be used to make regexes more readable

ReadablePhoneRegex = re.compile(r'''
\d\d\d   # Area Code
-        # First Dash
\d\d\d   # First 3 Digits
-        # Second Dash
\d\d\d\d # Last 4 digits''', re.VERBOSE)

ReadablePhoneRegex.findall('315-965-2137')

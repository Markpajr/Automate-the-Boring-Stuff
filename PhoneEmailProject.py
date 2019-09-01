#! python3

import re
import pyperclip
import pprint

# Create a regex for phone numbers
phoneNumRegex = re.compile(r'''
# Number Types: 555-555-5555, (555) 555-5555, 555-5555, 555-5555 ext 12345, ext.12345,x12345
(((\d{3}) | (\(\d{3}\)))?             # Area Code (Optional)
(-|\s|\.)?                                 # First separater
(\d{3})                                 # First 3 digits
(-|\s|\.)?                                 # Seperator
\d{4}                               # Last 4 digits
(((ext(\.)?\s)|x)                      # Extension Word
    (\d{2,5}))?                        # extension number)
)''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# Email Type : some.+_thing@something.com/edu/gov/etc

[a-zA-Z.+_]+        # Name Part
@                   # @ Symbol
[a-zA-Z.+_]+        #Domain name part
''', re.VERBOSE)
# DONE: Get the text off the clipboard
text = pyperclip.paste()


# DONE: Extract the emails/phones from this text
extractedPhone = phoneNumRegex.findall(text)
extractedEmail = emailRegex.findall(text)


allPhoneNumbers = []
for phonenumber in extractedPhone:
    allPhoneNumbers.append(phonenumber[0])

# DONE: Copy the extracted emails/phones to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# resultsDict = dict(zip(allPhoneNumbers, extractedEmail))

pyperclip.copy(results)

# pprint.pprint(resultsDict)

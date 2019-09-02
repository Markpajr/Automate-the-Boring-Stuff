import re
import pyperclip
# DONE: Write Function to detect password strength
# DONE: Use Reg Ex to determine if password is strong
# DONE: Get password from clipboard
# DONE: Strong password : 8+ Char Length, Upper & lower, 1 digit
# TODO: Pull list of passwords from excel and test strength
# TODO: Output strength list back to excel
# TODO: Improve strength to 16 characters, one special character
# TODO: Generate random list of passwords

upperRegex = re.compile(r'[A-Z]+')
lowerRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')


def passwordstrength(password):

    return bool(len(password) >= 8 and upperRegex.search(password) and lowerRegex.search(password) and digitRegex.search(password))


passTest = passwordstrength(pyperclip.paste())

if passTest is True:
    print("Strong Password")
else:
    print("Weak Password")

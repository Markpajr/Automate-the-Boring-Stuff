import string
import random
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
punctRegex = re.compile(r'\W+')


def passwordstrength(password):

    return bool(len(password) >= 16 and upperRegex.search(password) and lowerRegex.search(password) and digitRegex.search(password) and punctRegex.search(password))


passTest = passwordstrength(pyperclip.paste())

if passTest is True:
    print("Strong Password")
else:
    print("Weak Password")

# Creates a list of 15 randomly generated passwords.
# 10-36 Characters including punctuation, Upper/Lower letters, and Digits
randPassList = []
for i in range(0, 15):
    randPass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(random.randint(8, 36))])
    randPassList.append(randPass)

for password in range(len(randPassList)):
    randTest = passwordstrength(randPassList[password])
    if randTest is True:
        print("Strong Password")
    else:
        print("Weak Password")

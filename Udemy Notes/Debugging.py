# Raising exceptions
# Can be used to raise custom error messages
"""
The following code will crash the program with an error message
raise Exception('Example of error message')
"""


def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"Height" and "Width" must be greater than 1')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)

    print(symbol * width)


boxprint("%", 1, 15)

"""
Error message returned is called a traceback.
This traceback gives you the line the error was on, and the function causing it
Errors can be written to a log file using the traceback module
This can allow you to keep a program running but log errors
import traceback
try:
    raise Exception('Error message')
except:
    errorFile = open('Error_Log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt)

"""

# Assertions: Sanity check to make sure code isn't doing anything wrong
# Assertion: This statement I add will alays be true, otherwise there is a bug in the program
# Stoplight example
market_2nd = {"ns": "green", "ew": "red"}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
            intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"
    assert "red" in intersection.values(), "Neither light is red!" + str(intersection)


print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

"""
Assertions are meant to find programmer errors not meant to be recovered from.
For user errors, raise exceptions for the user to fix
"""

"""
Setup code for logging in python:
import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s-%(levelname)s-%(message)s')
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(levelname)s-%(message)s")
logging.disable(logging.CRITICAL) # Disables the log messages, can re-enable by commenting out
# There are 5 levels of logging, Debug, Info, Warning, Error, Critical
# Logging messages can be changed to show different levels
# To write log messages to a file, add filename = 'Logging.txt' to the beginning of the basic config
logging.debug ('Start of program')
def factorial(n):
    logging.debug(f'Start of facorial {n}')
    total = 1
    for i in range(1, n + 1): # Original: range(n+1) Started at 0, causing error
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    
    logging.debug(f'Return value is {total}')
    return total

print(factorial(5))

logging.debug('End of program')
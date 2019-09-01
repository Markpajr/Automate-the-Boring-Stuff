#! python3
# First line of python script should be a "Shebang line" which is #! python3 on windows
import sys
print('Hello World')

# Create a new windows batch file, a txt file with the .bat extension. Use the following lines to run the code

# @py "C:\Users\Owner\Documents\Programming\Python\Practice\Automate the Boring Stuff\Running a program outside IDLE.py" %*
# @pause

# To run the code without showing a cmd prompt, ust following

# @pyw "C:\Users\Owner\Documents\Programming\Python\Practice\Automate the Boring Stuff\Running a program outside IDLE.py" %*


print(sys.argv)

#! python3

import webbrowser, sys, pyperclip

sys.argv  #

# Check if command line arguements were passed

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')

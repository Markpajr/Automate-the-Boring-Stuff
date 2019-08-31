import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
pprint.pprint(count)  # Print using pretty print modules pprint funtion to get a nicer print output, puts dictionary in order
# pformat can output the dictionary as a string

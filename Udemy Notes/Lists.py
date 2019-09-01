

import copy
friends = ['mike', 'chloe', 'ed', 'ben', 'kaye', 'patrick', 'JC', 'Emma']

for i in range(len(friends)):  # For loops are equivalent to looping through a list
    print('Friend number ' + str(i+1) + ' is named ' + friends[i])

# Multiple assignment can be used to assign multiple variables at once to a list, or comma deliminated variable list ie one,two = 1,2.
smallman, gremlin, britishdetective, farmboy, meinu, richguy, richguy2, emma = friends

print(gremlin)


spam = 42
spam += 1  # Augmented operaters can be used to create iterative variables. This line is equivalent to spam = spam +1

print(spam)

greetings = ['hello', 'hi', 'howdy', 'heya']
greetings.index('hello')  # index returns the index for the specified value in the list

greetings.append('Whats up')  # Append adds a value to the end of the list
print(greetings)

greetings.insert(1, 'Nihao')  # Instert adds a value to the list at the specified index
print(greetings)

friends.sort(key=str.lower)  # Key = str.lower is necessary to sort in alphabetical order ignoring Caps

print(friends)

# Strings are considered lists and can have operations done on them, but they can't be changed like normal lists
myName = 'Mark'

for letter in myName:
    print(letter)

# To modify a string it's necessary to creat a new variable and use list slicing
string1 = 'Kaye wants a potato'
string2 = string1[0:5]+'is'+string1[10:]
print(string2)

# Lists store a reference to a list, and when you call the list it copies the reference. Any changes to this list change the original list in the computers memory
spam = [1, 2, 3, 4, 5, 6]  # This creates the list spam in the computers memory
cheese = spam  # This copies the reference to the spam list to the cheese variable
cheese[1] = 'hello'  # This changes the item at index 1 to hello inside the spam list through the reference in cheese
print(spam)  # This prints spam, which is now changed from the original list

# To make a full copy of the list, import the copy module and use the function copy.deepcopy(Lists)
copylist = ['a', 'b', 'c']

copylist2 = copy.deepcopy(copylist)
copylist2[1] = 'cheese'
print(copylist)
print(copylist2)


# Line continuation can be done with \

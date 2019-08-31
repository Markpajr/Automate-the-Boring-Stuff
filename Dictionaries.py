# Dictionaries are like lists, dictionaries can use many data types. Indexes are called keys
# Dictionary variables are also references, like lists
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])  # You can call keys in a dictionary similarly to the way you call Indexes in a list

print('My cat has ' + myCat['color']+' fur.')  # Dictionary keys can also be concatenated the same way

# Dictionaries are unordered, While [1,2,3] == [3,2,1] is false, {'name':'Bob', 'color':'purple'} == {'color':'purple','name':'bob'} is true

print([1, 2, 3] == [3, 2, 1])
eggs = {'name': 'Bob', 'color': 'purple'}
hame = {'color': 'purple', 'name': 'Bob'}
print(bool(eggs == hame))

list(eggs.keys())  # Returns all keys in the dictionary
list(eggs.values())  # Returns all values in the dictionary
list(eggs.items())  # Returns all items in the dictionary as a list with two item tuples
# Tuples are like lists, immunable and use parenthesis

for k in eggs.keys():
    print(k)

for k, v in eggs.items():
    print(k, v)

# You can use get in and not in to check whether a key is in a Dictionary
# This will return an error, to check without getting an error use get
# dictionary.get('KEY','Value if Key not found')
eggs.get('level', 'Not in dictionary')

# Set default sets keys value if it doesn't already exist
hame = {'color': 'purple', 'name': 'Bob'}
hame.setdefault('color', 'black')  # Will return 'Purple' since color exists in hame
hame.setdefault('towel', 'green')  # Will return 'green', adding the 'towel' key to the hame dictionary
for k, v in hame.items():
    print(k, v)

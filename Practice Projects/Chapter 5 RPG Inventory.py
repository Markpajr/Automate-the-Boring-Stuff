# DONE Write function displayInventory() to take invnentory dictionary and display in a multiline output

test = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
stuff = test

# Funtion to print the Dictionary
# inventory.items() creates a list of tuples based on the dictionary, with item,quantity referencing the corresponding tuple values


def displayInventory(inventory):
    print('Inventory:')
    for item, quantity in inventory.items():
        print(str(item) + ' ' + str(quantity))
    item_total = len(inventory.keys())  # Counts the number of keys in the dictionary using length
    quant_total = sum(inventory.values())  # Adds together every value in the dictionary
    print('Total Inventory Items:' + str(item_total) + '\n' + 'Total inventory Quantity: ' + str(quant_total))


displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    print("Inventory:")
    for newitem in addedItems:
        itemcount = inventory.get(newitem, 0) + 1  # Gets the corresponding dictionary value at newitem key, if key doesn't exist creates it with value 0
        inventory[newitem] = itemcount  # Sets the key new item with the value itemcount
    for items, quantity in inventory.items():
        print(str(items) + " " + str(quantity))
    print('Total Inventory Items:' + str(len(inventory.keys())) + '\n' + 'Total inventory Quantity: ' + str(sum(inventory.values())))

# Alternative, use inventory.setdefault(newitem, 0) and inventory[newitem] +=1


addToInventory(stuff, dragonLoot)

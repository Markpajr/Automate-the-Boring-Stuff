# DONE: Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
# #Assume that all the inner lists will contain the same number of strings.


def printTable(inputList):
    '''
    This funtion takes a list of lists containing strings as inputs. It will then output a nright justified organized table from the strings, one column for each list and one row for each string.
    '''

    colWidths = [0] * len(inputList)  # Creates a list of 0's based on the length of the inputList
    # Loops all indexes in inputList (0:3)
    for innerlist in range(len(inputList)):
        # Loops all indexes in each innerList (0:5)
        for item in range(len(inputList[innerlist])):
            # Checks length of each item vs col length
            if len(inputList[innerlist][item]) >= colWidths[innerlist]:
                colWidths[innerlist] = len(inputList[innerlist][item])
    # Loops based on number of indexes in first innerList (0:5)
    for a in range(len(inputList[0])):
        for b in range(len(inputList)):  # Loops based on number of indexes in inputList (0:3)
            # Prints each index [Innerlist][item] and right justifies
            print(inputList[b][a].rjust(colWidths[b]), end=" ")
        print('')  # Prints a new line for each innerList


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

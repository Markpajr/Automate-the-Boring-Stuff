# TODO: Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.


def printTable(inputList):
    '''
    This funtion takes a list of lists containing strings as inputs. It will then output a nright justified organized table from the strings, one column for each list and one row for each string.
    '''
    colWidths = [0] * len(inputList)  # Creates a list of 0's based on the length of the inputList
    for innerlist in range(len(inputList)):  # Loops all indexes in inputList (0:3)
        for item in range(len(inputList[innerlist])):  # Loops all indexes in each innerList (0:5)
            if len(inputList[innerlist][item]) >= colWidths[innerlist]:  # Checks length of each item vs col length
                colWidths[innerlist] = len(inputList[innerlist][item])
    for a in range(len(inputList[0])):  # Loops based on number of indexes in first innerList (0:5)
        for b in range(len(inputList)):  # Loops based on number of indexes in inputList (0:3)
            print(inputList[b][a].rjust(colWidths[item]), end=" ")  # Prints each index [Innerlist][item] and right justifies
        print('')  # Prints a new line for each innerList


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

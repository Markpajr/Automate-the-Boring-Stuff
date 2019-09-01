# DONE: Write function Collatz(). One Parameter: Number. If number even, print number/2. If odd, print number *3+1
# DONE: Make program allow user to type integer. loop collatz on integer until result is 1.


def Collatz(number):
    if number % 2 == 0:  # Checks for division by 2 with a remainder of 0 to determine if number is even
        newnumber = number//2
        print(newnumber)
        return newnumber  # Sets the result of the collatz function
    else:
        result = (number*3)+1
        print(result)
        return result


n = input("Please input a number")
print(n)
try:
    while n != 1:  # Runs loop until n = 1
        n = Collatz(int(n))  # Sets n equal to result of Collatz funtion
except ValueError:  # Returns error message if a non-integer is entered
    print("Please enter a number")

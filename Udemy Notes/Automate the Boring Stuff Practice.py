
print('Hello')
print('What is your name?')
myName = input()
print('It is good to meet you ' + myName)
print('The length of your name is')
print(len(myName))
print('what is your age?')
myAge = input()
print('You will be '+str(int(myAge)+1)+' in one year')


spam = 0
while spam < 5:
    print("Hello")
    spam = spam+1

# Adds up all numbers between 0 and 101
total = 0  # starting value of total
for num in range(101):  # For will loop through every number until 101
    total = total + num  # Will add current num to total
print(total)


# sys.exit stops the current program
import sys
print('he')
sys.exit
print('2')

# Pyperclip package helps manipulate the clipboard in windiows
import pyperclip
pyperclip.copy("Yellow")
pyperclip.paste()


def hello():
    print('hello')


hello()


def div42by(num):  # Custom function created to divide 42 by number
    try:
        return 42/num
    except ZeroDivisionError:
        print('Cannot divide by 0')


print(div42by(2))
print(div42by(0))
print(div42by(14))

# Input and if tests with try/except to handle errors
print('How many dogs do you want?')
numDogs = input()
try:
    if int(numDogs) >= 4:
        print('That is not enough dogs')
    elif int(numDogs) < 4 and int(numDogs) >= 0:
        print('You really need more dogs')
    elif int(numDogs) < 0:
        print('You cannt give away your dogs')

except ValueError:
    print('You have to put in a number of dogs')

# Random number guessing game
import random
print('Hello, What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a random number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('You guessed '+str(guess)+' which is too low')
    elif guess > secretNumber:
        print('You guessed '+str(guess)+' which is too high')
    else:
        break
if guess == secretNumber:
    print('Congratulations, ' + name + ', the number I was thinking of was ' + str(secretNumber)
          + '. You took ' + str(guessesTaken) + ' guesses to correctly guess my number')
else:
    print('Idiot, the number I was thinking of was ' + str(secretNumber))

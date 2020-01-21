import random


guess = ""
while guess.lower() not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
if guess.lower() == "tails":
    guess = 0
elif guess.lower() == "heads":
    guess = 1
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = ""
    while guess.lower() not in ("heads", "tails"):
        print("Guess the coin toss! Enter heads or tails:")
        guess = input()
    if guess.lower() == "tails":
        guess = 0
    elif guess.lower() == "heads":
        guess = 1
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")


import random

def sayrules():
    print("I'm going pick a number from 1 to 100. You can guess it, and I'll tell you if you're higher or lower.")

def play():
    print("-"*30)
    sayrules()
    goal = random.randint(1,100)
    playerGuess = -1
    while playerGuess != goal:
        playerGuess = guess()
        compare(playerGuess,goal)

    print(f"Well done! Your guess is correct. My number was {goal}.")
    ask_to_play_again()

def guess():
    return int(input("What is your guess? "))

def compare(guess, goal):
    if guess > goal:
        print("Too high!")
    if guess < goal:
        print("Too low!")

def ask_to_play_again():
    decision = input("Would you like to play again? (y/n)").lower()
    if decision == "y":
        play()
    if decision == "n":
        print("See you next time!")

play()


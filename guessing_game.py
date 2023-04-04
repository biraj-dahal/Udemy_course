import random


def set_lives():
    if input("Enter the difficulty level. Type 'easy' for easy level, and 'hard' for hard level.") == 'easy':
        return 10
    else:
        return 5


def check_guess(guess, actual):
    if guess == actual:
        return True
    elif guess > actual:
        return "Too high.\nGuess Again."
    else:
        return "Too low.\nGuess Again."


def play_game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    lives = set_lives()
    print(f"You have {lives} attempts remaining to guess the number.")
    actual = random.randint(1, 100)
    while lives >0:
        guess = int(input("Make a guess: "))
        if check_guess(guess, actual):
            print(f"You win. You guessed it correct.\nCorrect number was {actual}")
            return
        else:
            print(check_guess(guess, actual))
            lives-=1
            print(f"You have {lives} attempts remaining to guess the number.")
    print(f"You've run out of lives. You lose.\nCorrect number was {actual}")


play_again = True
while play_again:   
    play_game()
    if input("Play Again? Type 'yes' or 'no'.") == 'yes':
        play_again = True
    else:
        play_again = False





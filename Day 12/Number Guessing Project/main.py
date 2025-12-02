from art import logo
import random

number = random.randint(1, 100)
game_is_easy = True

def guesser(point):
    while True:
        if point > 0:
            print(f"You have {point} attempts to guess.")
            guess = int(input("Make a guess: "))
            if guess < number:
                print("Too Low.")
                point -= 1
                continue
            elif guess > number:
                print("Too High.")
                point -= 1
                continue
            elif guess == number:
                print(f"You got it. The number was {number}")
                break
            else:
                print("Invalid Syntax")
        else:
            print("You have run out of guesses, you lose.")
            print(f"The correct number was {number}")
            break

def game():
    global game_is_easy
    print(logo)
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
    chance = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if chance == "easy":
        pass
    elif chance == "hard":
        game_is_easy = False
    else:
        print("Wrong syntax.")
        exit()

    if game_is_easy:
        point = 10
        guesser(point)
    else:
        point = 5
        guesser(point)

if __name__ == "__main__":
    game()


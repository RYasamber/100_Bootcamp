import random
from art import logo, vs
from game_data import data

def compare():
    print(f"\nCompare A: {data[ran_num_a]['name']}, {data[ran_num_a]['description']}, {data[ran_num_a]['country']}")
    print(vs)
    print(f"Against B: {data[ran_num_b]['name']}, {data[ran_num_b]['description']}, {data[ran_num_b]['country']}")

def result():
    a = data[ran_num_a]['follower_count']
    b = data[ran_num_b]['follower_count']
    a_vs_b = input("Who has more followers? Type 'A' or 'B':\n>> ").lower()
    if a_vs_b == "a":
        if a > b:
            return True
        else:
            return False
    elif a_vs_b == "b":
        if b > a:
            return True
        else:
            return False


score = 0
win = False
try:
    while True:
        print(logo)
        if win:
            print(f"You're right! Current score: {score}")
        ran_num_a = random.randint(0, (len(data) - 1))
        ran_num_b = random.randint(0, (len(data) - 1))
        compare()
        if result() == True:
            win = True
            score += 1
            print("\n" * 20)
            continue
        else:
            break

    print(f"Sorry, that's wrong. Final score : {score}")

except ValueError:
    print("Wrong Input")



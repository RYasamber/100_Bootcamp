import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
correct_ltr = []
# TODO-1: - Use a while loop to let the user guess again.
game_over = True
while game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter in correct_ltr:
            display += letter
        elif letter == guess:
            display += letter
            correct_ltr.append(letter)
        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over = False
        print("You Win!!")

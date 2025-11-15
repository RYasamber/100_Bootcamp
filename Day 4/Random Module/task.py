import random
start = input("press \"f\" to flip the coin\n>")
if start == "f":
    if random.random() < 0.5:
        print("Heads")
    else:
        print("Tails")
else:
    print("Why?")
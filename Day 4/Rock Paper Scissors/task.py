import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
g_images = [rock, paper, scissors]
u_pick =int(input("choose one: Rock, Paper or scissors.\n \"0\" for \"Rock\", \"1\" for \"paper\" and \"2\" for \"scissors\"\n>> "))
if 0 <= u_pick < 3:
    print(f"You chose: {g_images[1]}")
c_pick = random.randint(0,1)
if 2 < u_pick < 0:
    print("\nInvalid input")
elif u_pick < c_pick or u_pick == 2 and c_pick == 0:
    print(f"\n Computer picked: {g_images[c_pick]}\n  *You Lost*")
elif u_pick > c_pick or u_pick == 0 and c_pick == 2:
    print(f"\n Computer picked: {g_images[c_pick]}\n  *You Won*")
elif u_pick == c_pick:
    print(f"computer chose: {g_images[c_pick]}\nIts a draw")
else:
    print("\nThats not in the options")
while True:
    try:
        age = int(input("How old are you?"))
        break
    except ValueError:
        print("You have typed invalid type of characters, please try again")
        continue
if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print(f"Sorry, you can't drive at age {age}")
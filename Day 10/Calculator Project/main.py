from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculations = {"+" : add, "*" : multiply, "/" : divide, "-" : substract}
agree = True
number = 0
while True:
    if agree:
        num_1 = float(input("Enter first number:\n>> "))
    if not agree:
        num_1 = number
    for calc in calculations:
        print(calc)
    chosen = input("Pick an operation:\n>> ")
    if chosen not in calculations:
        print("Invalid input.")
        exit()
    num_2 = float(input("Enter next number:\n>> "))

    for calc in calculations:
        if calc == chosen:
            operation = calculations[calc]
            result = operation(num_1, num_2)
            print(f"{num_1} {chosen} {num_2} = {result}")

    options = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start a new calculation: ").lower()
    if options == "y":
        agree = False
        number = result
    elif options == "n":
        agree = True
        print("\n" * 20)
        print(logo)
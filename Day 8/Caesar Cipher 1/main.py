alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(original_text, shift_amount):
    cypher_text = ""
    for text in original_text:
        position_shift = alphabet.index(text) + shift_amount
        position_shift %= len(alphabet)
        cypher_text += alphabet[position_shift]
    print(f"Your encrypted text is: {cypher_text}")

encrypt(text, shift)





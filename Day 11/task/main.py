import random
from art import logo


def calculate_score(cards):
    score = sum(cards)
    # Convert Ace (11) to 1 if needed
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score


def dealer_play(cards, user_score, deck):
    while True:
        score = calculate_score(cards)

        # Dealer stops at >= 17
        if score >= 17:
            break

        cards.append(random.choice(deck))

    return score


def show_state(user_cards, dealer_cards, user_score):
    print(f"\nYour cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's first card: {dealer_cards[1]}\n")


def blackjack_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    print("\n" * 10)
    print(logo)

    user = random.choices(cards, k=2)
    dealer = random.choices(cards, k=2)

    user_score = calculate_score(user)
    dealer_score = calculate_score(dealer)

    # Check for Blackjack
    if user_score == 21:
        dealer_score = dealer_play(dealer, user_score, cards)
        if dealer_score == 21:
            print("Both got Blackjack! It's a draw.")
        else:
            print("Blackjack! You win!")
        return

    # User turn
    show_state(user, dealer, user_score)

    while True:
        choice = input("Type 'Y' to hit or 'N' to stand: ").lower()
        if choice == 'y':
            user.append(random.choice(cards))
            user_score = calculate_score(user)
            show_state(user, dealer, user_score)

            if user_score > 21:
                print("You busted! You lose!")
                return
        else:
            break

    # Dealer turn
    dealer_score = dealer_play(dealer, user_score, cards)

    # Results
    print(f"\nYour final hand: {user}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")

    if dealer_score > 21:
        print("Dealer busted! You win!")
    elif user_score > dealer_score:
        print("You win!")
    elif user_score < dealer_score:
        print("You lose!")
    else:
        print("It's a draw!")


# Game loop
while True:
    play = input("\nDo you want to play Blackjack? (Y/N): ").lower()
    if play == "y":
        blackjack_game()
    else:
        print("Goodbye!")
        break

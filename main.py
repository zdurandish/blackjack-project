import random

def deal_card():
    """Takes a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score (list):
    """Takes a list of cards and returns the score calculated from the cards."""
    score = sum(list)
    if score == 21 and len(list) == 2:
        return 0
    if score > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    return score


def compare(u_score, c_score):
    """Takes both the user and the computer scores and compares them."""
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "The opponent had a blackjack. You lose!"
    elif u_score == 0:
        return "You had a blackjack. You win!"
    elif u_score > 21:
        return "You went over, you lose!"
    elif c_score > 21:
        return "The opponent went over, you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        should_continue = input("Type 'y' to draw another card. Type 'n' to pass: ").lower()
        if should_continue == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
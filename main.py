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


user_cards = []
computer_cards = []
game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, Current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    game_over = True

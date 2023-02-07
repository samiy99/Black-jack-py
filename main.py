# in this program the player refers to both the computer and the human user
import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []
black_jack = 21


# function to deal cards
def deal_cards(card_choices, player):
    """takes the deck of cards and a player either the computer or the human player as inputs and adds a card to their stack"""
    selected_card = random.choice(card_choices)
    player.append(selected_card)


# function to calculate the score of the player
def calculate_score(player_cards):
    player_score = sum(player_cards)
    return player_score


# change ace function
def ace_change(player_cards):
    for i in player_cards:
        if i == 11:
            player_cards[player_cards.index(i)] = 1


# initial card dealing


# # # # game logic # # # #
def game():
    for i in range(0, 2):
        deal_cards(cards, user_cards)
        deal_cards(cards, computer_cards)
    print( f"   your cards:{user_cards}, current score {calculate_score(user_cards)}")
    print(f"   computer's first card: {computer_cards[0]}")
    if calculate_score(user_cards) == 21 and calculate_score(
            computer_cards) == 21:
        print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
        print( f"  computer final hand is: {computer_cards} computer final score is {calculate_score(computer_cards)}")        
        return ("you draw both of you have black jacks")
    elif calculate_score(user_cards) == 21:
        print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
        print( f"  computer final hand is: {computer_cards} computer final score is {calculate_score(computer_cards)}") 
        return ("you win with black jack")
    elif calculate_score(computer_cards) == 21:
        print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
        print( f"  computer final hand is: {computer_cards} computer final score is {calculate_score(computer_cards)}") 
        return ("computer wins with black jack")
    elif calculate_score(user_cards) > 21:
        ace_change(user_cards)
    elif calculate_score(computer_cards) > 21:
        ace_change(computer_cards)
    # # # # player logic mechanism
    option = input("Do you want to hit or stand? type 'y' for hit or 'n' for stand: ")
    while option == "y":
        deal_cards(cards, user_cards)
        if calculate_score(user_cards) > 21:
            
            if 11 in user_cards:
                ace_change(user_cards)
            else:
                print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
                print( f"  computer final hand is: {computer_cards} computer final score is {calculate_score(computer_cards)}") 
                return ("bust you lose")
                option = "n"
        print( f"   your cards:{user_cards}, current score {calculate_score(user_cards)}")        
        option = input("Do you want to hit or stand? type 'y' for hit or 'n' for stand :")
    # # # # computer logic mechanism
    while calculate_score(computer_cards) < 17:
        deal_cards(cards, computer_cards)
        if calculate_score(computer_cards) > 21:
            if 11 in computer_cards:
                ace_change(computer_cards)
            else:
                print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
                print( f"  computer final hand is: {computer_cards} computer final score is {calculate_score(computer_cards)}") 
                return ("computer bust you win  ")
        
    # # # winner evaluation logic
    if calculate_score(user_cards) == calculate_score(computer_cards):
        print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
        print( f"  computer final hand is: {computer_cards} your final score is {calculate_score(computer_cards)}") 
        return ("draw")
    elif calculate_score(user_cards) > calculate_score(computer_cards):
        print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
        print( f"  computer final hand is: {computer_cards} your final score is {calculate_score(computer_cards)}") 
        return ("you win")
    else:
        print( f"  your final hand is: {user_cards} your final score is {calculate_score(user_cards)}")
        print( f"  computer final hand is: {computer_cards} your final score is {calculate_score(computer_cards)}") 
        return ("computer wins")



game_control = input("Do you want to play black jack? type 'y' for yes and 'n' for no: ")

while game_control == "y":
    print(logo)
    print(game())
    computer_cards = []
    user_cards = []
    game_control = input("Do you want to play black jack? type 'y' for yes and 'n' for no: ")
    clear()
    



import random
logo  = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"             
"""
value_and_card_dict = {
    "1" : [11,''' 
 -------
|A      |
|       |
|       |
|       |
|      A|
 ------- '''],
    "2" : [2,'''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- '''],
    "3" : [3,'''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- '''],
    "4" : [4,'''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- '''],
    "5" : [5,'''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- '''],
    "6" : [6,'''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- '''],
    "7" : [7,'''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- '''],
    "8" : [8,'''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- '''],
    "9" : [9,'''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- '''],
    "10" : [10,'''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- '''],
    "J" : [10,''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- '''],
    "Q" : [10,'''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- '''],
    "K" : [10,'''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- ''']
}

BLANKCARD = '''
 -------
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- 
 '''

def calculate_score(cards_hand):
    current_score = 0
    for val in cards_hand:   
        current_score += value_and_card_dict[val][0]
    if '1' in cards_hand and current_score > 21:
        return current_score - 11 + 1
    return current_score


def print_player_cards(players_cards):
    print("Your cards: \t\tYour Current Score: ", calculate_score(players_cards) )
    for single in players_cards:
        print(value_and_card_dict[single][1]) 

def print_computer_cards(computer_cards, player_pass):
    if player_pass:
        print("Computer's cards: \t\tComputer's Current Score: ", calculate_score(computer_cards) )
        for single in computer_cards:
            print(value_and_card_dict[single][1] ) 
    else:
        print("Computer's cards: \tComputer Current Score: ", value_and_card_dict[computer_cards[0]][0])
        print(value_and_card_dict[computer_cards[0]][1] )
        print(BLANKCARD) 

def append_cards(existing_hand):
    new_card_to_add = random.choice(['1','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    existing_hand.append(new_card_to_add)

def restart_game():
    game_over = False
    player_pass = False
    
    print(logo)
    players_cards = [random.choice(['1','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']) for i in range(2)]
    computer_cards = [random.choice(['1','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']) for i in range(2)]
        
    if calculate_score(players_cards) == 21:
            print_player_cards(players_cards)
            print_computer_cards(computer_cards, player_pass = True)
            print("\nYou Won! You hit the blackjack!\n")
            return
    elif calculate_score(computer_cards) == 21:
            print_player_cards(players_cards)
            print_computer_cards(computer_cards, player_pass = True)
            print("\nYou Lose! Oh no! Computer  hit the blackjack!\n")
            return

    while not game_over:
        print_player_cards(players_cards)
        print_computer_cards(computer_cards, player_pass)
        
        direction = input("Type 'y' to get another card, type 'n' to pass: ")
        if direction == 'y':
            append_cards(players_cards)
            if calculate_score(players_cards) > 21:
                print_player_cards(players_cards)
                print("\nYou Lose.\nYou went over 21. It's a BUST! \n")
                return
            
        if direction == 'n':
            while calculate_score(computer_cards) < calculate_score(players_cards) or  calculate_score(computer_cards)<= 16:
                append_cards(computer_cards)
            game_over = True

    print_player_cards(players_cards)
    print_computer_cards(computer_cards, player_pass = True)

    if calculate_score(computer_cards) > 21:
        print("\nYou Win. Wohoooo!Computer went over.\n")
            
    elif calculate_score(players_cards) == calculate_score(computer_cards):
        print("\nIt is a draw. You have equal Score.\n")
            
    else:
        print("\nYou lose. Computer has greater score than you, and has less than equal to 21.\n")


play_again = True if input("Do you want to play the Black Jack game ? Type 'y' for yes, and 'n' for no.") == 'y' else False
while play_again:
    restart_game()
    play_again = True if input("Do you want to play the game again? Type 'y' for yes, and 'n' for no.") == 'y' else False

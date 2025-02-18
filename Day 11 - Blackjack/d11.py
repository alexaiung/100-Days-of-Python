from random import randint

def show_hand(hand):
    return ', '.join([str(i) for i in hand])

def calculate_sum(hand):
    if 1 in hand and sum(hand) > 21:
        return sum(hand)
    else:
        hand = [i if i != 1 else 11 for i in hand]
        return sum(hand)

def replace_court(hand):
    return [i if i <= 10 else 10 for i in hand]

def check_end_game(player_hand, computer_hand, dealing=True):
    end_game = False
    if dealing:
        if calculate_sum(player_hand) > 21:
            print('Bust! Player lost!')
            end_game = True
        if calculate_sum(computer_hand) > 21:
            print('Bust! Computer lost!')
            end_game = True
        if calculate_sum(player_hand) == 21:
            print('You won!')
            end_game = True
    else:
        if calculate_sum(player_hand) > calculate_sum(computer_hand):
            print('Player won!')
            end_game = True
        elif calculate_sum(player_hand) == calculate_sum(computer_hand):
            print('Draw!')
            end_game = True
        else:
            print('Computer won, you lost!')
            end_game = True
    return end_game

print('Welcome to Blackjack!')



play = "y"
while play == 'y':
    play = ''
    while play not in ['y', 'n']:
        print('-' * 50)
        play = input('Do you want to play a game of Blackjack? Type "y" or "n": ')
        if play not in ['y', 'n']:
            print('Invalid answer')
    if play == 'y':
        # Initiate new round
        player_hand = list()
        computer_hand = list()
        keep_dealing = True

        # First card of the player
        player_hand.append(randint(1, 13))
        player_hand = replace_court(player_hand)
        computer_hand.append(randint(1, 13))
        computer_hand = replace_court(computer_hand)

        # Since the game is beginning, we start with the value of 'y' to the variable 'deal_more'
        deal_more = "y"
        end_game = False
        while not end_game:
            # Only deals if the player wanted that, but the computer may still obtain more cards
            if deal_more == 'y':
                player_hand.append(randint(1, 13))
                player_hand = replace_court(player_hand)
            # The rule is that, if the sum is under 17, the dealer must draw more cards
            if calculate_sum(computer_hand) < 17:
                computer_hand.append(randint(1, 13))
                computer_hand = replace_court(computer_hand)
                if deal_more == 'n':
                    while calculate_sum(computer_hand) < 17:
                        computer_hand.append(randint(1, 13))
                        computer_hand = replace_court(computer_hand)

            print(f'Your hand: {show_hand(player_hand)}')
            print(calculate_sum(player_hand))
            print(f'Computer hand: {show_hand(computer_hand)}')
            print(calculate_sum(computer_hand))

            # Check if player busted
            if check_end_game(player_hand, computer_hand) and keep_dealing:
                break

            # If deal_more == y, the game just started or the player wants more cards
            if deal_more == 'y':
                # Resets the variable
                deal_more = ''
                while deal_more not in ['y', 'n']:
                    deal_more = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if deal_more not in ['y', 'n']:
                        print('Invalid answer, try again')
            elif calculate_sum(computer_hand) >= 17:
                print('Your final hand:', player_hand)
                print("Computer's final hand:", computer_hand)
                check_end_game(player_hand, computer_hand, False)
                end_game = True




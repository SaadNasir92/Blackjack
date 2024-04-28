from art import logo
import random

print(logo)
unlimited_deck = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
player_chips = 500


# deal cards
def deal_cards(deck):
    """Deals cards. Returns random list."""
    hand = []
    cards = list(deck)
    for x in range(2):
        hand.append(random.choice(cards))
    return hand


# defining function for hit
def hit(hand, deck):
    """When hit is called, give hand another card. Returns List with new card."""
    cards = list(deck)
    hand.append(random.choice(cards))
    return hand


# Play function
def play(chip_stack):
    """Give play text and see if user wants to play - returns true or false to keep game running"""
    print(
        f"\nWould you like to play a game of blackjack? Current chips: ${chip_stack}"
    )
    play_game = input('\nType "y" to play or "n" to exit.\n').lower()
    if play_game == 'y' or play_game == 'yes':
        # insert game below or initiation of game.
        # clear()
        return True
    else:
        print(f"\nThanks for playing, you ended with ${chip_stack}.")
        return False


# checking hand values
def check_value(hand, deck, user):
    """Check hand value and return value or bust value."""
    value = 0
    alt_value = []
    aces = ace_check(hand)

    for x in hand:
        value += deck[x]
    for x in range(0, aces):
        if value > 21:
            value -= 10
        else:
            alt_value.append(value)
            value -= 10
    alt_value.append(value)

    if len(alt_value) == 2:
        total_value = alt_value[0]
        sub_value = alt_value[1]
        return total_value, sub_value
    else:
        if value > 21:
            print(f"\n{user} hand- {hand} - Value: {value}")
            print("Bust!\n")
            return -1, -1
        else:
            return value, -1


def has_blackjack(dlr_value, dlr_hand, user_value, user_hand):
    """Check to see if anyone has blackjack - Returns True or False"""
    if len(dlr_hand) == 2 and len(user_hand) == 2:
        if dlr_value == 21 and user_value == 21:
            print("\nYou and the Dealer have Blackjack!\nIt's a Draw!")
            return True
        elif dlr_value == 21:
            print("\nDealer has Blackjack!\nYou Lose!")
            return True
        elif user_value == 21:
            print("\nYou have Blackjack!\nYou Win!")
            return True
        else:
            return False
    else:
        return False


def ace_check(hand):
    """Check for # of aces in hand - returns int value of 1 Ace or 2 or more or none. """
    check = 0
    for x in hand:
        if x == 'A':
            check += 1
    return check


# BlackJack
def black_jack():
    """Run a game of blackjack, returns True/False to end or keep going."""
    # deal cards to player and dealer.
    player_hand = deal_cards(unlimited_deck)
    dealer_hand = deal_cards(unlimited_deck)

    # setting dlr hand values
    dlr_values = (check_value(dealer_hand, unlimited_deck, "Dealers"))
    dealer_hand_value = dlr_values[0]

    # capture hidden card and hide 2nd card of dlr, print dealer hand for user to see.
    hidden_card = dealer_hand[1]
    dealer_hand[1] = 'X'
    print(f"    Dealer's hand- {dealer_hand}")

    hitting = True
    while hitting:

        # return a tuple with 0 index as main value and 1 index as an alt value for ace or null to calc player value.
        values = (check_value(player_hand, unlimited_deck, "Your"))
        # setting player hand values
        player_alt_value = values[1]
        player_hand_value = values[0]

        # checking for blackjack (Only works first time since it's based on len of all hands = 2
        if has_blackjack(dlr_value=dealer_hand_value,
                         dlr_hand=dealer_hand,
                         user_value=player_hand_value,
                         user_hand=player_hand):
            dealer_hand[1] = hidden_card
            print(f'    {dealer_hand}')
            return play(player_chips)

        # check for bust
        if player_hand_value == -1:
            print('You lose!')
            return play(player_chips)

        # check for 2 value hands or 1 value hands (based on aces)
        elif player_alt_value == -1:
            print(
                f'\nYour Hand- {player_hand}: Value of hand: {player_hand_value}.'
            )
        else:
            print(
                f'\nYour Hand- {player_hand}: Value of hand: {player_alt_value} or {player_hand_value}.'
            )

        # Checking for hit or stay.
        print("\nWould you like to Hit or Stay?")
        choice = input("Type 'hit' to hit or 'stay' to stay.\n").lower()

        # they hit
        if choice == 'hit':
            player_hand = hit(player_hand, unlimited_deck)

        # they pass
        elif choice == 'stay':
            hitting = False

        # they type incorrectly
        else:
            print("\nInvalid input, please try again.")

    # reveal dealer hand
    dealer_hand[1] = hidden_card
    print(
        f"\n    Dealer's hand- {dealer_hand}: Value of hand: {dealer_hand_value}."
    )

    # check dlr hand being under 17
    while dealer_hand_value < 17:

        # while dlr hand is less than 17 including A @ 11, dlr has to hit.
        dealer_hand = hit(dealer_hand, unlimited_deck)

        # checking new dlr value & see if he busts or hits 17 first, otherwise prints dlr hand.
        dlr_val_check = check_value(dealer_hand, unlimited_deck, "Dealer's")
        dealer_hand_value = dlr_val_check[0]
        if dealer_hand_value == -1:
            print('You Win!')
            return play(player_chips)
        else:
            print(
                f"\n    Dealer's hand- {dealer_hand}: Value of hand: {dealer_hand_value}."
            )

    # value now 17 and didn't bust for dealer, time to check for winner.
    if dealer_hand_value == player_hand_value:
        print('\nPush!\n')
        return play(player_chips)
    elif dealer_hand_value > player_hand_value:
        print('\nDealer wins!\n')
        return play(player_chips)
    else:
        print('\nYou win!\n')
        return play(player_chips)


running = play(player_chips)
while running:
    running = black_jack()

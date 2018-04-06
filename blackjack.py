import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4


def get_hand(deck):

    hand = (random.sample(deck, 2))
    return hand


def total(hand):
    total = 0
    for card in hand:
        if card <= 10:
            total += card
        elif card == 11:
            if total >= 11:
                total += 1
            else:
                total += 11
    return total


def hit(hand, deck):
    hand.append(random.choice(deck))
    # print("You now have: " + str(hand) + "for a total of " + str(total(hand)))
    return hand


def get_instructions():
    command = input("Would you like to stay or hit? ")
    return command


def check_status(hand):
    if total(hand) > 21:
        print("You went bust!")
        keep_playing = input("Would you like to play again? ")
        return reset(keep_playing, hand)
    else:
        get_instructions()


def reset(keep_playing, hand):
    if keep_playing == "y":
        hand = []
        print(hand)
        hand = get_hand(deck)
        return hand
    if keep_playing == "n":
        exit()


def play_round(deck):
    # Setup player and dealer hand
    player_hand = get_hand(deck)
    dealer_hand = get_hand(deck)

    # Print hands
    print("You have " + str(player_hand))
    print("The dealer is showing " + str(dealer_hand))

    # user input to resolve the hand
    while True:
        # Check for blackjack
        player_blackjack = total(player_hand) == 21
        if player_blackjack:
            print("You have a blackjack\n")
            return False
        chosen_action = input("Would you like to hit or stay? \n")
        if chosen_action == "hit":
            hit(player_hand, deck)
            print("Your hand is now " + str(player_hand), str(total(player_hand)))
            if total(player_hand) > 21:
                print("You've busted")
                return False
            else:
                continue
        # Resolve dealers hand
        if total(dealer_hand) == 21:
            print("The dealer has blackjack")
            if player_blackjack:
                print("This is a push\n")
                return True
            else:
                print("The dealer won")
                exit()
        while total(dealer_hand) < 17:
            hit(dealer_hand, deck)
            print(total(dealer_hand))
        if total(dealer_hand) > 21:
            print("The dealer has " + str(total(dealer_hand)))
            print("The dealer busted, you won\n")
            return True
        else:
            if total(player_hand) > total(dealer_hand):
                print("You won this round\n")
                return True
            else:
                print("The dealer has " + str(total(dealer_hand)))
                print("The dealer won\n")
                return False


def run_game():

    while True:
        play_round(deck)
        play_again = input("Would you like to play again? ")
        if play_again == "no":
            return False
        else:
            continue


run_game()

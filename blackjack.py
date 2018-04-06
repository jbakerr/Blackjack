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
    print("You now have: " + str(hand) + "for a total of "+ str(total(hand)))
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


def run_game():

    command = ""
    player_hand = get_hand(deck)
    dealer_hand = get_hand(deck)
    while True:

        print(
            "You have " + str(player_hand) + "for a total of " +
            str(total(player_hand)))
        # print("The dealer is showing " + str(dealer_hand[0]))

        command = get_instructions()
        if command == "hit":
            while total(dealer_hand) < 17:
                hit(dealer_hand, deck)
            hit(player_hand, deck)
            print(player_hand)
            print(total(player_hand))
            # while total(dealer_hand) < 17:
            #     hit(dealer_hand, deck)
        elif command == "q":
            break

        # if command == "hit":
        #     hit(player_hand, deck)
        #     check_status(player_hand)
        # elif command == "stay":
        #     break

run_game()

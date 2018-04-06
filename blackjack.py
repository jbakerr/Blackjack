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
    return hand


def play_round(deck):
    # Setup player and dealer hand
    player_hand = get_hand(deck)
    dealer_hand = get_hand(deck)

    # Print hands
    print("You have " + str(player_hand), str(total(player_hand)))
    print("The dealer is showing " + str(dealer_hand[0]))

    # user input to resolve the hand
    while True:
        # Check for blackjack
        player_blackjack = total(player_hand) == 21
        if player_blackjack:
            print("You have a blackjack\n")
        elif not player_blackjack:
            chosen_action = input("Would you like to hit or stay? \n")
            if chosen_action == "hit":
                hit(player_hand, deck)
                print("Your hand is now " + str(player_hand), str(total(player_hand)))
                if total(player_hand) > 21:
                    print("You've busted")
                    return False, -1
                else:
                    continue
            elif chosen_action == "stay":
                print("Let's see what the dealer has.\n")
        # Resolve dealers hand
        if total(dealer_hand) == 21:
            print("The dealer has blackjack")
            if total(player_hand) == 21:
                print("This is a push\n")
                return False, 1
            else:
                print("The dealer won")
                return False, -1
        while total(dealer_hand) < 17:
            hit(dealer_hand, deck)
        if total(dealer_hand) > 21:
            print("The dealer has " + str(total(dealer_hand)))
            print("The dealer busted, you won\n")
            return True, 2
        else:
            if total(player_hand) > total(dealer_hand):
                print("The dealer has " + str(total(dealer_hand)) + ", you won this round\n")
                return True, 2
            else:
                print("The dealer has " + str(total(dealer_hand)))
                print("The dealer won\n")
                return False, -1


def get_bet(money):
    while True:
        bet = input("What would you like to bet? ")
        bet = int(bet)
        if bet > money:
            print("Please don't bet more than you have.")
            continue
        else:
            return bet


def run_game():
    money = 100

    while money > 0:
        bet = get_bet(money)
        win, payout = play_round(deck)
        if win:
            money += (payout * bet)
        else:
            money += bet * payout
        print("You have " + str(money))
        if money > 0:
            play_again = input("Would you like to play again? ")
            if play_again == "no":
                print("You've left the table with $" + str(money))
                return
            else:
                continue
    print("You've lost the game")


run_game()

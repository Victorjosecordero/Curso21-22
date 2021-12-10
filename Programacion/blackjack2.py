# BlackJack or 21 game

import random
# THE PLANNING PHASE
 # Dealer cards
dealer_cards = []
 # Player cards
player_cards = []

# Deal the cards
# Display the cards
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)
 
 # Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# Sum of the Player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?  "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You Win!! 21")

 # Compare the sums of the cards between D v P  
 # If P card sum is greater than 21 = BUST
 # If P card sum is less than 21 = Option Hit or Stay
 # If P option Stay compare sum of D v P 
 # If P sum < 21 && > D sum then P wins!
 # If P sum < D sum then P loses
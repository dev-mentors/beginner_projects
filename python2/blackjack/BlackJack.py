from Deck import Deck
from Hand import Hand

new_deck = Deck()

print(new_deck.cards)

print "Welcome to the game Black Jack!"

my_hand = Hand()
dealer_hand = Hand()

# need to subtract cards from deck
drawn_card = new_deck.draw_card()
drawn_card_2 = new_deck.draw_card()

dealer_card = new_deck.draw_card()
dealer_card_2 = new_deck.draw_card()

my_hand.add_card(drawn_card)
my_hand.add_card(drawn_card_2)
# need way to add cards to hand

my_hand.print_hand()

dealer_hand.add_card(dealer_card)
dealer_hand.add_card(dealer_card_2)

dealer_hand.print_hand()

print "My Hand: " + str(my_hand.get_score())
print "Dealer: " + str(dealer_hand.get_score())

hit = raw_input("Would you like to hit?")
if hit == "yes" or "Yes":
    my_hand.add_card(new_deck.draw_card())
elif hit == "No" or "no":
    print "This is your hand: " + str(my_hand.get_score())

if my_hand.is_busted():
    print "You lose "+ str(my_hand.get_score())




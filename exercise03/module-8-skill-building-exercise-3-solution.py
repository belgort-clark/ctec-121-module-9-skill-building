# Module 8 - Skill Building Exercise No. 3 Solution
# Author: Bruce Elgort
# Date: July 22, 2017
# Revised: February, 25, 2019

class PlayingCard:

    def __init__(self,rank,suit):
        self.__rank = rank
        self.__suit = suit
        self.__flipped = False

    def flip(self):
        flipped = self.__flipped
        if not flipped:
            self.__flipped = True
        else:
            self.__flipped = False

    def getRank(self):
        return self.__rank

    def getSuit(self):
        return self.__suit

    def getFlipped(self):
        return self.__flipped

def main():
    # build list of suits
    suits = ['Clubs','Hearts','Diamonds','Spades']

    # build list of card ranks
    ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    # create a list for the deck
    deck = []

    print("Building the deck of cards...")

    # using nested loops, create the deck of cards
    for suit in suits:
        for rank in ranks:
            deck.append(PlayingCard(rank,suit))

    print("Deck of cards built!")

    # flip all of the cards over to show their faces
    for i in range(len(deck)):
         deck[i].flip()

    # now show each card
    print("\n\nDisplaying each card...\n\n")
    for i in range(len(deck)):
        print("Rank: {0:>8}".format(deck[i].getRank()),"Suit:{0:>11}".format(deck[i].getSuit()),"Flipped:{0:>5}".format(deck[i].getFlipped()))

    # now flip them back
    for i in range(len(deck)):
         deck[i].flip()

    # now show each card
    print("\n\nShowing the flipped deck of cards...\n\n")
    for i in range(len(deck)):
        print("Rank: {0:>8}".format(deck[i].getRank()),"Suit:{0:>11}".format(deck[i].getSuit()),"Flipped:{0:>5}".format(deck[i].getFlipped()))


main()
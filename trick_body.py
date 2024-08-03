# Packages
import random
import ternarios as ter
#=========================
# Functions

# Function to create a deck of cards
def create_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    image_paths = [(f'{rank}_of_{suit}.png') for suit in suits for rank in ranks]
    return image_paths

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck
    
# Function to select 27 random cards
def select_random_cards(deck, num_cards=27):
    return random.sample(deck, num_cards)    

# Function to distribute cards into 3 piles
def distribute_into_3piles(cards):
    pile1 = [cards[(3*i)+0] for i in range(9)]
    pile2 = [cards[(3*i)+1] for i in range(9)]
    pile3 = [cards[(3*i)+2] for i in range(9)]    
    return pile1, pile2, pile3 

# Function to put 3 pilas in on deck
def piles_into_1deck(pile1, pile2, pile3, num_pile, ternario):
    if ternario == 0:
        if num_pile == 1:
            deck = pile1 + pile2 + pile3
        elif num_pile == 2:
            deck = pile2 + pile1 + pile3
        else:
            deck = pile3 + pile1 + pile2
    elif ternario == 1:
        if num_pile == 1:
            deck = pile2 + pile1 + pile3
        elif num_pile == 2:
            deck = pile1 + pile2 + pile3
        else:
            deck = pile1 + pile3 + pile2
    elif ternario == 2:
        if num_pile == 1:
            deck = pile2 + pile3 + pile1
        elif num_pile == 2:
            deck = pile3 + pile1 + pile2
        else:
            deck = pile2 + pile1 + pile3
    else:
        return 'Error'
    
    return deck

   
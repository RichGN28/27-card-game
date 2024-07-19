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

def display_one_column(cards):
    N = len(cards)
    
    print('')
    print('')        
    print('Selecciona una carta, toma nota.')
    print('')    
    print(' Col 1 ')
    for l in range(N):
        print(cards[l])
    print('')
    
def display_three_columns(pile1,pile2,pile3):
    N = len(pile1)
    print(' Col 1        Col 2        Col 3')
    for l in range(N):
        print(pile1[l],'',pile2[l],'',pile3[l])


def call_the_winer(selected_cards, num):
    print(f"Tu carta es {selected_cards[num]} y esta en la posicion numero: {num}")
            
# Main function
def main():
    deck = create_deck()
    shuffle_deck(deck)
    selected_cards = select_random_cards(deck)
    display_one_column(selected_cards)

    
    entrada = int(input("Cual es tu numero favorito? "))
    ternario = ter.traductor_ternario(entrada)
    ternario.reverse()
    
    print('========================================')
    print('INICIA EL JUEGO: 21 trick card')
    print('========================================')
    print('')
    
    for k in range(3):
        pile1, pile2, pile3 = distribute_into_3piles(selected_cards)
        display_three_columns(pile1,pile2,pile3)
        print('')
        num_pile = int(input(f"Tu carta está en la columna número: ")) 
        selected_cards = piles_into_1deck(pile1,pile2,pile3,num_pile, ternario[k]) 

    print('')
    print('')
    call_the_winer(selected_cards, entrada)
    print('========================================')
    print('FIN DEL JUEGO')    
    print('========================================')   
    print(selected_cards) 
if __name__ == "__main__":
    main()    
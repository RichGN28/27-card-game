import trick_body as trick
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def create_27_cards_deck():
    deck = trick.create_deck()
    deck = trick.shuffle_deck(deck)
    deck = trick.select_random_cards(deck)
    return deck

def distribute(deck):
    pile1, pile2, pile3 = trick.distribute_into_3piles(deck)
    return pile1, pile2, pile3

def group_piles(pile1, pile2, pile3, num_pile, num):
    deck = trick.piles_into_1deck(pile1, pile2, pile3, num_pile, num)
    return deck 



import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import button_functions as bf
import os
from ternarios import traductor_ternario


def get_number():
    global my_number, ternario
    my_number = fav_number.get()
    fav_number.set('') # Clear the entry
    ternario = traductor_ternario(my_number-1)
    ternario.reverse()

def start_app():
    # Hide the main window
    window.withdraw()

    # Create the start menu window
    global start_menu
    start_menu = tk.Toplevel(window)
    start_menu.title('Welcome to the 27 Trick Game')
    start_menu.geometry('1500x1000')
    start_menu.config(background='green')

    # Add a welcome message
    welcome_label = ttk.Label(start_menu, text='Welcome to the 27 Trick Game!')
    welcome_label.pack(pady=10)

    # portada
    portada = Image.open('portadaok.png')
    ref_image = ImageTk.PhotoImage(portada)
    image_refs.append(ref_image)
    card = ttk.Label(start_menu, image=ref_image)
    card.pack()


    # button
    start_button = ttk.Button(start_menu, text='Start Game', command=initiate_game)
    start_button.pack(pady=10)


def initiate_game():
    start_game()
    start_menu.destroy()
    window.deiconify()


def display_images(pile, frame):
    # Destroy existing widgets in the frame
    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Label):
            widget.destroy()

    # Load and display new images
    for card_image in pile:
        file_path = f'card_images/{card_image}'
        
        if os.path.exists(file_path):
            # Import an image
            current_image = Image.open(file_path).resize((50, 100))
            image_tk = ImageTk.PhotoImage(current_image)

            # Store the reference to the PhotoImage object
            image_refs.append(image_tk)  # Keep a reference to avoid garbage collection
    
            # Create a label with the image and pack it into the frame
            label = ttk.Label(frame, image=image_tk)
            label.pack()
        else:
            print(f'File {file_path} not found')


def display_winner_images(pile, frame):
    # Destroy existing widgets in the frame
    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Label):
            widget.destroy()
    
    counter = 1
    # Load and display new images
    for card_image in pile:
        file_path = f'card_images/{card_image}'
        
        if os.path.exists(file_path):
            if counter == my_number:
                current_image = Image.open(file_path).resize((75, 125))
                image_tk = ImageTk.PhotoImage(current_image)
                image_refs.append(image_tk)
                label = ttk.Label(frame, image=image_tk)
                label.pack(side='left')
            else:
                # Import an image
                current_image = Image.open(file_path).resize((50, 100))
                image_tk = ImageTk.PhotoImage(current_image)

                # Store the reference to the PhotoImage object
                image_refs.append(image_tk)  # Keep a reference to avoid garbage collection
        
                # Create a label with the image and pack it into the frame
                label = ttk.Label(frame, image=image_tk)
                label.pack(side='left')
        else:
            print(f'File {file_path} not found')
    
        counter += 1



def start_game():
    if 'winner_window' in globals() and winner_window.winfo_exists():
        close_window()
    else:
        global deck, pile1, pile2, pile3, rounds
        rounds = 0
        deck = bf.create_27_cards_deck()
        pile1, pile2, pile3 = bf.distribute(deck)

        display_images(pile1, frame1)
        display_images(pile2, frame2)
        display_images(pile3, frame3)


def increment_round():
    global rounds
    rounds += 1

def button_1():
    iterate(1)
    

def button_2():
    iterate(2)

def button_3():
    iterate(3)

def iterate(pile_number):
    global deck, pile1, pile2, pile3, rounds, ternario
    increment_round()


    if rounds < 3:

        
        deck = bf.group_piles(pile1, pile2, pile3, pile_number, ternario.pop(0))

        pile1, pile2, pile3 = bf.distribute(deck)

        display_images(pile1, frame1)
        display_images(pile2, frame2)
        display_images(pile3, frame3)

    else:
        deck = bf.group_piles(pile1, pile2, pile3, pile_number, ternario.pop(0))
        show_winner()



def show_winner():
    global winner_window
    winner_window = tk.Toplevel()
    winner_window.title('Is this your card?')

    frame_winner = ttk.Frame(winner_window, width=1800, height=300, borderwidth=10, relief=tk.RIDGE)
    frame_winner.pack(padx=100)

    label = ttk.Label(winner_window, text=f'Is your card in the position {my_number}?')
    label.pack()
    display_winner_images(deck, frame_winner)

def close_window():
    winner_window.destroy()

# Global variable to store references to the PhotoImage objects
image_refs = []

# Create the main window
window = tk.Tk()
window.geometry('1500x1000')
window.title('21 Trick')
window.config(background='green')

# Create the start menu
window.after(0, start_app)


# Create frames for card display and buttons
frame1 = ttk.Frame(window, width=700, height=300, borderwidth=10, relief=tk.RIDGE)
frame1.pack(side=tk.LEFT, padx=100)

frame2 = ttk.Frame(window, width=700, height=300, borderwidth=10, relief=tk.RIDGE)
frame2.pack(side=tk.LEFT, padx=100)

frame3 = ttk.Frame(window, width=700, height=300, borderwidth=10, relief=tk.RIDGE)
frame3.pack(side=tk.LEFT, padx=100)

frame_buttons = ttk.Frame(window, width=700, height=300, borderwidth=10, relief=tk.RIDGE)
frame_buttons.pack(side=tk.LEFT, padx=100, pady=100)

# Create entry
fav_number = tk.IntVar()
# my_number = get_number()


entry_num = ttk.Entry(frame_buttons, textvariable=fav_number)
entry_num.pack()



# Create buttons for piles
button1 = ttk.Button(frame1, text='Pile 1', command=button_1)
button2 = ttk.Button(frame2, text='Pile 2', command=button_2)
button3 = ttk.Button(frame3, text='Pile 3', command=button_3)
button1.pack()
button2.pack()
button3.pack()  

# Button to start the game
button_start = ttk.Button(frame_buttons, text='Restart Game!', command=start_game)
button_start.pack(side='right')
button_number = ttk.Button(frame_buttons, text='Enter number', command=get_number)
button_number.pack(side='left')


# Run the application
window.mainloop()

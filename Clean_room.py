# This is a Clean the Room game where the player cleans up messes
import random
messes = ["dirty socks", "old books", "trash", "dirty dishes"]

def show_intro():
    print("Welcome to Clean the Room!")
    print("First, try cleaning the " + random.choice(messes))

def show_room():
    print("Messes still in the room: ", messes)

def clean_item(choice):
    if choice in messes:
        messes.remove(choice)
        print("You cleaned the " + choice)
    else:
        print("That isn't in the room. Try something else.")

def play_game():
    show_intro()
    while len(messes) > 0:
        show_room()
        answer = input("What do you want to clean? ")
        clean_item(answer)
    print("The room is clean! Great job!")

play_game()
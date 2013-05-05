#Mini-project 2: A simple game of "Guess the Number!"
#to be run on www.codeskulptor.org

import random
import simplegui

comp_guess = -1
guesses_left = 0
guessrange = ""

#changes range to range [0,100) and restarts game
def range100():
    print "Let's start a new game... The range is 0 - 100."
    
    global comp_guess, guesses_left, guessrange
    comp_guess = random.randrange(0,100)
    guesses_left = 7
    guessrange = "r100"
    
    print "You have " + str(guesses_left) + " guesses left.\n"


#changes range to range [0,1000) and restarts game
def range1000():
    print "Let's start a new game... The range is 0 - 1000."
    
    global comp_guess, guesses_left, guessrange
    comp_guess = random.randrange(0,1000)
    guesses_left = 10
    guessrange = "r1000"
    
    print "You have " + str(guesses_left) + " guesses left.\n"


def restart():
    global guessrange
    if(guessrange == "r100"):
        range100()
    else:
        range1000()
    
#game logic: validates input guess against computer's guess
def get_input(guess):
    print "Your Guess is " + guess
    guess = int(guess)

    global guesses_left
    guesses_left -= 1
    
    if(comp_guess > guess):
        print "Higher!\n"
    elif(comp_guess < guess):
        print "Lower!\n"
    else:
        print "Absolutely Correct!\n"
        restart()

    if(guesses_left == 0):
        print "Game Over! Try again!\n"
        restart()

#initialize gui
def setup():
    #frame
    global frame
    frame = simplegui.create_frame("Guess the Number", 200, 200)
    
    #buttons
    range100_button = frame.add_button("Range 0-100", range100, 100)
    range1000_button = frame.add_button("Range 0-1000", range1000, 100)

    #input field
    inp = frame.add_input("Enter your guess: ", get_input, 100)

setup()
frame.start()

#start the game
range100()
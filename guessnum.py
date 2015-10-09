# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui

secret_number = 0
high_end = 101
n = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, n
    secret_number = random.randrange(0, high_end)
    n = math.ceil( math.log(high_end + 1, 2) )
    
    print ("")
    print ("New game. Range is from 0 to", high_end - 1)
    print ("Number of remaining guess is", int(n))

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high_end
    high_end = 101
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global high_end
    high_end = 1001
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global n
    n = n - 1
    
    print ("")
    print ("Guess was " + guess)
    print ("Number of remaining guess is", int(n))
    
    guess_number = int(guess)
    if guess_number == secret_number:
        print ("Correct!")
        new_game()
    elif n == 0:
        print ("You ran out of guesses. The number was", secret_number)
        new_game()
    elif guess_number < secret_number:
        print ("Higher!")
    elif guess_number > secret_number:
        print ("Lower!")
   
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
button_100 = frame.add_button("Range: 0 - 100", range100)
button_1000 = frame.add_button("Range: 0 - 1000", range1000)
inp = frame.add_input("Enter a guess", input_guess, 50)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

""" Top down development of Hangman game.

Try to 'fill in the blanks' and perhaps write any helper functions
you need (I didn't use any that aren't listed here, but it is ok if you
want to.  I haven't structured this to be done as a Class, but you can
try to do that for extra credit (see Canvas for description of what
you'd need to do).

"""
import string
import random


# construct main game loop
def main():
    """ Make a loop that repeatedly asks the user if they want to play
    Hangman.  If they do, then call the single function "playGame()", if
    they don't then exit.  Make it so the user enters upper or lower case
    it works.  Also, ignore white space."""
    choose = str(input("Do you want to play Hangman (Y or N)? "))
    while choose == 'y' or choose == 'Y':
        playGame()
        choose = str(input("\nDo you want to play Hangman (Y or N)? "))


def playGame():
    """The is function actually implements the game.  It should work as
    follows:
        guesses is a sring variable that holds all the characters guessed
        (initially set to "")
        numberWrong is the count of the number of wrong guesses (initially set
        to 0)
        MAX_WRONG is a constant = 9
        word is a randomly chosen word the human player must guess.  It should
        be initialized by a function called "chooseWord"
        displayWord is a string that holds the chosen word with dashes '-' in
        place of each letter that hasn't been guessed yet.  Its value gets
        set by the "makeDisplay" function.

        After the above initilization, then construct the loops that will
        repeatedly draw the gallows, print the displayWord, print a table of
        the letters used, and ask the user for a guess.
    """
    guesses = ""
    numberWrong = 0
    MAX_WRONG = 9
    word = chooseWord()
    displayWord = makeDisplay(word, guesses)
    # Outer loop, keeps going if game not over
    while numberWrong < MAX_WRONG and displayWord != word:
        # Inner loop, repeats until valid guess is made
        while True:
            pass
            # call the drawGallows function
            drawGallows(numberWrong)
            # update the variable displayWord
            displayWord = makeDisplay(word, guesses)
            # print "Word so far:" followed by the displayWord
            print("Word so far:", displayWord)
            # print "Letters Used:" followed by a table of the guesses.
            print("Letters Used:")
            printGuesses(guesses)
            # This table of guesses will be printed by calling the
            # "printGuesses" function

            # get the guess from user input.  Force it to be lower case
            # check if guess is valid by calling isValid(guess, guesses)
            # if it is valid then check if guess is not in word.  If it isn't
            # then increase numberWrong by one.
            # Whether or not the guess is in word, update the guesses string
            # with the guess and then break (we can break out of the inner
            # loop because we've established the guess is valid).
            guess = str(input("Enter your guess: ")).lower()
            if isValid(guess, guesses):
                guesses += guess
                if not (guess in word):
                    numberWrong += 1
            else:
                print("Invalid guess.")

            # if the guess is not valid then print "Invalid guess."  This ends
            # the body of the inner loop
            # The last thing to do in the body of the outer loop is to update
            # the displayWord by calling makeDisplay
            # Now outside of the outer loop the game is over and we need to respond
            # appropriately.  If displayWord==word then the user won.  Otherwise
            # we want to display the gallows one last time and say they lost
            # the last thing to do is print what the word was

            displayWord = makeDisplay(word, guesses)
            if displayWord == word:
                print("Congratulations! You won!")
                print("The word was", word)
                break
            elif numberWrong == MAX_WRONG:
                print("Too bad. You lost :(")
                print("The word was", word)
                break


def chooseWord():
    """This function randomly chooses a word and returns it.  You can have a
    short list and choose with if-elif-else
    """
    list = ["pizza", "letter"]
    i = random.randint(0, 1)
    return list[i]


def drawGallows(n):
    """ Draws an character art representation of the gallows.  The number n is
    how many pieces of the drawing to include.  Insert the appropriate if-elif
    statements between the print statements below.   You shouldn't have to edit
    the the actual print('''    ''') statements below, but you may need to
    adjust the indent level of the lines with "print('''".
    """
    if n == 0:
        print('''
    
    
    
    
    
    
     =========''')
    elif n == 1:
        print('''
    
           |
           |
           |
           |
           |
     =========''')
    elif n == 2:
        print('''
       +---+
       |   |
           |
           |
           |
           |
     =========''')
    elif n == 3:
        print('''
       +---+
       |   |
           |
           |
           |
           |
     =========''')
    elif n == 4:
        print('''
       +---+
       |   |
       O   |
           |
           |
           |
     =========''')
    elif n == 5:
        print('''
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========''')
    elif n == 6:
        print('''
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========''')
    elif n == 7:
        print('''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========''')
    elif n == 8:
        print('''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========''')
    elif n == 9:
        print('''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     =========''')


def makeDisplay(word, guesses):
    """This function takes a word (which could be the word chosen by the
    computer, or it could be the list of the alphabet) and returns a string
    where only characters in the guesses string are shown, with all other
    characters replaced by "-".
    I suggest a for loop over each character  in word along with an if-else
    statement to either append the character or the dash "-".
    """
    display = ""
    for i in word:
        if i in guesses:
            display += i
        else:
            display += "-"
    return display

def printGuesses(guesses):
    """This function will print out a table of guesses with 5 characters in
    row.  You can get the whole alphabet from string.ascii_lowercase
    assign the variable toPrint to the value returned by makeDisplay(alphabet,guesses)
    Then print slices of toPrint on separate lines.  You can do this in a for
    loop or by 6 print statments with the appropriate slices hard coded.
    """
    # just print the guesses, you don't need to return anything
    toString = makeDisplay(string.ascii_lowercase, guesses)
    count = 0
    for i in toString:
        count += 1
        if count % 5 == 0:
            print(i, end="\n")
        else:
            print(i, end="")
    print()


def isValid(guess, guesses):
    """This returns a Boolean value if the guess is valid.  The guess
    (contained in the variable "guess") is valid if it hasn't been guessed
    before (that is, it is not in guesses), and it is a letter, and it is a
    single character.
    """
    if len(guess) == 1 and not(guess in guesses):
        return True
    else:
        return False


# call the main function
main()

"""
This template will guide you through the process of writing a text-based
concentration game.  This is a game frequently played with a set of cards
where you have two of each one.  They are laid face down in a grid and
on each turn you select (one at a time) two cards to turn over.  If they
match they are removed.  If they don't match you they are turned over
again.  The goal is to find all the matches in as few tries as you can.

Write this program from the one function/class at a time.  The comments
will tell you what to do and there may be some test code below to verify
that it is working.  Uncomment that code to run the test, and then comment
it out again when you have it working.

"""
import random
import string

N=4  # The number of rows and columns in the grid of cards.
"""
Here is the UML for the ConcentrationCard class.  It is meant to
make it a bit easier to write the rest of the program.

          ConcentrationCard
------------------------------------------
face: str
show: bool
------------------------------------------
ConcentrationCard(face=" ", show=False)

__str__(): str
__eq__(card:ConcentrationCard): bool
__repr__(): str
------------------------------------------

The __str__ method should return different
things depending on the what face and show are.
Note: everything returned will always be 5 characters long.

if face is the empty string then it should always return 5 spaces.

if show is False then it should return "[[*]]"

if show is True then it should return "[face]" (where face
will contain a single character)

The __repr__ method can just return self.__str__()
"""


class ConcentrationCard:
    def __init__(self, face = " ", show = False):
        self.face = face
        self.show = show

    def __str__(self):
        if not self.face:
            return "     "
        else:
            if self.show:
                return "[ " + self.face + " ]"
            else:
                return "[[*]]"

    def __eq__(self, card):
        return self.face == card.face

    def __repr__(self):
        return self.__str__()

# c1=ConcentrationCard()
# c2=ConcentrationCard("",True)
# c3=ConcentrationCard("B",True)
# c4=ConcentrationCard("",False)
# print(c1,c2,c3,c4,c1)
"""Should give this:
[[*]]       [ B ]       [[*]]
"""

""" aRow(n) will create a list of n ConcentrationCard objects
and return it.  Use the default object (call ConcentrationCard() with
no arguments).  I suggest using a list comprehension for this.
"""
def aRow(n):
    return n * [ConcentrationCard()]

# print(aRow(4))
# print(aRow(6))
"""The above test lines should output:
[[[*]], [[*]], [[*]], [[*]]]
[[[*]], [[*]], [[*]], [[*]], [[*]], [[*]]]
"""

""" initializeGrid will take a grid (which is a list of lists of
ConcentrationCard objects) and initialize the faces to random
characters.  You need to have two and only two of each character.
Set n=len(grid) to get the size of the grid.  The total number of
letters you need will then be (n**2)//2 + 1.  Make a list with that
number of letters, double it so you have two of each one, and the
randomize it using random.shuffle.  Then use a nested for loop like
this to put the letters in the cards:

    for row in grid:
        for card in row:
            <<get a letter by using .pop(0) applied to your list of randomized letters>>
            <<set the face of the card (which is a ConcentrationCard object) equal to the letter>>
            <<set the card.show equal to the show parameter>>>
"""
    
def initializeGrid(grid, show=False):
    n = len(grid)
    num_of_letter = (n**2)//2 + 1
    l = list(string.ascii_uppercase)
    letters = l[0:num_of_letter] * 2
    random.shuffle(letters)
    for row in grid:
        for card in row:
            face = letters.pop(0)
            card.face = face
            card.show = show


""" printGrid will take a grid (which is a list of lists of
ConcentrationCard objects) and print it out in a nice way.
I recommend labeling the row and column numbers.  You can find
the size of the grid from len(grid)
"""
def printGrid(grid):
    n=len(grid)
    #print("\n"*100)
    print("      ", end="")
    for c in range(1,n+1):
        print("{:^6}".format(c),end="")
    print("  <<--- column")
    r=1
    for row in grid:
        print("{:^6}".format(r), end="")
        for card in row:
            print(card,end=" ")
        print("\n")
        r += 1
    print("^^^\nrow\n")

"""These lines will test printGrid and initialize grid.
Since the letters are randomized your letters will be
in a different order
"""
grid=[aRow(3) for i in range(3)]
printGrid(grid)
initializeGrid(grid,True)
printGrid(grid)
""" The lines above should give something like this:
        1     2     3     <<--- column
  1   [[*]] [[*]] [[*]] 

  2   [[*]] [[*]] [[*]] 

  3   [[*]] [[*]] [[*]] 

^^^
row

        1     2     3     <<--- column
  1   [ E ] [ G ] [ I ] 

  2   [ F ] [ D ] [ B ] 

  3   [ I ] [ F ] [ C ] 

^^^
row
"""
"""printStats should be a one line function that prints out
the number of tries and the number of matches"""
def printStats(tries, matches):
    print("Tries: ", tries, "          Matches: ", matches)

#printStats(1,3)
""" Should output:
Tries:  1           Matches:  3
"""

""" getCard will take a grid, row number, and column number, and return
the card object corresponding to that position.  The grid object is a list
each element is a row.  So grid[0] gives the row 1 (which is a list of
ConcentrationCard objects).  grid[1] gives row 2, etc.  To get a particular
column you can use the index operator on the list that you get by indexing the
grid.  So, to get the first column of the first row you can do grid[0][0].
To get the second column of the first row you do grid[0][1].  To get the first
column of the second row you'd do grid[1][0].  In general, to the rth row and cth
column, you would return grid[r-1][column-1]
"""
def getCard(grid, r, c):
    return grid[r - 1][c - 1]



#grid=[aRow(2) for i in range(2)]
#grid[0][0].face="A"
#grid[0][1].face="B"
#grid[1][0].face="C"
#grid[1][1].face="D"
#print(getCard(grid,1,1).face,getCard(grid,1,2).face,getCard(grid,2,2).face)
"""The above lines should output:
A B D
"""

""" getGuess will take a grid and a prompt string, and ask for the user
to enter a row and column (separated by commas), and return the card object
that corresponds to that location in the grid.  Ideally, the code will
check to make sure it is a valid guess.  To be valid the following must be True:
0<row<=n
0<column<=n

if the row or column are not in the right range, you should ask again.
If they are in range then you should get the corresponding card (using the
getCard function) and make sure that card.face is not the empty string, and
the card.show is False (meaning it is "face down").  If these things are not
True then you should ask again.

Once a valid card has been chosen, then card.show should be set to True
and the card returned to the caller.

I suggest the following structure:

<<get n from the size of grid>>

    while True:
        <<get the number of rows,columns from user input>>
        if <<they are in range then>>
            <<use getCard to get the card at the chosen row and column>>
            if <<the card isn't the empty string and is not being shown then>>:
                <<break out of loop>>
            else:
                print("You must pick a face down card.  Please try again")
        else:
            print("r and c must be between 1 and", n,"Please try again")
    card.show=True
    return card


"""
def getGuess(grid,prompt):
    def getGuess(grid, prompt):
        n = len(grid)
        while True:
            r, c = eval(input(prompt))
            if 0 < r <= n and 0 < c <= n:
                card = getCard(grid, r, c)
                if card.face != "" and card.show == False:
                    break
                else:
                    print("You must pick a face down card.  Please try again")
            else:
                print("r and c must be between 1 and", n, "Please try again")
        card.show = True
        return card


""" This function is the main routine for playing the game.
You can use it as is.
"""

def playGame():
    matches = 0
    tries = 0
    grid = [ aRow(N) for i in range(N)]
    initializeGrid(grid)
    while matches < N**2//2:

        printGrid(grid)
        printStats(tries, matches)
        card1=getGuess(grid, "Enter row, column for position 1: ")
        printGrid(grid)
        printStats(tries, matches)
        card2=getGuess(grid, "Enter row, column for position 2: ")
        tries += 1
        printGrid(grid)
        printStats(tries, matches)
        if card1==card2:
            print("You found a match!")
            card1.face=""
            card2.face=""
            matches+=1
        else:
            print("Not a match :(")
            card1.show=False
            card2.show=False
            
        input("Press 'ENTER' to continue")
    
    print("You found all the matches!  Game over.")
    


            
playGame()
 

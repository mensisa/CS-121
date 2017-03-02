""" Bottom up design of a 'paint by numbers' program
This file will guide you through the process I went through while 
quickly writing a program to take a sequence of numbers and translate
them into a pixelated picture using turtle graphics.  Even though I
frequently do software development in a top down way, this time I went 
bottom up.  I wanted to come up with a hands on demonstration that shows
how modular software structure works and give you a chance to write 
a collection of relatively simple functions that, when put together, do 
something reasonably cool.

In the code that follows you will find function definitions followed by
some comments and the Python keyword 'pass'.  The pass keyword does nothing
but lets you have some code that expects there to be an indented body (def, 
for, while, if, elif, else) but not have anything there.  It is a placeholder
useful for development but not usually left in released code.

For each function, carefully read the comment block and try to do what it says.
After each function there is a line or two of code which is commented out.
If you uncomment the lines you can then run the program and those lines 
will test the function immediately above it.  Once your code is working,
comment out the test lines again, and move on to the next function.
"""


import turtle

def drawSquare(length):
    """Use turtle graphics to draw a square with sides of length 'length'
    assume the pen might be up and leave the penup when the function is done.
    You should have the turtle move forward and then turn right 90 degree for 
    a total of for times.  Be sure to use begin_fill() and end_fill() to fill
    it.  Don't set the color in this function.  Assume that is set somewhere 
    else.
    """
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    pass

"""Uncomment the following lines to test drawSquare.  It should draw a single,
filled square near the middle of the screen, using the default pen color.
"""
# drawSquare(50)


def placeSquare(x,y,Length,color):
    """This function places a square of the requested color at the coordinates
    contained in x and y.  It should call the drawSquare function you just
    wrote.  Be sure to set both the pencolor, and the fill color.  Also,
    make sure the turtle is pointing straight up before the drawSquare function
    is called.
    """
    turtle.penup()
    turtle.goto(x - 300, y)
    turtle.pendown()
    turtle.color(color)
    drawSquare(Length)
    pass
    
"""Uncomment the following lines to test placeSquare.  It should draw three 
progressively larger squares in different colors diagonnally from the upper 
left to the lower right.
"""

# placeSquare(-100,100,30,"blue")
# placeSquare(0,0,40,"red")
# placeSquare(100,-100,50,"green")

    
def placeSquareRowCol(r,c,length,color):
    """ This function places a square of the desired size and color at a 
    particular row and column.  Imagine that you draw a bunch of squares 
    in a grid, like a chess board.  The r=1 and c=1 location corresponds to 
    the lower left of the grid.  r=1 and c=2 corresponds to the square
    immediately to the right, while r=2 and c=1 corresponds to the square 
    immediately above.
    This function so call the placeSquare function and you'll have to calculate
    what the x and y coordinates are.  The formula for the x coordinate should
    be something like x = (c-1) * length
    The formula for the y coordinate will be similar.
    """
    x = (c-1) * length
    y = (r-1) * length
    placeSquare(x, y, length, color)
    pass

"""Uncomment the following lines to test placeSquareRowCol.  It should draw a
two by two grid of red and blue squares, each 30x30 pixels.
"""
# placeSquareRowCol(1,1,30,"blue")
# placeSquareRowCol(1,2,30,"red")
# placeSquareRowCol(2,1,30,"red")
# placeSquareRowCol(2,2,30,"blue")


def peelNumber(n):
    """This function will take an integer n, and peel off the right most digit
    (r) and return it along with the remaining digits (rest).  
    You'll want to get the right digit by taking the remainder of n divided by
    10 (use %, the remainder operator).  The rest of the number will be the 
    original number, n, integer divided by 10.  
    The return line should look like:
    
    return r,rest
    """
    r = n % 10
    rest = n // 10
    return r, rest
    pass

"""Uncomment the following lines to test peelNumber.  It should print three
pairs of numbers: (5, 12), (2, 1),  (1, 0)
"""
# print(peelNumber(125),", ",peelNumber(12), ", ", peelNumber(1))

def numberToColor(n):
    """This function will take a single digit integer and return the name of 
    a color.  The colors map as follows:
        n==1  --> returns 'white'
        n==2  --> returns 'red'
        n==3  --> returns 'orange'
        n==4  --> returns 'green'
        n==5  --> returns 'blue'
        n==6  --> returns 'yellow'
        n==7  --> returns 'brown'
        n==9  --> returns 'black'
    
    I suggest using if-elif
    """
    if n == 1:
        return 'white'
    elif n == 2:
        return 'red'
    elif n == 3:
        return 'orange'
    elif n == 4:
        return 'green'
    elif n == 5:
        return 'blue'
    elif n == 6:
        return 'yellow'
    elif n == 7:
        return 'brown'
    elif n == 9:
        return 'black'
    pass

"""Uncomment the following lines to test the numberToColor function.  It should
print out:  red white blue
"""
# print(numberToColor(2)+" " + numberToColor(1) + " " +numberToColor(5))


def paintByNumber(n,length,row,col = 1):
    """This is the final function that takes a number, representing a sequence
    of colors, and draws the corresponding row of squares of the specified
    length.  I suggest initializing a variable to hold the column number, and
    use a while to construct a loop as follows:
        as long as n>0 do the following:
            use peelNumber(n) to get a color number, and a new value for n
            use numberToColor to get the corresponding color string
            use placeSquareRowCol to place the square
            increase the column number
    """
    while n > 0:
        colorNum, n = peelNumber(n)
        color = numberToColor(colorNum)
        placeSquareRowCol(row, col, length, color)
        col += 1
    pass


"""Uncomment the following lines to test the paintByNumber function.  It should
replicate the same two by two grid we made when testing placeSquareRowCol.
"""
# paintByNumber(52,30,1)
# paintByNumber(25,30,2)


# Once you've written and tested all of the above code, you're ready for a
# nice surprise.  Uncomment the following lines by deleting the triple quotes
# at the top and bottom, and then run the program.


#  Delete the triple quotes below this line
turtle.speed(0)
turtle.tracer(0)

paintByNumber(777711117777,15,1)
paintByNumber(177711117771,15,2)
paintByNumber(115551155511,15,3)
paintByNumber(335555555533,15,4)
paintByNumber(333555555333,15,5)
paintByNumber(332565565233,15,6)
paintByNumber(222255552222,15,7)
paintByNumber(122252252221,15,8)
paintByNumber(111122252211,15,9)
paintByNumber(113333333111,15,10)
paintByNumber(177773333771,15,11)
paintByNumber(333733377371,15,12)
paintByNumber(133393337371,15,13)
paintByNumber(111393377711,15,14)
paintByNumber(122222222111,15,15)
paintByNumber(111122221111,15,16)

paintByNumber(11111119111119111111,15,1,18)
paintByNumber(11191191911191911911,15,2,18)
paintByNumber(11919911911911919191,15,3,18)
paintByNumber(19119911999911991191,15,4,18)
paintByNumber(19111111111111111191,15,5,18)
paintByNumber(19111111111111111119,15,6,18)
paintByNumber(91111111111111111119,15,7,18)
paintByNumber(91111111111111111119,15,8,18)
paintByNumber(91111111111111111119,15,9,18)
paintByNumber(91111111111111111119,15,10,18)
paintByNumber(91111111111119999119,15,11,18)
paintByNumber(91111111111191191919,15,12,18)
paintByNumber(91999111111111991119,15,13,18)
paintByNumber(91911991111111111119,15,14,18)
paintByNumber(91911119111119119119,15,15,18)
paintByNumber(19111111911111111191,15,16,18)
paintByNumber(11111111191111111191,15,17,18)
paintByNumber(11111111191911119191,15,18,18)
paintByNumber(11111111119199991911,15,19,18)
paintByNumber(1111111111111111111111,15,20,18)
turtle.hideturtle()
turtle.update()


turtle.hideturtle()
turtle.done()
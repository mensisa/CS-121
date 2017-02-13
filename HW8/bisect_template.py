def f(x):
    """You can put something different here if you want to have your program
    solve different equations"""
    return 3 * x ** 3 - 4 * x ** 2 + 2 * x - 5


"""

Here is the pseudo code for the implementation of the bisect method for 
finding the root (zero) of a function.  Try to translate it into Python using
a while loop.  I've included a function definition for f() (up above), so you
can call it in your program in the same way you would call a built in function
like print() or min() or max().  Pseudo code kind of looks like a program, but
its syntax is generic rather than being in a specific programming language.
The idea is that it provides enough structure and detail to make it easy to
write in whatever programming language you wish.  

For information on how the bisect method works, see:
        https://en.wikipedia.org/wiki/Bisection_method


INPUT: Function f, endpoint values a, b, tolerance TOL, maximum iterations NMAX
CONDITIONS: a < b, either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
OUTPUT: value which differs from a root of f(x)=0 by less than TOL

solutionFound = False 
N ← 1
While N ≤ NMAX # limit iterations to prevent infinite loop
  c ← (a + b)/2 # new midpoint
  If f(c) = 0 or (b – a)/2 < TOL then # solution found
    Output(N,c)
    solutionFound = True
    exit loop
  EndIf
  N ← N + 1 # increment step counter
  If sign(f(c)) = sign(f(a)) then a ← c else b ← c # new interval
EndWhile
If solutionFound is not True then 
    Output("Method failed.") # max number of steps exceeded
EndIf
"""
print("a = left bracket point (x value)")
print("b = right bracket point (x value)")
print("TOL = how close to true answer is acceptable")
print("NMAX = maximum allowable iterations")
print()

a, b, TOL, NMAX = eval(input("Enter a, b, TOL, NMAX: "))

solutionFound = False
N = 1
while N <= NMAX:
    c = (a + b) / 2
    if f(c) == 0 or (b - a) / 2 < TOL:
        print("iterations =", N, "\tsolution =", c)
        solutionFound = True
        break
    N += 1
    if f(c) * f(a) > 0:
        a = c
    else:
        b = c
if not solutionFound:
    print("Method failed.")

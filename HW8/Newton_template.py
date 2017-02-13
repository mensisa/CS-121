import math

def f(x):
    """You can put something different here if you want to have your program
    solve different equations"""
    return 3*x**3 - 4*x**2 + 2*x - 5

def fprime(x):
    """You can put something different here if you want to have your program
    solve different equations.  Note:  this has to be the derivative of the
    function in f(x)."""
    return 9*x**2 - 8*x + 2 
    
"""
Below is the psuedo code for a different method for finding roots, called
the Newton-Raphson method.  It uses both the function f, and its derivative
fprime.  I've defined functions for these above.  For information on the
Newton-Raphson method, see:  https://en.wikipedia.org/wiki/Newton's_method



read a, M, eps
N=0
repeat
    delta = f(a)/fprime(a)
    a = a - delta
    N=N+1
until |delta| < epsilon or N=M
print "approximation to root is", a
if |delta|>=eps then do
    print "required accuracy not reached in", M, "iterations"
endif

"""
a, M, epsilon = eval(input("Enter inital guess, maxiterations, and tolerance: "))

#Enter your code here, guided by pseudo code above.
N = 0
for N in range(0, M + 1):
    delta = f(a) / fprime(a)
    a -= delta
    N += 1
    if abs(delta) < epsilon:
        break
print("approximation to root is", a, "found in", N, "iterations")
if abs(delta) >= epsilon:
    print("required accuracy not reached in", M, "iterations")
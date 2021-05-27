import numpy as np
from scipy import optimize
import sympy

def func():
    h1 = 10 ** (-4.70)
    #h1 = 10 ** (-4.342)
    h2 = 10 ** (-9.30)
    #h2 = 10 ** (-8.898)
    x1 = 5.26
    x2 = 10.59
    #x2 = 10.521
    k1 = 5.04 * (10 ** (-3))
    #k1 = 1.48 * (10 ** (-2))
    c1 = 0.01
    c2 = 0.09505
    v = 50
    kw = 0.68e-14

    #sympy.var("x y")
    x, y = sympy.symbols("x, y")

    A1 = (c1 * v) / (1 + (h1 / x) + ((h1*h1) /(x * y)) + (h1*h1*h1 /(x * y * k1)))
    print("A1")
    #display(A1)
    print()

    A2 = (c1 * v) / (1 + (h2 / x) + (h2*h2 /(x * y)) + (h2*h2*h2 /(x * y * k1))) 

    s1 = (h1*h1 * A1 /(x * y) + 2 * h1 * A1/x + 3*A1 - h1 * v + kw*v/h1) / (h1 - kw/h1 + c2) - x1

    s2 = (h2*h2 * A2 /(x * y) + 2 * h2 * A2/x + 3*A2 - h2 * v + kw*v/h2) / (h2 - kw/h2 + c2) - x2

    #display(s1)
    #display(s2)
    s = sympy.solve([s1, s2], [x, y])
    print(s)
    #display(s)
    #return [[s1 - x1], [s2 - x2]]




if __name__ == "__main__":
    #result = optimize.root( func, [ 1.0, 0.0], method="broyden1")
    #print(result)
    func()
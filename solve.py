import numpy as np
from scipy import optimize
import sympy

def func():
    h1 = 10 ** (-4.70)
    h2 = 10 ** (-9.30)
    x1 = 5.26
    x2 = 10.59
    k1 = 5.04 * (10 ** (-3))
    c1 = 0.01
    c2 = 0.09505
    v = 50
    kw = 0.68e-14
    delta = 1e-14

    sympy.var("x y")

    A1 = (c1 * v) / (1 + (h1 / k1) + (h1*h1 /(k1 * x)) + (h1*h1*h1 /(k1 * x * y)))

    A2 = (c1 * v) / (1 + (h2 / k1) + (h2*h2 /(k1 * x)) + (h2*h2*h2 /(k1 * x * y))) 

    s1 = (h1*h1*h1 * A1 /(k1 * x) + 2 * h1 * A1/k1 + 3*A1 - h1 * v + kw*v/h1) / (h1 - kw/h1 + c2) - x1

    s2 = (h2*h2*h2 * A2 /(k1 * x) + 2 * h2 * A2/k1 + 3*A2 - h2 * v + kw*v/h2) / (h2 - kw/h2 + c2) - x2

    s = sympy.solve([s1, s2], [x, y])
    print(s)
    #return [[s1 - x1], [s2 - x2]]




if __name__ == "__main__":
    #result = optimize.root( func, [ 1.0, 0.0], method="broyden1")
    #print(result)
    func()
import numpy as np
from scipy import optimize

def f(x): return (x-0.3)**2 * np.exp(x)

def quad_interp(f, a, b, c):
    e = 1e-7
    q0 = a*f(b)*f(c) / (e + (f(a)-f(b))*(f(a)-f(c)))
    q1 = b*f(a)*f(c) / (e + (f(b)-f(a))*(f(b)-f(c)))
    q2 = c*f(a)*f(b) / (e + (f(c)-f(a))*(f(c)-f(b)))
    return q0+q1+q2


def golden(f, x1, x4):
    z = (1 + np.sqrt(5)) / 2
    p0 = x1*(z-1)
    x2 = (x4 + x1 + p0) / (1+z)
    x3 = (z*x2) - p0
    if f(x2) <= f(x3):
        step = x4 - x3
        return x1, x2, x3, step
    else:
        step = x2 - x1
        return x2, x3, x4, step

def Brent(f, a, c, tol):
    a, b, c, step = golden(f, a, c)
    while abs(a-c) > tol:
        s = quad_interp(f, a, b, c)
        if s > c or s < a:
            a, b, c, step = golden(f, a, c)
            continue
        else:
            if f(a) <= f(c):
                if s > b:
                    step2 = c - s
                    if step2 >= step:
                        a, b, c = a, b, s
                        continue
                    else: 
                        a, b, c, step = golden(f, a, c)
                        continue
                else:
                    step2 = c - b
                    if step2 >= step:
                        a, b, c = a, s, b
                        continue
                    else:
                        a, b, c, step = golden(f, a, c)
                        continue
            else: 
                if s > b:
                    step2 = b - a
                    if step2 >= step:
                        a, b, c = b, s, c
                        continue
                    else: 
                        a, b, c, step = golden(f, a, c)
                        continue
                else:
                    step2 = s - a
                    if step2 >= step:
                        a, b, c = s, b, c
                        continue
                    else:
                        a, b, c, step = golden(f, a, c)
                        continue
    return b

minimum = Brent(f, -1, 2, 1e-6)
print(minimum)

min_scipy = optimize.brent(f)
print(min_scipy)
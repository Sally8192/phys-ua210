import numpy as np 

def f(x):
    f = x*(x - 1)
    return f


def derivative(value, delta):
    x = value
    d = delta
    return ( f(x + d) - f(x) ) / d

print(derivative( 1, 1e-2))
print(derivative( 1, 1e-4))
print(derivative( 1, 1e-6))
print(derivative( 1, 1e-8))
print(derivative( 1, 1e-10))
print(derivative( 1, 1e-12))
print(derivative( 1, 1e-14))
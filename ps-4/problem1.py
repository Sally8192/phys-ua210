from numpy import *
import matplotlib.pyplot as plt

def trapezoid(f,N):
    h = (b-a)/(N)
    x = linspace(a,b,N+1) 
    
    weight = ones(N+1) 
    weight[0] = 0.5
    weight[-1] = 0.5
    
    return h*sum(weight*f(x))

N1 = 10 
a = 0
b = 2

def f(x):
    return x**4-2*x+1

I1 = trapezoid(f,N1)
I2 = trapezoid(f,2*N1)
error = (1/3)*(I2-I1)

print(f'Integral estimate (N1 = {N1}): {I1:.4f}')
print(f'Integral estimate (N2 = {2*N1}): {I2:.4f}')
print(f"The estimated error on the integral for {2*N1} slices is {error}")
print(f"Directly calculating the error via difference between actual and calculated result produces {4.4-I2}")
print("The percent difference between estimated and true error is",100*abs(4.4-I2-error)/abs(4.4-I2),"%")
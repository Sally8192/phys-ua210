import numpy as np
import matplotlib.pyplot as plt
from random import random


NTl = 1000            
NPb = 0              
tau = 3.053*60       
h = 1.0               
p = 1 - 2**(-h/tau)   
tmax = 1000           

tpoints = np.arange(0.0,tmax,h)
Tlpoints = []
Pbpoints = []


for t in tpoints:
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)

    
    decay = 0
    for i in range(NTl):
        if random()<p:
            decay += 1
    NTl -= decay
    NPb += decay


plt.plot(tpoints,Tlpoints,label='Tl')
plt.plot(tpoints,Pbpoints,label='Pb')
plt.xlabel("Time(s)")
plt.ylabel("Number of atoms")
plt.title('Decay of 208Tl Over Time')
plt.legend()
plt.savefig('Decay2.png')
plt.show()

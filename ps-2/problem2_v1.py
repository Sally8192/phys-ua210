import numpy as np

def madelung_constant(L):
    # L: number of atoms in all direction

    M = 0
   
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if (i==j==k==0):
                    continue
                
                M += (-1)**(i+j+k)/(np.sqrt(i**2+j**2+k**2))

    return abs(M)


print("The Madelung constant of NaCl is",madelung_constant(100)) 

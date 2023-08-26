# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:25:13 2023

@author: Lakshya Singh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 07:47:12 2023

@author: Lakshya Singh
"""

import numpy as np
from math import factorial
from tabulate import tabulate
#import random as ran
import matplotlib.pyplot as plt 
from itertools import permutations, combinations



N = 4 #no. of coins tossed for making table
n = 4 #no. of coins tossed for making graph


c1 = np.arange(1,N+2,1)
c2 = np.arange(N,-1,-1)
c3 = np.arange(0,N+1,1)

#for plotting
c2_new = np.arange(n,-1,-1)

h = []
for k in range(0,len(c2_new)):
    h.append(factorial(n)/(factorial(c2_new[k])*factorial(n-c2_new[k])))
 
plt.rcParams["figure.dpi"] = 100    
plt.plot(c2_new,h, marker = "o",lw = 2,color = "g")
plt.xlabel("No. of Heads appeared")
plt.ylabel("Thermodynamic Probability")
plt.title(f"Probability Distribution Curve for {n} coins")

"""
for m in range(len(h)):
    plt.annotate(f"({c2_new[m]},{h[m]})",xy = (c2_new[m],h[m]),fontsize=11,fontweight ="bold")
"""

#for table    
# create header
head = ["S.No.", "N1","N2","Microstates","Thermo Prob.","True Prob."]
mydata = []

for i in range(len(c1)):
    samp1 = ["H"]*c2[i]
    samp2 = ["T"]*c3[i]
    samp = samp1 + samp2
    
   
    perm = list(permutations(samp,N))
    
    new_perm = []
    [new_perm.append(x) for x in perm if x not in new_perm]

    
    w = []
    N1 = []
    prob = []
    for k in range(0,len(new_perm)):
        N1.append(new_perm[k].count("H"))
        w.append(factorial(N)/(factorial(N1[k])*factorial(N-N1[k])))
        prob.append(w[k]/2**N)


    wi = []
    [wi.append(x) for x in w if x not in wi]

    probi = []
    [probi.append(x) for x in prob if x not in probi]
    
    arr = np.array(new_perm)
    
    mydata.append([c1[i],c2[i],c3[i],arr,wi[0],probi[0]])
    #print(probi)
    

print(f"                          Table for {N} coins")
print()
print(tabulate(mydata, headers=head, tablefmt="grid",numalign="center"))

    




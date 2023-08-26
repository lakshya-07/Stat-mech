# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:43:48 2023

@author: thirdyear
"""

import matplotlib.pyplot as plt
from math import exp
import numpy as np
from scipy.integrate import quad

R = 8.3144598 #J/mol-K
h = 6.63*1e-34 #Js
Kb = 1.38*1e-23 #J/k
Na = 6.023*1e23

def classical(t):
    return 3.0*R
    
v = 1.0e13 #Hz
e = h*v/Kb #K  
def einstein(t):
    p = e/t
    q = np.exp(p)
    r = 3.0*Na*Kb*p*p*(q)/(((q-1)*(q-1)))
    return r


e = 88 #K  debye temp for lead
def debye(t):
    p = t/e
    return 9.0*Na*Kb*p**3
    
funct = lambda x: exp(x)*x**4/((exp(x)-1)**2)

def simp(a,b,n):
    h = (b-a)/n
    s1 = funct(a)-funct(b)
    
    for i in range(1,n):
        v = a + i*h
        
        if(i % 2 == 0):
            s1 = s1 + 2*funct(v)
        else:
            s1 = s1 + 4*funct(v)
    return s1*(h/3)       
 

t = np.arange(1.0,500.0,0.5)
   
intgral = [simp(0.000001,e/t[i],1000) for i in range(len(t))]
intgrl_new = [quad(funct,0.0001,e/t[i]) for i in range(len(t))]


cv1 = [classical(t[i]) for i in range(len(t))]
cv2 = [einstein(t[i]) for i in range(len(t))]
cv3 = [debye(t[i])*intgral[i] for i in range(len(t))]

cv3_new = [debye(t[i])*intgrl_new[i][0] for i in range(len(t))]
print(intgrl_new)


plt.rcParams["figure.dpi"] = 100
plt.subplots_adjust(wspace = 0.6,hspace = 0.6)

plt.suptitle("Specific heat (Cv,J/kg-K) Vs Temperature (T,K)")
plt.plot(t,cv1, color = "r", lw = 2,label = "Classical model")
plt.plot(t,cv2,color = "g", lw =2, label = "Einstein model")  
plt.plot(t,cv3,color = "y", lw = 3, label = "Debye model") 
plt.plot(t,cv3_new,color = "k", lw = 2,ls = "--", label = "Debye model (inbuilt integration)")  
plt.xlabel("Temperature (Kelvin)") 
plt.ylabel("Specific heat (Cv,J/kg-K)")
plt.ylim(0,28)
plt.legend(loc = "lower right")





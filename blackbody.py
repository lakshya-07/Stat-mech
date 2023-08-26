# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 08:42:23 2023

@author: thirdyear
"""

import matplotlib.pyplot as plt
from math import exp
import numpy as np
from scipy.integrate import quad

h = 6.626e-34 #Js
c = 3e8
Kb = 1.38e-23 #J/k
pi = np.pi

def planck(w,T):
    a = (8.0*pi*h*c)/(w**5.0)
    b = (exp((h*c/(w*Kb*T))-1))
    U = a/b
    return U #(8.0*pi*h*c)/(w**5.0*(exp((h*c/(w*Kb*T))-1)))
    
def rayleigh(w,T):
    return (8.0*pi*Kb*T)/(w**4.0)    
  
w1 = np.arange(1e-7,0.25e-5,1e-8)   # in metre
w2 = w1
#w2 = np.linspace(1e-4,1e-3,100)  
T = [3000,4000,5000]  #temperature


planck1 = [planck(w1[i],T[0]) for i in range(len(w1))]
rayleigh1 = [rayleigh(w2[i],T[0]) for i in range(len(w2))]


planck2 = [planck(w1[i],T[1]) for i in range(len(w1))]
rayleigh2 = [rayleigh(w2[i],T[1]) for i in range(len(w2))]

planck3 = [planck(w1[i],T[2]) for i in range(len(w1))]
rayleigh3 = [rayleigh(w2[i],T[2]) for i in range(len(w2))] 
print(max(planck1))
plt.rcParams["figure.dpi"] = 100


plt.subplots_adjust(wspace = 1.6,hspace = 1.6)
plt.subplots(figsize=(6,8))

plt.suptitle("Blackbody radiation: Energy Density(u(w)dw v/s Temperature (T,K)")
plt.subplot(3,1,1)
plt.annotate(f"T = {T[0]} K", xy = (0.8e-6,max(planck1)))
plt.annotate(f"T = {T[1]} K", xy = (0.7e-6,max(planck2)))
plt.annotate(f"T = {T[2]} K", xy = (0.6e-6,max(planck3)))
plt.plot(w1,planck1, color = "r", lw = 2)
plt.plot(w1,planck2, color = "g", lw = 2,) 
plt.plot(w1,planck3, color = "b", lw = 2)
#plt.title("Planck's Blackbody Radition")
plt.ylabel("Planck's U(w)dw")
  


plt.subplot(3,1,2)
plt.plot(w2,rayleigh1,color = "r",label = f"T = {T[0]} K")
plt.plot(w2,rayleigh2,color = "g",label = f"T = {T[1]} K") 
plt.plot(w2,rayleigh3,color = "b",label = f"T = {T[2]} K")
#plt.title("Rayleigh-Jean's Blackbody Radition") 
plt.xlim(0.8e-7,0.2e-6)
plt.ylabel("Rayleigh-Jean's U(w)dw")
plt.legend() 



plt.subplot(3,1,3)
plt.plot(w1,planck3, color = "b", lw = 2,label = "Planck's Blackbody")
plt.plot(w2,rayleigh3,color = "k",ls = "--", label = "Rayleigh-Jean's Blackbody")
plt.annotate(f"T = {T[2]} K", xy = (0.5e-6,max(planck3)))
plt.ylim(0,0.2e7)
plt.xlabel("Wavelength (m)")
plt.ylabel("Energy Densit U(w)dw")
plt.legend() 

plt.show()
  
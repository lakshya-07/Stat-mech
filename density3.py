# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:50:16 2023

@author: Lakshya Singh
"""

# non relativistic fermions at low and high temperature 


import numpy as np
import matplotlib.pyplot as plt 

#Kb = 1 #8.61733*1e-5 #eV/K
mu = 1 #eV
T = [100,1000] #kelvin
h = 6.626e-34#4.135e-15 #ev
Kb = 1.38e-23 #Boltzmann constant(joule per kelvin) 
ch = 1.6e-19 #charge


ei = np.arange(0,2,1e-3) #in eV
#x = ((ei-mu))/(Kb*T)

def funct(x,c,T):
    v = ((x-mu))/(Kb*T)
    return  1/(np.exp(v*ch) + c)

def den1(e):
    s = 0.5  #(electrons)
    V = 1
    m = 9.1e-31 # mass particle in kg 
    A = (2*s+1)*((2.0*m)**(3.0/2.0))
    B = 2*e**(0.5)*np.pi*V/(h**3)
    return A*B


density = [den1(ei)*funct(ei,1,T[0]), den1(ei)*funct(ei,1,T[1])]
 
#print(ei)
plt.rcParams["figure.dpi"] = 100
plt.subplots(figsize=(10,8))

plt.subplot(3,2,1)    
plt.plot(ei,den1(ei),c = "g")
plt.ylabel("g(e)")
plt.grid(True)

plt.subplot(3,2,3)    
plt.plot(ei,funct(ei,1,T[0]),lw = 2, label = f"T = {T[0]} K",c = "g")
plt.ylabel("n(e)")
plt.legend()
plt.grid(True)

plt.subplot(3,2,5)  
plt.plot(ei,density[0],lw = 2, label = f"T = {T[0]} K",c = "g")
plt.grid(True)
plt.ylabel("dn/dE")
plt.xlabel("Energy (in eV)")
plt.legend()
plt.grid(True)
plt.show() 

plt.subplots(figsize=(10,8))

plt.subplot(3,2,2)    
plt.plot(ei,den1(ei),lw = 2,c = "r")
plt.ylabel("g(e)")
plt.grid(True)

plt.subplot(3,2,4)    
plt.plot(ei,funct(ei,1,T[1]),lw = 2, label = f"T = {T[1]} K",c = "r")
plt.ylabel("n(e)")
plt.legend()
plt.grid(True)

plt.subplot(3,2,6)  
plt.plot(ei,density[1],lw = 2, label = f"T = {T[1]} K",c = "r")
plt.grid(True)
plt.ylabel("dn/dE")
plt.xlabel("Energy (in eV)")
plt.legend()
plt.grid(True)
plt.show() 

#plt.subplots_adjust(wspace = 2,hspace = 10)



# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:42:58 2023

@author: Lakshya Singh
"""



# relativistic Fermions at low and high temperature 


import numpy as np
import matplotlib.pyplot as plt 

#Kb = 1 #8.61733*1e-5 #eV/K
mu = 1 #eV
T = [1e8,1e9] #kelvin
h = 6.626e-34#4.135e-15 #ev
#e = 1.6e-19 #electric charge  
Kb = 1.38e-23 #Boltzmann constant(joule per kelvin) 
ch = 1.6e-19 
vel = 3e8

ei = np.arange(0,2,1e-3) #in MeV
#x = ((ei-mu))/(Kb*T)

def funct(x,c,T):
    v = ((x-mu))/(Kb*T)
    return  1/(np.exp(v*ch*1e6) +c)

def den1(e):
    s = 0.5  #(electrons)
    V = 1
    A = (2*s+1)*4
    B = e**(2)*np.pi*V/((vel*h)**3)
    return A*B


density = [den1(ei)*funct(ei,1,T[0]), den1(ei)*funct(ei,1,T[1])]
 
#print(ei)
plt.rcParams["figure.dpi"] = 100
plt.subplots(figsize=(10,8))

plt.subplot(3,2,1)    
plt.plot(ei,den1(ei),lw = 2)
plt.ylabel("g(e)")
plt.grid(True)

plt.subplot(3,2,3)    
plt.plot(ei,funct(ei,1,T[0]),lw = 2, label = f"T = {T[0]} K")
plt.ylabel("n(e)")
plt.legend()
plt.grid(True)

plt.subplot(3,2,5)  
plt.plot(ei,density[0],lw = 2, label = f"T = {T[0]} K")
plt.grid(True)
plt.ylabel("dn/dE")
plt.xlabel("Energy (in MeV)")
plt.legend()
plt.grid(True)
plt.show() 

plt.subplots(figsize=(10,8))

plt.subplot(3,2,2)    
plt.plot(ei,den1(ei),lw = 2,c = "m")
plt.ylabel("g(e)")
plt.grid(True)

plt.subplot(3,2,4)    
plt.plot(ei,funct(ei,1,T[1]),lw = 2, label = f"T = {T[1]} K",c = "m")
plt.ylabel("n(e)")
plt.legend()
plt.grid(True)

plt.subplot(3,2,6)  
plt.plot(ei,density[1],lw = 2, label = f"T = {T[1]} K",c = "m")
plt.grid(True)
plt.ylabel("dn/dE")
plt.xlabel("Energy (in MeV)")
plt.legend()
plt.grid(True)
plt.show() 
#plt.subplots_adjust(wspace = 2,hspace = 10)














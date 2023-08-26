# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:40:56 2023

@author: Lakshya Singh
"""

import numpy as np
import matplotlib.pyplot as plt 

Kb = 8.61733*1e-5 #eV/K
mu = 0 #eV
T = 1000 #kelvin
#e = 1.6e-19 #electric charge  
#Kb = 1.38e-23 #Boltzmann constant(joule per kelvin) 

ei = np.linspace(-0.4,0.4,1001)


def funct(x,c,T):
    v = ((x-mu))/(Kb*T)
    return  1/(np.exp(v)+c)


plt.rcParams["figure.dpi"] = 100
plt.plot(ei,funct(ei,0,T),lw = 2, label = "Maxwell-Boltzmann")
plt.plot(ei,funct(ei,-1,T),lw = 2, label = "Bose-Einstein")
plt.plot(ei,funct(ei,1,T),lw = 2, label = "Fermi-Dirac")
plt.ylim(0,3)
plt.ylabel("Distribution Functions (f)")
plt.xlabel("Energy (in eV)")
plt.title(f"Comparison of distribution functions for M-B,F-D,B-E \n at T = {T}K")
plt.grid(True)
plt.legend()


temp = np.arange(500,1500,200)
plt.subplots_adjust(wspace = 1.6,hspace = 1.6)
plt.subplots(figsize=(5,8))

for i in range(len(temp)):
    plt.subplot(3,1,1)
    plt.plot(ei,funct(ei,0,temp[i]),lw = 2, label = f"T = {temp[i]} K")
    plt.ylim(0,1)
    plt.xlim(0,0.4)
    plt.grid(True)
    plt.ylabel("M-B Function")
    plt.legend()


    plt.subplot(3,1,2)
    plt.plot(ei,funct(ei,-1,temp[i]),lw = 2, label = f"T = {temp[i]} K")
    plt.ylim(0,4)
    plt.xlim(0,0.4)
    plt.grid(True)
    plt.ylabel("B-E Function")
    plt.legend()



    plt.subplot(3,1,3)
    plt.plot(ei,funct(ei,1,temp[i]),lw = 2, label = f"T = {temp[i]} K")
    plt.ylim(0,1.0)
    plt.grid(True)
    plt.xlabel("Energy (in eV)")
    plt.ylabel("F-D Function")
    plt.legend()

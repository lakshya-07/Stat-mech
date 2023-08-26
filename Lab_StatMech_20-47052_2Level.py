# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 06:25:59 2023

@author: Lakshya Singh
"""

import sympy as sp
from sympy import exp, log, lambdify
#from sympy.utilities.lambdify import implemented_function
import numpy as np
import matplotlib.pyplot as plt 


beta,e,Kb,T = sp.symbols("beta,e,Kb,T")


n = 2 #no. of particles
E = [0,0.01] #energy levels in eV
Kb = 8.617e-5 #eV/K

z = 0
for i in range(len(E)):
    z += exp(-E[i]/(Kb*T))

Z = sp.Function("Z")("T")
Z = z**n

F = sp.Function("F")("T")
F = -Kb*T*log(Z) # helmholtz free energy

U = sp.Function("U")("T")
U = Kb*T*T*sp.diff(log(Z),T).simplify()  #average energy

S = sp.Function("S")("T")
S = -sp.diff(F,T).simplify()  #entropy

Cv = sp.Function("Cv")("T")
Cv = sp.diff(U,T).simplify()     #specific heat


U_new = sp.Function("U")("T")
U_new = n*E[1]/(exp(E[1]/(Kb*T))+1)  #average energy

S_new = sp.Function("S_new")("T")
S_new = (n)*((1/T)*(E[1]/(exp(E[1]/(Kb*T))+1))+(log(z)*Kb))

Cv_new = sp.Function("Cv_new")("T")
Cv_new = n*(E[1]**2)*(exp(E[1]/(Kb*T)))/(Kb*T*T*(exp(E[1]/(Kb*T))+1)**2)     #specific heat           
           
param = [Z,F,U,S,Cv]

param2 = [U_new,S_new,Cv_new]
ylabel = ["Partition Function, Z","Helmholtz Free Energy,F","Average Energy, U","Entropy, S","Specific Heat, Cv"]
colors = ["r","g","b","orange","violet"]

plt.rcParams["figure.dpi"] = 100
plt.subplots_adjust(wspace = 1.2,hspace = 0.7)
plt.suptitle("Plots of various Thermodynamic Properties for Maxwell Boltzman Statistics", va = "baseline")

for k in range(len(param)):
    thermo_prop = lambdify(T, param[k], 'numpy') 
    print(param[k])
    print()
    temp = np.arange(0.05,1000,1)
    val = thermo_prop(temp)
    plt.subplot(2,3,k+1)
    plt.plot(temp,val, color = colors[k])
    plt.xlabel("Temperature,T")
    plt.ylabel(ylabel[k])
 
    
print() 
for k in range(len(param2)):
    thermo_prop2 = lambdify(T, param2[k], 'numpy') 
    print(param2[k])
    temp = np.arange(0.05,1000,0.5)
    val2 = thermo_prop2(temp)
    plt.subplot(2,3,k+3)
    plt.plot(temp,val2, ls = "--", color = "k")
   


    





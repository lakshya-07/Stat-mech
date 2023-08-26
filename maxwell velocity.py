import sympy as sp
import numpy as np
from scipy.integrate import quad
from sympy import exp,lambdify,oo
import matplotlib.pyplot as plt 

T,v,Kb,m,pi = sp.symbols("T,v,Kb,m,pi")


A = (4*pi)*(m/(2*pi*Kb*T))**(3/2)
B = (v**2)*exp((-m*v**2)/(2*Kb*T))
Prob = A*B


mps = sp.diff(Prob,v).simplify()
mps = sp.solve(mps,v)


print("The calculated most probable speed formula are ",mps)
print()


params = {Kb:1.38e-23, m:32*1.66e-27, pi:np.pi}
Prob = Prob.evalf(subs = params )
mps[2] = mps[2].evalf(subs = params )

Prob_fn = lambdify([v,T], Prob, 'numpy') 
v_mp = lambdify(T,mps[2], 'numpy')



T = [300,500,1000]
v = np.arange(0,2000,1)

#print(Prob_fn(500,T[0]))


for i in range(len(T)):
    Kb = 1.38e-23 #Boltzmann constant(joule per kelvin) 
    m = 32*1.66e-27
    v_avg = np.sqrt(8*Kb*T[i]/(np.pi*m))
    v_rms = np.sqrt(3*Kb*T[i]/m)
    print("The most probable speed at T = ",T[i],"K is ",v_mp(T[i]))
    print("The average speed at T = ",T[i],"K is ",v_avg)
    print("The root mean square speed at T = ",T[i],"K is ",v_rms)
    print()


vels = []    
for i in range(len(T)):
    val = Prob_fn(v,T[i])
    plt.plot(v,val, lw = 2, label = f"T = {T[i]} K")
    vels.append(round(v_mp(T[i]),3))
    plt.annotate(f"V(mp) = {vels[i]} m/s",xy = (vels[i],Prob_fn(vels[i],T[i])))
    
    
plt.rcParams["figure.dpi"] = 100
plt.ylabel("Distribution Function, N(v)dv")
plt.xlabel("Speed,v (m/s)")
plt.title("Plot of Maxwell Speed Distribution Function \n for O2 gas")
plt.grid(True)
plt.legend()





"""
import numpy as np
import matplotlib.pyplot as plt 

#Kb = 8.61733*1e-5 #eV/K
#e = 1.6e-19 #electric charge 
#N = 6.022e26
 
Kb = 1.38e-23 #Boltzmann constant(joule per kelvin) 

m = 32*1.66e-27
v = np.arange(0,2000,1)
T = [300,500,1000]

def funct(v,T):
    A = (4*np.pi)*(m/(2*np.pi*Kb*T))**(3/2)
    B = (v**2)*np.exp((-m*v**2)/(2*Kb*T))
    return A*B


for i in range(len(T)):
    v_avg = np.sqrt(8*Kb*T[i]/(np.pi*m))
    v_rms = np.sqrt(3*Kb*T[i]/m)
    v_prob = np.sqrt(2*Kb*T[i]/m)
    print("The average speed at T = ",T[i],"K is =",v_avg)
    print("The root mean square speed at T = ",T[i],"K is =",v_rms)
    print("The most probable speed at T = ",T[i],"K is =",v_prob)
    print()
    
for i in range(len(T)):
    val = funct(v,T[i])
    plt.plot(v,val, lw = 2, label = f"T = {T[i]} K")
    
    
plt.rcParams["figure.dpi"] = 100
plt.ylabel("Distribution Function, N(v)dv")
plt.xlabel("Speed,v (m/s)")
plt.title("Plot of Maxwell Speed Distribution Function \n for O2 gas")
plt.grid(True)
plt.legend()


"""

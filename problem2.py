from functions import *
from plotting import *
import numpy as np

def makeK(z,L): #K from eq 11 in problem text
    Larr=np.full(len(z),L)
    return 0.001+(0.02/7)*z*np.exp(-z/7)+(0.05/10)*(Larr-z)*np.exp(-(Larr-z)/10)

kw=6.97e-5
day=86400 #1day in seconds
Ceq=5060*415e-6

T=10*day
L=100
dt=0.8
dz=0.1 
timesteps=int(T/dt)
t=np.linspace(0,T,timesteps)

def shallowSim(T,L,dt,dz,kw,Ceq,npyFile):
    N=int(L/dz)
    timesteps=int(T/dt)
    z=np.linspace(0,L,N)
    Ceqs=np.full(timesteps,Ceq)
#initialization
    K=makeK(z,L)
    Cinit=np.zeros(N) #zero initial concentration
    S=makeS(N,timesteps,Ceqs,kw,dz,dt,K)
    
    C=runSimulation(Cinit,dt,dz,K,kw,timesteps,S)
    np.save(npyFile,C)


#shallowSim(T,L,dt,dz,kw,Ceq,"dt"+str(dt)+".npy")
#shallowCdt1=np.load("dt1.npy")
#shallowCdt10=np.load("dt10.npy")

#For later
#shallowCdt10min,shallowCdt10max=minAndMaxConcentrations(shallowCdt10)
#plotMinAndMaxConcentrations(t,shallowCdt10min,shallowCdt10max,Ceq,"variable")

def checkMaxError(C,Ctest):
    x=int(len(C)/len(Ctest))
    Csub=C[::x] #array with every xth column of C
    errors=np.abs(Csub-Ctest) #array with absolute value of the difference between each of the elements of C and Ctest
    return np.amax(errors) #return largest error

Cdt1=np.load("dt1.npy")
Cdt10=np.load("dt10.npy")
Cdt2=np.load("dt2.npy")
Cdt08=np.load("dt0.8.npy")
print("ok")
print("maxError",checkMaxError(Cdt08,Cdt2))

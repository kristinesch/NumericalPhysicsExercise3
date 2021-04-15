from functions import *

N=5
kw=0.0000697
K=[1,1,1,1,1,1]
dt=0.01
dz=0.01
Cinit=[1,1,1,1,1,1]
timesteps=50
S=np.zeros((timesteps,N+1))

C=runSimulation(Cinit,dt,dz,K,kw,timesteps,S)
print(C)
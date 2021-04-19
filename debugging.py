from functions import *
from plotting import *
from scipy.stats import norm

N=100
dz=10
dt=10
timesteps=1000
kw=1
Cinit=np.zeros(N)

z=np.linspace(1,N,N)
K=np.sin(2*z)+10

HpCO2=2
Ceq=np.full(timesteps,HpCO2)
S=makeS(N,timesteps,Ceq,kw,dz,dt,K)



C=runSimulation(Cinit,dt,dz,K,kw,timesteps,S)
print(C)
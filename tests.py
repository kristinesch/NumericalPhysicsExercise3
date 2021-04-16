from functions import *
from plotting import *

def test1(N,dt,dz,timesteps):
    K=np.linspace(1,10,N)

    #initialize C
    C1init=np.zeros(N)
    C1init.fill(1)
    print("Cinit",C1init)

    S=np.zeros((timesteps,N))

    C=runSimulation(C1init,dt,dz,K,kw,timesteps,S)
    print(C)
    np.save("Ctest1",C)
    plotConcentrations("Ctest1.npy","test1")

N=100
kw=0
dt=0.01
dz=0.01
timesteps=100

test1(N,dt,dz,timesteps)


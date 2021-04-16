from functions import *
from plotting import *
from scipy.stats import norm

def test1(N,dt,dz,timesteps):
    K=np.linspace(1,10,N)

    #initialize C
    C1init=np.zeros(N)
    C1init.fill(1)
    print("Cinit",C1init)

    S=np.zeros((timesteps,N))

    C=runSimulation(C1init,dt,dz,K,kw,timesteps,S)
    plotConcentrations(C,"test1")

def test2(N,dt,dz,timesteps):
    S=np.zeros((timesteps,N))
    x=np.linspace(1,10,N)
    K=np.full(N,1)
    Cinit=norm.pdf(x,N/2,N/5) #normal distribution
    C=runSimulation(Cinit,dt,dz,K,kw,timesteps,S)
    massDiff=massDifference(C)
    print(np.sum(C[0]))
    #print(massDiff)
    plotMassDifference(massDiff)
    plotConcentrations(C,"test2C")

def test3(N,dt,dz,timesteps):
    S=np.zeros((timesteps,N))
    z=np.linspace(1,N,N)
    print(z)
    K=np.full(N,1)
    print(K)
    Cinit=norm.pdf(z,N/2,2*dz) #normal distribution, very thin
    C=runSimulation(Cinit,dt,dz,K,kw,timesteps,S)
    plotConcentrations(C,"test3C")
    #print(C)
    sigmas=[]
    for Ci in C:
        #print(Ci)
        mu=np.sum(np.dot(Ci,z)*dz)/np.sum(Ci*dz)
        print(mu)
        #print(Ci*((z-mu)@(z-mu)))
        sigmas.append(np.sum(Ci*((z-mu)**2)*dz)/(np.sum(Ci)*dz))
        
    #print(sigmas)
    plotSigma(sigmas,K)



"""Test 1"""
N=100
kw=0
dt=1
dz=1
timesteps=10000

#test1(N,dt,dz,timesteps)

"""Test 2"""

#test2(N,dt,dz,timesteps)

"""Test 3"""

test3(N,dt,dz,timesteps)


from functions import *
from plotting import *
from scipy.stats import norm

#%load_ext line_profiler

def test1(N,dt,dz,timesteps):
    K=np.linspace(1,10,N)

    #initialize C
    C1init=np.zeros(N)
    C1init.fill(1)
    print("Cinit",C1init)


    S=np.zeros((timesteps,N))

    C=runSimulation(C1init,dt,dz,K,0,timesteps,S)
    plotConcentrations(C,"test1")

def test2(N,dt,dz,timesteps):
    S=np.zeros((timesteps,N))
    x=np.linspace(1,N,N)
    K=np.full(N,1)
    Cinit=norm.pdf(x,N/2,N/5) #normal distribution
    C=runSimulation(Cinit,dt,dz,K,0,timesteps,S)
    massDiff,initMass=massDifference(C)
    print(np.sum(C[0]))
    #print(massDiff)
    plotMassDifference(massDiff,initMass)
    plotConcentrations(C,"test2C")

def test3(N,dt,dz,timesteps):
    S=np.zeros((timesteps,N))
    z=np.linspace(1,N,N)
    K=np.full(N,1)
    Cinit=norm.pdf(z,N/2,2*dz) #normal distribution, very thin
    C=runSimulation(Cinit,dt,dz,K,0,timesteps,S)
    plotConcentrations(C,"test3C")
    #print(C)
    sigmas=[]
    for Ci in C:
        #print(Ci)
        mu=np.sum(np.dot(Ci,z)*dz)/np.sum(Ci*dz)
        #print(mu)
        #print(Ci*((z-mu)@(z-mu)))
        sigmas.append(np.sum(Ci*((z-mu)**2)*dz)/(np.sum(Ci)*dz))
        
    #print(sigmas)
    plotSigma(sigmas,K)

def test4(N,dt,dz,timesteps,kw):
    Cinit=np.full(N,1) #init concentration const in space
    S=np.zeros((timesteps,N)) #??
    t=np.linspace(0,timesteps,timesteps)

    #constant diffusitivity
    Kconst=np.full(N,1000) 
    C=runSimulation(Cinit,dt,dz,Kconst,kw,timesteps,S)
    massesKconst=np.sum(C,axis=1) #gives array with the mass for each time

    #variable diffusitivity
    z=np.linspace(0,N,N)
    Kvar=np.sin((N/2)*z)+1000
    # plt.plot(z,Kvar)
    # plt.show()
    C=runSimulation(Cinit,dt,dz,Kvar,kw,timesteps,S)
    massesKvar=np.sum(C,axis=1) #gives array with the mass for each time

    plotMass(massesKconst,massesKvar,t,kw,N,dz)






"""PROFILING""" #funker ikke :(
#K=np.linspace(1,10,N)

# #initialize C
# C1init=np.zeros(N)
# C1init.fill(1)
# S=np.zeros((timesteps,N))

# #%lprun -f runSimulation x = runSimulation(C1init,dt,dz,K,kw,timesteps,S)



"""Test 1"""
N=100
kw=0
dt=1
dz=1
timesteps=1000

#test1(N,dt,dz,timesteps)

"""Test 2"""

#test2(N,dt,dz,timesteps)

"""Test 3"""

#test3(N,dt,dz,timesteps)

"""Test 4"""
kw=0.01
test4(N,dt,dz,timesteps,kw)

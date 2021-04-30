from functions import *
from plotting import *
from scipy.stats import norm

#%load_ext line_profiler

def test1(L,dt,dz,T):
    N=int(L/dz)
    timesteps=int(T/dt)
    K=np.linspace(1,10,N)

    #initialize C
    C1init=np.zeros(N)
    C1init.fill(1)

    S=np.zeros((timesteps,N))

    C=runSimulation(C1init,dt,dz,K,0,timesteps,S)
    plotConcentrations(C,"test1")

def test2(L,dt,dz,T):
    N=int(L/dz)
    timesteps=int(T/dt)
    S=np.zeros((timesteps,N))
    z=np.linspace(1,L,N)
    K=np.sin(z)*100+1000 #variable K
    Cinit=norm.pdf(z,L/2,L/5) #normal distribution
    C=runSimulation(Cinit,dt,dz,K,0,timesteps,S)
    massDiff,initMass=massDifference(C,dz)
    plotMassDifference(massDiff,initMass,T)
    plotConcentrations(C,"test2C")

def test3(L,dt,dz,T):
    N=int(L/dz)
    timesteps=int(T/dt)
    S=np.zeros((timesteps,N))
    z=np.linspace(0,L,N)
    K=np.full(N,1)
    print(K)
    Cinit=norm.pdf(z,L/2,2*dz) #normal distribution, very thin
    C=runSimulation(Cinit,dt,dz,K,0,timesteps,S)
    #plotConcentrations(C,"test3C")
    #print(C)
    sigmas=[]
    for Ci in C:
        mu=np.sum(np.dot(Ci,z)*dz)/np.sum(Ci*dz)
        sigmas.append(np.sum(Ci*((z-mu)**2)*dz)/(np.sum(Ci)*dz))
    plotSigma(sigmas,K,L,timesteps)


def test4(L,dt,dz,T,kw):
    N=int(L/dz)
    timesteps=int(T/dt)
    print(L)
    Cinit=np.full(N,1) #init concentration const in space
    S=np.zeros((timesteps,N)) 
    t=np.linspace(0,T,timesteps)

    #constant diffusitivity
    Kconst=np.full(N,10) 
    CKconst=runSimulation(Cinit,dt,dz,Kconst,kw,timesteps,S)
    massesKconst=np.sum(CKconst,axis=1) #gives array with the mass for each time

    #variable diffusitivity
    z=np.linspace(0,L,N)
    Kvar=np.sin((N/2)*z)+10
    CKvar=runSimulation(Cinit,dt,dz,Kvar,kw,timesteps,S)
    massesKvar=np.sum(CKvar,axis=1)*dz #gives array with the mass for each time
    print("C",len(CKvar))
    #plotConcentrations(CKvar,"funkerikke")
    #plt.matshow(CKvar.T)
    plotMass(massesKconst,massesKvar,t,kw,L)

def test5(N,dt,dz,T,kw,Ceq,K,Kstring):
    timesteps=int(T/dt)
    Cinit=np.zeros(N)
    S=makeS(N,timesteps,Ceq,kw,dz,dt,K)
    t=np.linspace(0,T,timesteps)
    
    C=runSimulation(Cinit,dt,dz,K,kw,timesteps,S)
    Cmin,Cmax=minAndMaxConcentrations(C)
    plotMinAndMaxConcentrations(t,Cmin,Cmax,Ceq,Kstring,"test5")




"""PROFILING""" 
#K=np.linspace(1,10,N)

# #initialize C
# C1init=np.zeros(N)
# C1init.fill(1)
# S=np.zeros((timesteps,N))

# #%lprun -f runSimulation x = runSimulation(C1init,dt,dz,K,kw,timesteps,S)



"""Test 1"""
L=30
dz=0.01
N=int(L/dz)

dt=0.1
T=2000
timesteps=int(T/dt)

kw=0

#test1(L,dt,dz,T)

"""Test 2"""
L=30
dz=0.01
N=int(L/dz)

dt=0.1
T=2000
timesteps=int(T/dt)

test2(L,dt,dz,T)

"""Test 3"""
L=30
dz=0.01
N=int(L/dz)

dt=0.1
T=200
timesteps=int(T/dt)

#test3(L,dt,dz,T)

"""Test 4"""
kw=0.0000697
kw=0.1
#test4(L,dt,dz,T,kw)

"""Test 5"""
#TESTING S
# N=5
# T=10
# dz=1
# dt=1
# timesteps=int(T/dt)
# t=np.linspace(0,T,timesteps)
# Ceq=np.sin(t)*10000
# C=np.zeros((N,N))
# S=makeS(N,timesteps,Ceq,kw,dz,dt,K)
# print(S)


# #Testing Cmin, Cmax
HpCO2=2.01

Kc=np.full(N,1)
z=np.linspace(0,N,N)
Kv=np.sin(2*z)+2
Ceq=np.full(timesteps,HpCO2)
kw=0.1

#test5(N,dt,dz,timesteps,kw,Ceq,Kc,"constant")
# test5(N,dt,dz,timesteps,kw,Ceq,Kv,"variable")



#testing stuff for making arrays same dimension
C=np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
Ctest=np.array([[1,3,5],[1,3,5],[1,3,5]])

x=np.round(np.linspace(0,len(C)-1,len(Ctest))).astype(int)
#print(x)
y=np.round(np.linspace(0,len(C[0])-1,len(Ctest[0]))).astype(int)
#print(y)
Csub=C[x,y]
print(Csub)

def makeArraysSameDim(A1,A2): #assume A1 is bigger than A2
    x=np.round(np.linspace(0,len(A1)-1,len(A2))).astype(int)
    y=np.round(np.linspace(0,len(A1)-1,len(A2))).astype(int)
    return A1[x,y] #returns subsampling of A1, with same dim as A2
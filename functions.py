import numpy as np
from numba import jit
import math


"""Thomas algorithm"""
@jit(nopython = True)
def tdma_solver(a,b,c,d): #from jupyter notebook on linear algebra https://github.com/nordam/ComputationalPhysics/blob/master/Notebooks/10%20-%20Linear%20Algebra.ipynb

    N=len(d)
    c_temp = np.zeros(N-1)
    d_temp = np.zeros(N)
    x  = np.zeros(N)

    #i=0
    c_temp[0] = c[0]/b[0]
    d_temp[0] = d[0]/b[0]

    #i=1 to i=N-2
    for i in range(1, N-1):
        q = (b[i] - a[i-1]*c_temp[i-1])
        c_temp[i] = c[i]/q
        d_temp[i] = (d[i] - a[i-1]*d_temp[i-1])/q

    #i=N-1
    d_temp[N-1] = (d[N-1] - a[N-2]*d_temp[N-2])/(b[N-1] - a[N-2]*c_temp[N-2])

    #Back substitution
    x[N-1] = d_temp[N-1]
    for i in range(N-2, -1, -1):
        x[i] = d_temp[i] - c_temp[i]*x[i+1]
    return x

def tdma(A,d):
    a=A.diagonal(-1)
    b=A.diagonal(0)
    c=A.diagonal(1)
    return tdma_solver(a,b,c,d)


"""Simulation"""

def makeLandR(N,dt,dz,K,kw): #K has length N, indeces (0,1,2,3,..,N-1)
    #some variables
    alpha=dt/(2*dz*dz)
    Gamma=2*alpha*kw*dz*(1-((-(3/2)*K[0]+2*K[1]-(1/2)*K[2])/(2*K[0])))
    

    #X is the difference between R and the identity matrix
    #R=I+X, L=I-X
    X=np.zeros((N,N))
    #first row
    X[0,0]=-2*alpha*K[0]-Gamma
    X[0,1]=2*alpha*K[0]
    #all rows except first and last
    for i in range(1,N-1):
        X[i,i-1]= -(alpha/4)*(K[i+1]-K[i-1])+alpha*K[i]
        X[i,i]=-2*alpha*K[i]
        X[i,i+1]=(alpha/4)*(K[i+1]-K[i-1])+alpha*K[i]
    #last row
    X[N-1,N-2]=2*alpha*K[N-1]
    X[N-1,N-1]=-2*alpha*K[N-1]
    
    L=np.identity(N)
    R=np.identity(N)
    R+=X
    L-=X
    return L,R

def makeS(N,timesteps,Ceq,kw,dz,dt,K): #Ceq(t) depends on time, K(z) depends on space
    S=np.zeros((timesteps,N))
    alpha=dt/(2*dz*dz)
    Gamma=2*alpha*kw*dz*(1-(-(3/2)*K[0]+2*K[1]-(1/2)*K[2])/(2*K[0]))
    S[:,0]=Ceq*2*Gamma 
    return S


def nextC(Ci,L,R,Si,Snext): #calculates C for the next time step
    V=R@Ci+0.5*(Si+Snext)
    return tdma(L,V) #using the tdma solver

def runSimulation(Cinit,dt,dz,K,kw,timesteps,S):
    #initialization
    N=len(Cinit)
    L,R=makeLandR(N,dt,dz,K,kw)
    C=np.zeros((timesteps,N))
    C[0]=Cinit

    #simulation loop
    for i in range(timesteps-1):
        C[i+1]=nextC(C[i],L,R,S[i],S[i+1])

        if ((i*100)%timesteps==0): #just to keep track of the time
            print(i*100/timesteps,"%")
    return C #C is a 2d array, the first index is the time, and the second is the spatial coordinate 
    #a vector of the sea columns for each time



"""Calculating stuff after simulation"""

def massDifference(C): #C is the array returned after simulation
    mass=np.sum(C,axis=1) 
    initMass=mass[0]
    return mass-initMass, initMass #returns difference between initial mass and current mass for all timesteps, and the initial mass

def minAndMaxConcentrations(C):#C is the array returned after simulation
    minC=np.amin(C,axis=1) #minimum value of each column of C
    maxC=np.amax(C,axis=1) #max value of each column of C
    return minC,maxC

def totalMass(C,L):
    masses=np.sum(C,axis=1)*12*360e12
    return masses

"""convergence test"""
def checkMaxError(C,Ctest):
    x=int(len(C)/len(Ctest))
    y=int(len(C[0])/len(Ctest[0]))
    print("x",x)
    print("lens",len(C),len(Ctest))
    Csub=C[::x,::y] #array with every yth row and xth column of C
    print(len(Csub))
    errors=np.abs(Csub-Ctest) #array with absolute value of the difference between each of the elements of C and Ctest
    return np.amax(errors) #return largest error

# def checkMaxErrorLastTimestep(C,Ctest):
#     y=int(len(C[0])/len(Ctest[0]))
#     i=np.round(np.linspace(0,len(C)-1,len(Ctest))).astype(int)
#     Cend=C[len(C)-1]
#     errors=np.abs(Cend[y]-Ctest[len(Ctest)-1])
#     return np.amax(errors)
    
def checkMaxErrorLastTimestep(C,Ctest):
    errors=np.abs(C[len(C)-1]-Ctest[len(Ctest)-1])
    return np.amax(errors)


def convergenceTest(C,CList): #C is an accurate simulation to be compared with
    errors=[]
    i=0
    for Ci in CList:
        print("dt no",i)
        print(len(Ci),len(C))
        errors.append(checkMaxError(C,Ci))
        i+=1
    return errors

def convergenceTestLastTimestep(C,CList): #C is an accurate simulation to be compared with
    errors=[]
    for Ci in CList:
        errors.append(checkMaxErrorLastTimestep(C,Ci))
    return errors
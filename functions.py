import numpy as np

#make L and R matrices

def makeLandR(N,dt,dz,K,kw): #K has length N, indeces (0,1,2,3,..,N-1)
    #some variables
    alpha=dt/(2*dz*dz)
    Gamma=2*alpha*kw*dz*(1-(-(3/2)*K[0]+2*K[1]-(1/2)*K[2])/2*K[0])
    

    #X is the difference between R and the identity matrix
    #R=I+X, L=I-X
    X=np.zeros((N,N))
    X[0,0]=-2*alpha*K[0]-Gamma
    X[0,1]=2*alpha*K[0]
    #all rows except first and last
    for i in range(1,N-1):
        #print(i)
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
    #print(L,R)
    return L,R

def nextC(Ci,L,R,Si,Snext):
    V=R@Ci+0.5*(Si+Snext)
    #print(Ci)
    #print(R,Ci,R@Ci)
    #print(np.linalg.solve(L,V))
    return np.linalg.solve(L,V)

def runSimulation(Cinit,dt,dz,K,kw,timesteps,S):
    N=len(Cinit)
    L,R=makeLandR(N,dt,dz,K,kw)
    #print(R)
    C=np.zeros((timesteps,N))
    C[0]=Cinit
    #print(C)
    for i in range(timesteps-1):
        #print(C[i])
        C[i+1]=nextC(C[i],L,R,S[i],S[i+1])
    return C
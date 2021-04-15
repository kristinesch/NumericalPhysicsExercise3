import numpy as np

#make L and R matrices

def makeLandR(N,dt,dz,K,kw):
    #some variables
    alpha=dt/(2*dz*dz)
    Gamma=2*alpha*kw*dz*(1-(-(3/2)*K[0]+2*K[1]-(1/2)*K[2])/2*K[0])
    
    #create array to fill
    R=np.zeros((N,N))
    #first row:
    R[0,0]=1-2*alpha*K[0]-Gamma
    R[0,1]=2*alpha*K[0]
    #all rows except first and last
    for i in range(1,N-2):
        print(i)
        R[i,i-1]= -(alpha/4)*(K[i+1]-K[i-1])+alpha*K[i]
        R[i,i]=1-2*alpha*K[i]
        R[i,i+1]=(alpha/4)*(K[i+1]-K[i-1])+alpha*K[i]
    #last row
    R[N-1,N-2]=2*alpha*K[N-1]
    R[N-1,N-1]=1-2*alpha*K[N-1]

    #L 
    L=-R #RIGHT????
    return L,R

def nextC(Ci,L,R,Si,Snext):
    V=np.dot(R,Ci)+0.5*(Si+Snext)
    return np.linalg.solve(L,V)

def runSimulation(Cinit,dt,dz,K,kw,timesteps,S):
    N=len(Cinit)
    L,R=makeLandR(N,dt,dz,K,kw)
    C=np.zeros((timesteps,N))
    C[0]=Cinit
    for i in range(1,timesteps):
        C[i+1]=nextC(C[i],L,R,S[i],S[i+1])
    return C
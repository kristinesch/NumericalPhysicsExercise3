from functions import *
from plotting import *
import numpy as np



kw=6.97e-5
day=86400 #1day in seconds
Ceq=5060*415e-6

#values used for dt convergence test: T=10*day, L=100, dz=0.1
#values used for dz convergence test: T=10*day, L=100, dt=100

T=10*day
L=100
dt=100
dz=0.1 
timesteps=int(T/dt)
t=np.linspace(0,T,timesteps)

def makeK(z,L): #K from eq 11 in problem text
    Larr=np.full(len(z),L)
    return 0.001+(0.02/7)*z*np.exp(-z/7)+(0.05/10)*(Larr-z)*np.exp(-(Larr-z)/10)


def shallowSim(T,L,dt,dz,kw,Ceq,npyFile): #simulation with parameters from problem 2
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

"""Convergence test for dt"""
#shallowSim(T,L,dt,dz,kw,Ceq,"dt"+str(dt)+".npy")

# Cdt1=np.load("dt1.npy")
#CList=[np.load("dt2.npy"),np.load("dt5.npy"),np.load("dt10.npy"),np.load("dt15.npy"),np.load("dt20.npy"),np.load("dt50.npy"),np.load("dt100.npy"),np.load("dt200.npy"),np.load("dt500.npy"),np.load("dt1000.npy")]
dtList=[2,5,10,15,20,50,100,200,500,1000]
# #errors=convergenceTest(Cdt1, CList)
# #np.save("convergenceErrors.npy",errors)
#errors=np.load("convergenceErrors.npy")
#convergencePlot(dtList, errors,"dt")
#print(errors)

#plotConcentrations(Cdt1, "2p2checkC")
dtListShort=[15,20,50,100,200,500,1000]

    
        
C_ref=np.load("dt1.npy")
print("ok")
#dtM1andRMSconvergence(C_ref, dtList, 0.1,L,T,2)


"""Convergence test for dz"""
# # dz=0.1
# # shallowSim(T,L,dt,dz,kw,Ceq,"dz"+str(dz)+".npy")

dzList=[0.02,0.05,0.1,0.2,0.5,1]
dzListShort=[0.5,1]
# # # for dzi in dzList:
# # #     print(dzi)
# # #     shallowSim(T,L,dt,dzi,kw,Ceq,"dz"+str(dzi)+".npy")

Cdz=np.load("dz0.01.npy")
# # CdzList=[np.load("dz0.02.npy"),np.load("dz0.05.npy"),np.load("dz0.1.npy"),np.load("dz0.2.npy"),np.load("dz0.5.npy"),np.load("dz1.npy")]
# # dzErrors=convergenceTest(Cdz,CdzList)
# # np.save("dzConvergenceErrors.npy",dzErrors)
# dzErrors=np.load("dzConvergenceErrors.npy")
# convergencePlot(dzList, dzErrors,"dz")
# print(dzErrors)

dzM1andRMSconvergence(Cdz, dzList, dz, L, T, 2)


"""180 days simulation"""
T=180*day
L=100
dt=15
dz=0.1
timesteps=int(T/dt)
t=np.linspace(0,T,timesteps)

#shallowSim(T, L, dt, dz, kw, Ceq, "C180daySimulation.npy")
C=np.load("C180daySimulation.npy")
#print("maximum value in C: ",np.amax(C))

#PLOTTING
#Cmin,Cmax=minAndMaxConcentrations(C)
#plotMinAndMaxConcentrations(t, Cmin, Cmax, Ceq, "variable", "P2minMaxC",test5=False)
#plotConcentrationFor4times(C, "P2C(z)",L)

"""plotting K"""
# def plotK(L,dz): #plotting K as described in problem 2
#     N=int(L/dz)
#     z=np.linspace(0,L,N)
#     K=makeK(z, L)
#     fig,ax=plt.subplots(1,1)
#     ax.plot(z,K)
#     ax.set_xlabel("x")
#     ax.set_ylabel("K")
#     fig.savefig("P2K")
#     plt.show()
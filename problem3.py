import numpy as numpy
from functions import *
from plotting import *

kw=6.97e-5
day=86400 #1day in seconds
year=365*day #1 year in seconds
H=5060
pCO2init=415e-6


L=4000
T=365*day
dz=1
dt=100
N=int(L/dz)
timesteps=int(T/dt)



def makeK3(z): #K from eq 12 in problem text
    K1=0.01
    K0=0.0001
    a=0.5
    z0=np.full(len(z),100)
    return K1+((K0-K1)/(1+np.exp(-a*(z-z0))))

def deepSim(T,L,dt,dz,kw,npyFile): #simulation with parameters from problem 3
    N=int(L/dz)
    timesteps=int(T/dt)
    z=np.linspace(0,L,N)
    t=np.linspace(0,T,timesteps)
    K=makeK3(z) 
    Cinit=np.full(N,H*pCO2init) #constant equilibrium concentration at beginning
    Ceqs=H*(pCO2init+2.3e-6*t/year) #Equilibrium concentration as functon of time, values from problem text
    S=makeS(N, timesteps, Ceqs, kw, dz, dt, K)
    C=runSimulation(Cinit, dt, dz, K, kw, timesteps, S)
    np.save(npyFile,C) #saving the data

"""plotting K(z)"""
# z=np.linspace(0,L,N)
# K=makeK3(z)
# plt.plot(z,K)
# plt.show()

"""Convergence test"""

# #Parameters used for dt: T=1*year, L=4000, dz=0.2
dt=1000
T=1*year
dz=0.2
# #deepSim(T,L,dt,dz,kw,"C3dt"+str(dt)+"dz"+str(dz)+".npy")
# dtList=[5000,10000,50000,100000,500000,1000000,5000000,10000000]
# for dti in dtList:
#     deepSim(T,L,dti,dz,kw,"C3dt"+str(dti)+"dz"+str(dz)+".npy")


# C3dt1000dz02=np.load("C3dt1000dz0.2.npy")
# #plotConcentrationFor4times(C3dt1000dz02, "P3test", L)


# CdtList=[]
# for dti in dtList:
#     CdtList.append(np.load("C3dt"+str(dti)+"dz"+str(dz)+".npy"))
# dtErrors=convergenceTestLastTimestep(C3dt1000dz02, CdtList)
# np.save("ConvergenceP3dt.npy",dtErrors)
# print(dtErrors)
# convergencePlot(dtList, dtErrors, "dt")



def runConvergenceSimulations(d,dList): #d is a string: dt or dz
    if d=="dz":
        for dzi in dList:
            deepSim(T,L,dt,dzi,kw,"C3dt"+str(dt)+"dz"+str(dzi)+".npy")
    elif d=="dt":
        for dti in dList:
            deepSim(T,L,dti,dz,kw,"C3dt"+str(dti)+"dz"+str(dz)+".npy")

def calculateConvergenceTestErrors(d, dList,accurateCnpy,allTimes=True):
    CList=[]
    if d=="dz":
        for dzi in dList:
            CList.append(np.load("C3dt"+str(dt)+"dz"+str(dzi)+".npy"))
    elif d=="dt":
        for dti in dList:
            print(dti)
            CList.append(np.load("C3dt"+str(dti)+"dz"+str(dz)+".npy"))
    accurateC=np.load(accurateCnpy)
    if allTimes:
        dErrors=convergenceTest(accurateC, CList)
    else:
        dErrors=convergenceTestLastTimestep(accurateC, CList)
    np.save("ConvergenceP3"+d+".npy",dErrors)
    print("Errors:",dErrors)
    convergencePlot(dList, dErrors, d)

dtList=[10000,50000,100000,500000,1000000,5000000,10000000]
#runConvergenceSimulations("dt", dtList)
calculateConvergenceTestErrors("dt", dtList, "C3dt1000dz0.2.npy",allTimes=False)




#dzList=[0.4,0.8,1.6,4,16,40,100,400,1000]
#runConvergenceSimulations("dz", dzList)
#calculateConvergenceTestErrors("dz", dzList, "C3dt1000dz0.2.npy")

"""Full 10 year simulation"""



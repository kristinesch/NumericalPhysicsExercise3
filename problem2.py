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



"""Convergence test for dt"""
#shallowSim(T,L,dt,dz,kw,Ceq,"dt"+str(dt)+".npy")

# Cdt1=np.load("dt1.npy")
# #CList=[np.load("dt2.npy"),np.load("dt5.npy"),np.load("dt10.npy"),np.load("dt15.npy"),np.load("dt20.npy"),np.load("dt50.npy"),np.load("dt100.npy"),np.load("dt200.npy"),np.load("dt500.npy"),np.load("dt1000.npy")]
dtList=[2,5,10,15,20,50,100,200,500,1000]
# #errors=convergenceTest(Cdt1, CList)
# #np.save("convergenceErrors.npy",errors)
errors=np.load("convergenceErrors.npy")
convergencePlot(dtList, errors,"dt")
print(errors)

#plotConcentrations(Cdt1, "2p2checkC")


"""Convergence test for dz"""
# dz=0.1
# shallowSim(T,L,dt,dz,kw,Ceq,"dz"+str(dz)+".npy")

dzList=[0.02,0.05,0.1,0.2,0.5,1]
# # for dzi in dzList:
# #     print(dzi)
# #     shallowSim(T,L,dt,dzi,kw,Ceq,"dz"+str(dzi)+".npy")

# Cdz=np.load("dz0.01.npy")
# CdzList=[np.load("dz0.02.npy"),np.load("dz0.05.npy"),np.load("dz0.1.npy"),np.load("dz0.2.npy"),np.load("dz0.5.npy"),np.load("dz1.npy")]
# dzErrors=convergenceTest(Cdz,CdzList)
# np.save("dzConvergenceErrors.npy",dzErrors)
dzErrors=np.load("dzConvergenceErrors.npy")
convergencePlot(dzList, dzErrors,"dz")
print(dzErrors)


"""180 days simulation"""
T=180*day
L=100
dt=15
dz=0.1
timesteps=int(T/dt)
t=np.linspace(0,T,timesteps)

shallowSim(T, L, dt, dz, kw, Ceq, "C180daySimulation.npy")
C=np.load("C180daySimulation.npy")
print("maximum value in C: ",np.amax(C))
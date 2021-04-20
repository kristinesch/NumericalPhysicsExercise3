from matplotlib import pyplot as plt 
import numpy as np

def plotConcentrations(Ci,plotFile):
    fig,ax=plt.subplots(2,1)
    T=len(Ci)
    N=len(Ci[0])
    z=np.linspace(0,N,N)

    #ax[0].set_ylim(0,2)
    ax[0].plot(z,Ci[0])
    ax[0].set_title("Initial concentration")
    ax[0].set_ylabel("Concentration")
    ax[0].set_ylim(0.9,1.1)

    #ax[1].set_ylim(0,2)
    ax[1].plot(z,Ci[T-1])
    ax[1].set_title("Final concentration")
    ax[1].set_xlabel("z")
    ax[1].set_ylabel("Concentration")
    ax[1].set_ylim(0.9,1.1)
    fig.tight_layout()
    fig.savefig(plotFile)
    plt.show()

def plotMassDifference(massDiff,initMass,T):
    fig, ax=plt.subplots(1,1)
    initMassString="{:.2f}".format(initMass)
    timesteps=len(massDiff)
    t=np.linspace(0,T,timesteps)
    ax.plot(t,massDiff)
    ax.set_xlabel("Time")
    ax.set_ylabel("Difference from initial mass ("+initMassString+")")
    fig.savefig("test2")

    plt.show()

def plotSigma(sigmas,K,L,timesteps):
    N=len(K)
    T=len(sigmas)
    t=np.linspace(0,T,timesteps)
    #upper limit, the variance should go towards this value
    uniformSigma=(L*L)/12
    uniformSigmaList=np.full(timesteps,uniformSigma)
    #theoretical change of sigma at begining
    theorySigma=2*K[0]*t+sigmas[0]

#Plotting
    fig, ax=plt.subplots(1,1)
    ax.plot(t,sigmas,label="Variance from simulation")
    ax.plot(t,theorySigma,label="Linear increase of variance")
    ax.plot(t,uniformSigmaList,label="uniform distribution variance")
    ax.set_ylim(0,uniformSigma*1.2) #axis stop a little bit over the plot
    fig.suptitle("Variance of distribution for "+str(N)+" spatial points")
    ax.set_xlabel("Time")
    ax.set_ylabel("Variance")
    fig.legend(loc="center")
    fig.savefig("test3")
    #fig.tight_layout()
    plt.show()

def plotMass(massesKconst,massesKvar, time,kw,L):
    M0=massesKconst[0] #denne er lik for begge right?
    M=M0*np.exp(-time*(kw/L))

    fig, ax= plt.subplots(2,1,sharex=True)
    ax[0].plot(time,massesKconst,label="Simulation data",color="red")
    ax[0].plot(time,M,label="Theoretical decay",linestyle="--", color="lightskyblue")
    ax[0].set_title("Constant diffusitivity")

    ax[1].plot(time,massesKvar,color="red")
    ax[1].plot(time,M,linestyle="--", color="lightskyblue")
    ax[1].set_title("Variable diffusitivity")

    fig.legend(loc="center right")
    ax[1].set_xlabel("Time")
    ax[0].set_ylabel("Mass")
    ax[1].set_ylabel("Mass")
    fig.tight_layout()
    #fig.suptitle("Total mass as a function of time")
    fig.savefig("test4")
    plt.show()

def plotMinAndMaxConcentrations(time, Cmin,Cmax,Ceq,varOrConst):
    fig, ax=plt.subplots(1,1)
    Ceqs=np.full(len(time),Ceq)
    ax.plot(time,Cmin,label="Minimum concentration")
    ax.plot(time,Cmax,label="Maximum concentration")
    ax.plot(time,Ceqs,label="Equilibrium concentration")
    ax.set_xlabel("Time")
    ax.set_ylabel("Concentration")
    fig.legend(loc="center")
    fig.suptitle("Minimum and maximum concentrations as function of time")
    ax.set_title("for "+varOrConst+" diffusivity")
    fig.savefig("test5"+varOrConst)
    plt.show()

def plotConcentration(C,plotFile):
    fig,ax=plt.subplots(1,1)
    T=len(C)
    N=len(C[0])
    z=np.linspace(0,N,N)

    ax.plot(z,C[0])
    ax.set_title("Concentration as function of depth")
    ax.set_ylabel("Concentration")
    ax.set_xlabel(z)
    ax.set_ylim(0.9,1.1)

    fig.tight_layout()
    fig.savefig(plotFile)
    plt.show()
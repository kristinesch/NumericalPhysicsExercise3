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

    #ax[1].set_ylim(0,2)
    ax[1].plot(z,Ci[T-1])
    ax[1].set_title("Final concentration")
    ax[1].set_xlabel("z")
    ax[1].set_ylabel("Concentration")
    fig.tight_layout()
    fig.savefig(plotFile)
    plt.show()

def plotMassDifference(massDiff):
    fig, ax=plt.subplots(1,1)
    T=len(massDiff)
    t=np.linspace(0,T,T)
    ax.plot(t,massDiff)
    ax.set_xlabel("t")
    ax.set_ylabel("Difference from initial mass")
    fig.savefig("test2")

    plt.show()

def plotSigma(sigmas,K):
    N=len(K)
    T=len(sigmas)
    t=np.linspace(0,T,T)
    #upper limit, the variance should go towards this value
    uniformSigma=(N*N)/12
    uniformSigmaList=np.full(T,uniformSigma)
    #theoretical change of sigma at begining
    theorySigma=2*K[0]*t+sigmas[0]

#Plotting
    fig, ax=plt.subplots(1,1)
    ax.plot(t,sigmas,label="Variance from simulation")
    ax.plot(t,theorySigma,label="Linear increase of variance")
    ax.plot(t,uniformSigmaList,label="uniform distribution variance")
    ax.set_ylim(0,uniformSigma*1.2) #axis stop a little bit over the plot
    fig.suptitle("Variance of distribution for "+str(N)+" particles")
    ax.set_xlabel("time")
    ax.set_ylabel("Variance")
    fig.savefig("test3")
    plt.show()
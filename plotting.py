from matplotlib import pyplot as plt 
import numpy as np

def plotConcentrations(CiFile,plotFile):
    Ci=np.load(CiFile)
    fig,ax=plt.subplots(2,1)
    N=len(Ci[0])
    z=np.linspace(0,N,N)

    ax[0].set_ylim(0,2)
    ax[0].plot(z,Ci[0])
    ax[0].set_title("Initial concentration")
    ax[0].set_ylabel("Concentration")

    ax[1].set_ylim(0,2)
    ax[1].plot(z,Ci[N-1])
    ax[1].set_title("Final concentration")
    ax[1].set_xlabel("z")
    ax[1].set_ylabel("Concentration")
    fig.tight_layout()
    fig.savefig(plotFile)
    plt.show()

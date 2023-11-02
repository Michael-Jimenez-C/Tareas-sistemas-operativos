import matplotlib.pyplot as plt
import numpy as np

def GANT(historicos):
    Y=[i for i in historicos]
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.grid()
    ax.xaxis.tick_top()
    ax.set_yticks(-np.array(range(len(Y))),Y)
    maximo=0
    for i,j in enumerate(Y):
        maximo=np.maximum(maximo,historicos[j][-1])
        ax.scatter(historicos[j][0],[-i],marker='>',color='gray')
        ax.scatter([historicos[j][1:],np.array(historicos[j][1:])-1],[[-i]*len(historicos[j][1:]),[-i]*len(historicos[j][1:])],marker='s')
        ax.set_xticks(range(0,maximo+1,maximo//10+1))
    return fig,ax


if __name__=='__main__':
    GANT({'a':[1],'b':[2,3,4,5,6,7]})


##Hacer que muestre por separado los tiempos de espera, y de comienzo
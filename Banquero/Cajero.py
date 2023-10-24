from Politicas import *
from Graficador import *
class Cajero:

    def __init__(self) -> None:
        self.clientes = []
        self.clientes.append(self.clientes)
        self.bloqueados = []
        self.t=0
        self.historico={}
    
    def append(self,obj:dict) -> list:
        self.clientes.insert(-1,obj)
        if obj['Nombre'] not in self.historico:
            self.historico[obj['Nombre']]=[self.t]
        return self.clientes

    def atender(self,c=False) -> list:
        #self.t+=1
        a=prioridad(self,c)
        return a
    
    def bloqu(self):
        procbloq(self)
    
    def diagram(self):
        return GANT(self.historico)
    
    def GenTab(self):
        tab=[]
        for i in self.historico:
            t0=self.historico[i][0]
            t=self.historico[i][1:]
            #tabla: proceso| tiempo de llegada | rafaga | t inicio | t final | t retorno | t espera
            tab.append([i,t0,len(t), (t[0] if len(t)>0 else 'None'), (t[-1] if len(t)>0 else 'None'), (t[-1]-t0 if len(t)>0 else 'None'),(t[-1]-len(t) if len(t)>0 else 'None')])
        return tab
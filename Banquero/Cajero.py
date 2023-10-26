from Politicas import procbloq,prioridad
from Graficador import GANT
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
            
            tab.append([i, #Proceso
                        t0, #Tiempo de llegada
                        len(t), #Rafaga
                        (t[0]-1 if len(t)>0 else 'None'), #T inicio
                        (t[-1] if len(t)>0 else 'None'), # T final
                        (t[-1]-t0 if len(t)>0 else 'None'), #T retorno
                        (t[-1]-len(t) if len(t)>0 else 'None') # T espera
                        ])
        return tab
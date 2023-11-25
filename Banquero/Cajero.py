from Politicas import noexpulsiva_con_bloqueo, procbloq,prioridad, round_robins, srtt
from Graficador import GANT
from TablaProcesos import Tabla
from Contador import Contador


algoritmos={None:srtt,
            'srtt': srtt,
            'rr': round_robins,
            'prioridad': prioridad}

class Cajero:
    def __init__(self, politica=None) -> None:
        self.clientes = []
        self.clientes.append(self.clientes)
        self.bloqueados = []
        self.t=Contador.get()
        self.historico={}
        self.tabla=[]
        self.politica=politica

    def append(self,obj:dict) -> list:
        self.clientes.insert(-1,obj)
        if obj['Nombre'] not in self.historico:
            self.historico[obj['Nombre']]=[self.t.t]
        return self.clientes

    def atender(self,c=False) -> list:
        global algoritmos
        a=algoritmos[self.politica](self,c)
        return a
    
    def bloqu(self):
        procbloq(self)
    
    def diagram(self):
        return GANT(self.historico)
    '''
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
    '''
    def GenTab(self):
        return Tabla.get()
        
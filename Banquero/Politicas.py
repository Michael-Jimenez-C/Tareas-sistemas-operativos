import numpy as np
from TablaProcesos import Tabla

prev_bloq=False

def expulsiva(self,c=False):
    if self.clientes[0] != self.clientes:
        cliente=self.clientes.pop(0)
        cliente['Solicitudes']=int(cliente['Solicitudes'])
        if cliente['Solicitudes']>5:
            cliente['Solicitudes']-=5
            self.append(cliente)
    return self.clientes


#def noexpulsiva(self,c=False):
#    if self.clientes[0] != self.clientes:
#        cliente=self.clientes.pop(0)
#        cliente['Solicitudes']=int(cliente['Solicitudes'])
#    return self.clientes, cliente['Solicitudes']

def noexpulsiva(self,c=False):    
    self.clientes[0]['Solicitudes']=int(self.clientes[0]['Solicitudes'])-1
    if self.clientes[0]['Solicitudes']==0:
        self.clientes.pop(0)
    return self.clientes

def noexpulsiva_con_bloqueo(self,c=False):
    global prev_bloq
    if(np.random.rand()<.90):
        Tabla.add(self)
        self.clientes[0]['Solicitudes']=int(self.clientes[0]['Solicitudes'])-1
        self.historico[self.clientes[0]['Nombre']].append(self.t)
        prev_bloq=False
    else:
        self.bloqueados.append(self.clientes.pop(0))
        if len(Tabla.tabla[-1])!=0:
            Tabla.tabla.append([])
        if not prev_bloq:
            self.t-=1
            prev_bloq=True
        return self.clientes
    if self.clientes[0]['Solicitudes']==0:
        self.clientes.pop(0)
    return self.clientes

def prioridad(self,c=False):
    for i in range(1,len(self.clientes)-1):
        for j in range(i+1,len(self.clientes)-1):
            if int(self.clientes[i]['Prioridad'])>int(self.clientes[j]['Prioridad']):
                temp=self.clientes[i]
                self.clientes[i]=self.clientes[j]
                self.clientes[j]=temp
    return noexpulsiva_con_bloqueo(self,c)

#####
def procbloq(self):
    if len(self.bloqueados)>0:
        if (np.random.rand()>.85):
            self.append(self.bloqueados.pop(0))
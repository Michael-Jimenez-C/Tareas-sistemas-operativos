import numpy as np

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
        cliente=self.clientes.pop(0)
    return self.clientes
'''
def noexpulsiva_con_bloqueo(self,c=False):
    if self.clientes[0] != self.clientes:
        cliente=self.clientes.pop(0)
        cliente['Solicitudes']=int(cliente['Solicitudes'])
        if np.random.rand()>.8:
            cliente['Solicitudes']-=np.random.randint(0,cliente['Solicitudes']//2+1)
            self.bloqueados.append(cliente)
    if len(self.bloqueados)!=0:
        if np.random.rand()>.8:
            self.append(self.bloqueados.pop(0))

    return self.clientes, cliente['Solicitudes']
'''

def noexpulsiva_con_bloqueo(self,c=False):
    if(np.random.rand()<.90):
        self.clientes[0]['Solicitudes']=int(self.clientes[0]['Solicitudes'])-1
        self.historico[self.clientes[0]['Nombre']].append(self.t)
    else:
        self.bloqueados.append(self.clientes.pop(0))
        return self.clientes
    if self.clientes[0]['Solicitudes']==0:
        self.clientes.pop(0)
    return self.clientes


def procbloq(self):
    if len(self.bloqueados)>0:
        if (np.random.rand()>.85):
            self.append(self.bloqueados.pop(0))
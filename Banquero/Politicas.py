import numpy as np
from TablaProcesos import Tabla

prev_bloq=False
probabilidad_bloqueo=0
probabilidad_desbloqueo=0
cuantum=4
contador_cuantum=0
prev_process=None

bloqueados_t=[]

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
    global probabilidad_bloqueo
    global contador_cuantum
    global prev_process
    global bloqueados_t
    if prev_process!=self.clientes[0]['Nombre']:
        prev_process=self.clientes[0]['Nombre']
        contador_cuantum=0
    if(np.random.rand()<=(1-probabilidad_bloqueo)):
        Tabla.add(self)
        self.clientes[0]['Solicitudes']=int(self.clientes[0]['Solicitudes'])-1
        self.historico[self.clientes[0]['Nombre']].append(self.t.t)
        prev_bloq=False
        contador_cuantum+=1
    else:
        contador_cuantum=0
        #self.bloqueados.append(self.clientes.pop(0))
        bloqueados_t.append(self.clientes.pop(0))
        if len(Tabla.tabla[-1])!=0:
            Tabla.tabla.append([])
        if not prev_bloq:
            self.t-=1
            prev_bloq=True
        return self.clientes
    if self.clientes[0]['Solicitudes']==0:
        self.clientes.pop(0)
        contador_cuantum=0
    return self.clientes

def prioridad(self,c=False):
    for i in range(1,len(self.clientes)-1):
        for j in range(i+1,len(self.clientes)-1):
            if int(self.clientes[i]['Prioridad'])>int(self.clientes[j]['Prioridad']):
                temp=self.clientes[i]
                self.clientes[i]=self.clientes[j]
                self.clientes[j]=temp
    return noexpulsiva_con_bloqueo(self,c)

def round_robins(self,c):
    global cuantum
    global contador_cuantum
    global prev_process
    if contador_cuantum>=cuantum:
        contador_cuantum=0
        client=self.clientes.pop(0)
        self.append(client)
        if len(Tabla.tabla[-1])!=0:
            Tabla.tabla.append([])
    return noexpulsiva_con_bloqueo(self,c)

def srtt(self,c):
    for i in range(0,len(self.clientes)-1):
        for j in range(i+1,len(self.clientes)-1):
            if int(self.clientes[i]['Solicitudes'])>int(self.clientes[j]['Solicitudes']):
                temp=self.clientes[i]
                self.clientes[i]=self.clientes[j]
                self.clientes[j]=temp
    return noexpulsiva_con_bloqueo(self,c)

#####
def procbloq(self):
    global probabilidad_desbloqueo
    if len(self.bloqueados)>0:
        if (np.random.rand()<probabilidad_desbloqueo):
            self.append(self.bloqueados.pop(0))

def global_desbloq(self):#este self es una cola
    global bloqueados_t
    global probabilidad_desbloqueo
    if len(bloqueados_t)>0:
        if (np.random.rand()<probabilidad_desbloqueo):
            self.append(self.bloqueados.pop(0))
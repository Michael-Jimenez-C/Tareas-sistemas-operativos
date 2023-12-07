import numpy as np
class Tabla:
    tabla=[[]]
    global_const={}
    def get():
        if Tabla.tabla is None:
            Tabla.tabla = [[]]
        return Tabla.tabla
    def add(caj):
        if caj.clientes[0]['Nombre'] not in Tabla.global_const:
            Tabla.global_const[caj.clientes[0]['Nombre']]=caj.clientes[0]['Solicitudes']
        if len(Tabla.tabla[-1])==0:
            index=caj.clientes[0]['Nombre']
            t0=caj.historico[index][0]
            Tabla.tabla[-1]=[index, #Proceso
                        t0, #Tiempo de llegada
                        int(Tabla.global_const[index])-len(caj.historico[index][1:]), #Rafaga
                        caj.t.t-1, #T inicio
                        caj.t.t, # T final
                        caj.t.t, #T retorno
                        caj.t.t,# T espera
                        caj.clientes[0]['Prioridad']]
        elif (Tabla.tabla[-1][0]!=caj.clientes[0]['Nombre']):
            Tabla.tabla.append([])
            return Tabla.add(caj)
        else:
            index=caj.clientes[0]['Nombre']
            t=caj.historico[index][1:]
            Tabla.tabla[-1][4]=caj.t.t
            Tabla.tabla[-1][5]=caj.t.t-Tabla.tabla[-1][1]
            Tabla.tabla[-1][6]=np.maximum(0,Tabla.tabla[-1][5]-len(t)-1)
    def count(index):
        a,b=np.unique(np.array(Tabla.tabla)[0,:],return_counts=True)
        return b[a==index]
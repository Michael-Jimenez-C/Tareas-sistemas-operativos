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
                        caj.t-1, #T inicio
                        caj.t, # T final
                        caj.t, #T retorno
                        caj.t# T espera
                        ]
        elif (Tabla.tabla[-1][0]!=caj.clientes[0]['Nombre']):
            Tabla.tabla.append([])
            return Tabla.add(caj)
        else:
            index=caj.clientes[0]['Nombre']
            t=caj.historico[index][1:]
            Tabla.tabla[-1][4]=caj.t
            Tabla.tabla[-1][5]=caj.t-Tabla.tabla[-1][1]
            Tabla.tabla[-1][6]=Tabla.tabla[-1][5]-len(t)-1
from Cajero import Cajero
from Politicas import global_desbloq
from Contador import Contador
from Politicas import vejez
class Cola_prioridad:
    def __init__(self) -> None:
        self.colas={1:Cajero('rr'),
               2:Cajero('srtt'),
               3:Cajero('prioridad')}
        self.t=Contador.get()

    def append(self, obj:dict) -> None:
        if int(obj['Lista']) not in self.colas:
            obj['Lista']=3
        self.colas[int(obj['Lista'])].append(obj)
    
    def atender(self) ->None:
        for i in self.colas:
            if len(self.colas[i].clientes)>1:    
                self.colas[i].atender()
                break
        for i in self.colas:
            if len(self.colas[i].clientes)>1:
                if 'ol' not in self.colas[i].clientes[0]:
                    self.colas[i].clientes[0]['ol']=self.colas[i].clientes[0]['Lista']
                if self.colas[i].clientes[0]['ol'] != self.colas[i].clientes[0]['Lista']:
                    a=self.colas[i].clientes.pop(0)
                    self.append(a)
    
    def bloqueados(self) -> None:
        global_desbloq(self)
    
    def proceso_actual(self) -> str:
        for i in self.colas:
            if len(self.colas[i].clientes)>1:
                return self.colas[i].clientes[0]['Nombre']
        return None
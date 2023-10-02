class Cajero:

    def __init__(self) -> None:
        self.clientes = []
        self.clientes.append(self.clientes)
    
    def append(self,obj:dict) -> list:
        self.clientes.insert(-1,obj)
        return self.clientes

    def atender(self) -> list:
        if self.clientes[0] != self.clientes:
            cliente=self.clientes.pop(0)
            cliente['Solicitudes']=int(cliente['Solicitudes'])
            if cliente['Solicitudes']>5:
                cliente['Solicitudes']-=5
                self.append(cliente)
            else:
                del cliente
        return self.clientes
    
if __name__=='__main__':#Esto solo se ejecuta si es la ejecucion principal
    cajero=Cajero()
    cajero.append({"nombre":"a","solicitudes":20})
    cajero.append({"nombre":"b","solicitudes":2})
    cajero.append({"nombre":"c","solicitudes":4})
    cajero.append({"nombre":"d","solicitudes":5})
    cajero.append({"nombre":"e","solicitudes":7})
    print(cajero.atender())
    cajero.append({"nombre":"f","solicitudes":8})
    cajero.append({"nombre":"g","solicitudes":10})
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
    print(cajero.atender())
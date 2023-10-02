class INodo:
    pass

class Nodo(INodo):

    def __init__(self, obj:any) -> None:
        self.obj = obj
        self.next = self
        self.main=self

    def __repr__(self) -> str:
        return str(self.obj)

    def list(self, start:INodo = None) -> list:
        if start != self:
            if start == None:
                start = self
            return [self] + self.next.list(start = start)
        return []
    
    def add(self,other:INodo) -> None:
        self.next=other
        other.next=self.main
        other.main=self.main

    def pop(self) -> INodo:
        pass

a=Nodo("A")
q=Nodo("q")
a.add(q)

print(a.list())
class Contador:
    contador=None
    def __init__(self):
        self.t=0
    def get():
        if Contador.contador is None:
            Contador.contador = Contador()
        return Contador.contador
    
    def next(self):
        self.t+=1
        return self
    
    def back(self):
        self.t-=1
        return self

    def __add__(self, num):
        self.t+=num
        return self
    
    def __subs__(self,num):
        self.t-=num
        return self
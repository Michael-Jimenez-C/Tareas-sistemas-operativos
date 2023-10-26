import tkinter as tk
from tkinter import ttk
class Tabla:
    def __init__(self,master,titulo,width,height,bg='white',fg='black'):
        self.master=master
        self.ctabla=tk.Frame(self.master,width=width,height=height)
        tk.Label(self.ctabla,text=titulo,bg=bg,fg=fg).place(x=0,y=0,width=width,height=30)
        self.tabla=tk.Listbox(self.ctabla)
        self.tabla.place(x=0,y=30,width=width-20,height=height-30)
        scrollbar = ttk.Scrollbar(master=self.ctabla,orient=tk.VERTICAL,command=self.tabla.yview)
        scrollbar.place(x=width-20,y=0,width=20,height=height)
        self.cabezera=None

    def place(self,x,y):
        self.ctabla.place(x=x, y=y)
    
    def getTab(self):
        return self.tabla
    
    def actualizar(self,datos,espaciado):
        self.tabla.delete(0, tk.END)
        cab=[i[:3] for i in (datos[0] if len(datos)>0 else [''])]
        self.tabla.insert(tk.END,self.__convcad(cab,espaciado))
        for i in datos:
            aux=[i[j] for j in i]
            cad=self.__convcad(aux,espaciado)
            self.tabla.insert(tk.END,cad)
    
    def __convcad(self,lst,esp):
        cad=''
        for i in lst:
            cad+=str(i).ljust(esp,' ')
        return cad
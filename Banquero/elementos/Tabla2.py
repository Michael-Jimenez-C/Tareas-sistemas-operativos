import tkinter as tk
from tkinter import ttk

class Tabla2:
    def __init__(self,master,titulo,width,height,bg='white',fg='black'):
        self.master=master
        self.ctabla=tk.Frame(self.master,width=width,height=height)
        tk.Label(self.ctabla,text=titulo,bg=bg,fg=fg).place(x=0,y=0,width=width,height=30)
        self.tabla=ttk.Treeview(self.ctabla)
        self.tabla.place(x=0,y=30,width=width-20,height=height-30)
        scrollbar = ttk.Scrollbar(master=self.ctabla,orient=tk.VERTICAL,command=self.tabla.yview)
        scrollbar.place(x=width-20,y=0,width=20,height=height)
        self.cabezera=None

    def place(self,x,y):
        self.ctabla.place(x=x, y=y)
    
    def getTab(self):
        return self.tabla
    def setHeaders(self,headers):
        self.tabla.column("#0",width=0,anchor=tk.CENTER)
        self.tabla.config(columns=headers)
        for i in headers:
            self.tabla.heading(i,text=i,anchor=tk.CENTER)
            self.tabla.column(i,width=20,anchor=tk.CENTER)
        
    def actualizar(self,datos):
        self.tabla.delete(*self.tabla.get_children())
        for i in datos:
            if i is not []:
                self.tabla.insert("",tk.END,values=i)
    
    def actualizar2(self,datos):
        self.tabla.delete(*self.tabla.get_children())
        for i in datos:
            self.tabla.insert("",tk.END,values=(i['Nombre'],i['Solicitudes'],i['Prioridad']))
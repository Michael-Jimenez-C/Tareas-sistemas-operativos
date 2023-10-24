import tkinter as tk
from tkinter import ttk
from Cajero import Cajero
import time
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GUI(tk.Frame):
    def __init__(self, cajero, master=None) -> tk.Frame:
        self.colores={
            "bg": "#fff",
            "c1": "#b01e20",
            "c2": "#460c0d",
            "c3": "#dfa5a6"
            }
        tk.Frame.__init__(self, master)
        self.cajero=cajero
        self.createWidgets()
        for i in range(15):
            c=self.cajero.append({'Nombre': f"a{chr(i+96)}",'Solicitudes':np.random.randint(1,3)})
        self.actualizartabla(c,self.cajero.bloqueados)
        self.cajero.t+=1
        self.master.after(1000, self.ciclo)

    def createWidgets(self) -> None:
        self.master.geometry('1100x700')
        self.master.resizable(width=False , height=False)
        self.master.config(bg=self.colores['bg'])
        client=tk.Frame(self.master,width=260,height=120)
        client.place(x=20,y=20)
        cuali=['Nombre','Solicitudes','prioridad']
        dif=90//len(cuali)
        
        cliente_form={}

        for j,i in enumerate(cuali):
            tk.Label(client,text=i,bg=self.colores['c3'],fg=self.colores['c1']).place(x=0,y=dif*j,width=70,height=dif)
            cliente_form[i]=tk.Entry(client)
            cliente_form[i].place(x=70,y=dif*j,width=190,height=dif)
        
        boton=tk.Button(client,text="ACEPTAR",bg=self.colores['c2'],fg=self.colores['bg'],command=lambda:  self.agregarCliente(cliente_form))
        boton.place(x=0,y=90,width=260,height=30)

        ctabla=tk.Frame(self.master,width=260,height=210)
        ctabla.place(x=20, y=160)

        tk.Label(ctabla,text="Zona critica",bg=self.colores['c2'],fg=self.colores['bg']).place(x=0,y=0,width=260,height=30)

        self.tabla=tk.Listbox(ctabla)
        self.tabla.place(x=0,y=30,width=240,height=180)
        scrollbar = ttk.Scrollbar(master=ctabla,orient=tk.VERTICAL,command=self.tabla.yview)
        scrollbar.place(x=240,y=0,width=20,height=210)


        ctabla2=tk.Frame(self.master,width=260,height=210)
        ctabla2.place(x=290, y=160)

        tk.Label(ctabla2,text="Bloqueados",bg=self.colores['c2'],fg=self.colores['bg']).place(x=0,y=0,width=260,height=30)

        self.tabla2=tk.Listbox(ctabla2)
        self.tabla2.place(x=0,y=30,width=240,height=180)
        scrollbar2 = ttk.Scrollbar(master=ctabla2,orient=tk.VERTICAL,command=self.tabla2.yview)
        scrollbar2.place(x=240,y=0,width=20,height=210)
        
        ctabla3=tk.Frame(self.master,width=520,height=220)
        ctabla3.place(x=20, y=380)
        cab=""
        for i in 'P,TL,R,TC,TF,TR,TE'.split(','):
            cab+=i.ljust(15,' ')
        tk.Label(ctabla3,text=cab,bg=self.colores['c2'],fg=self.colores['bg']).place(x=0,y=0,width=520,height=30)

        self.tabla3=tk.Listbox(ctabla3)
        self.tabla3.place(x=0,y=30,width=500,height=180)
        scrollbar3 = ttk.Scrollbar(master=ctabla3,orient=tk.VERTICAL,command=self.tabla3.yview)
        scrollbar3.place(x=500,y=0,width=20,height=220)


        fig = Figure(figsize=(6, 5), dpi=100)
        ax = fig.add_subplot(111)
        fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.get_tk_widget().place(x=580,y=160,width=450,height=450)

        
    def ciclo(self) -> None:
        tiempo=250
        if self.cajero.clientes[0]!=self.cajero.clientes:
            self.cajero.atender()
        self.cajero.bloqu()
        c=self.cajero.clientes
        b=self.cajero.bloqueados
        self.cajero.t+=1
        self.actualizartabla(c,b)
        self.actualizarFigura()
        self.master.after(tiempo, self.ciclo)
        

    def agregarCliente(self,cliente) -> None:
        cliente_info={c: cliente[c].get() for c in cliente}
        c=self.cajero.append(cliente_info)
        self.actualizartabla(c,self.cajero.bloqueados)

    def actualizartabla(self,clientes,bloqueados) -> None:  
        self.tabla.delete(0, tk.END)
        for i in clientes[:-1]:
            self.tabla.insert(tk.END,f"{i['Nombre']:5} {i['Solicitudes']}")
        self.tabla2.delete(0, tk.END)
        for i in bloqueados:
            self.tabla2.insert(tk.END,f"{i['Nombre']:5} {i['Solicitudes']}")
        V=self.cajero.GenTab()
        self.tabla3.delete(0, tk.END)
        for i in V:
            cad=''
            for j in i:
                cad+=str(j).rjust(15,' ')
            self.tabla3.insert(tk.END,cad)
    
    def actualizarFigura(self):
        fig,ax=self.cajero.diagram()
        self.canvas.figure=fig
        self.canvas.draw()
    
if __name__ == '__main__':
    app = GUI(cajero=Cajero())
    app.master.title('Cajero')
    app.mainloop()
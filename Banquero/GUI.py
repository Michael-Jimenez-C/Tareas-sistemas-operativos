import tkinter as tk
from tkinter import ttk
from Cajero import Cajero
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from elementos.Tabla import Tabla
from elementos.Tabla2 import Tabla2

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
            c=self.cajero.append({'Nombre': f"a{chr(i+ord('a'))}",'Solicitudes':np.random.randint(1,10),'Prioridad':np.random.randint(1,10)})
        self.actualizartabla(c,self.cajero.bloqueados)
        self.cajero.t+=1
        self.master.after(1000, self.ciclo)

    def createWidgets(self) -> None:

        self.master.geometry('1100x700')
        self.master.resizable(width=False , height=False)
        self.master.config(bg=self.colores['bg'])


        client=tk.Frame(self.master,width=260,height=120)
        client.place(x=20,y=20)
        cuali=['Nombre','Solicitudes','Prioridad']
        dif=90//len(cuali)
        cliente_form={}
        for j,i in enumerate(cuali):
            tk.Label(client,text=i,bg=self.colores['c3'],fg=self.colores['c1']).place(x=0,y=dif*j,width=70,height=dif)
            cliente_form[i]=tk.Entry(client)
            cliente_form[i].place(x=70,y=dif*j,width=190,height=dif)
        boton=tk.Button(client,text="ACEPTAR",bg=self.colores['c2'],fg=self.colores['bg'],command=lambda:  self.agregarCliente(cliente_form))
        boton.place(x=0,y=90,width=260,height=30)
        

        self.ctabla=Tabla(self.master,'Zona Critica', 260,210,self.colores['c2'],self.colores['bg'])
        self.ctabla.place(x=20, y=160)

        self.ctabla2=Tabla(self.master,'Bloqueados', 260,210,self.colores['c2'],self.colores['bg'])
        self.ctabla2.place(x=290, y=160)

        cab=""
        for i in 'P,TL,R,TC,TF,TR,TE'.split(','):
            cab+=i.ljust(15,' ')
        self.ctabla3=Tabla(self.master,cab, 520,220,self.colores['c2'],self.colores['bg'])
        #self.ctabla3=Tabla2(self.master,cab, 520,220,self.colores['c2'],self.colores['bg'])
        #self.ctabla3.setHeaders('P,TL,R,TC,TF,TR,TE'.split(','))
        self.ctabla3.place(x=20, y=380)
        self.tabla3=self.ctabla3.getTab()

        fig = Figure()
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
        self.ctabla.actualizar(clientes[:-1],30)
        self.ctabla2.actualizar(bloqueados,30)
        V=self.cajero.GenTab()
        #self.ctabla3.actualizar(V)
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
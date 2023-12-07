import tkinter as tk
from Colas_prioridad import Cola_prioridad
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from elementos.Tabla2 import Tabla2
from Politicas import bloqueados_t
from Contador import Contador
import numpy as np
import time

class GUI(tk.Frame):
    cola=None
    def __init__(self, master=None) -> tk.Frame:
        self.colores={
            "bg": "#fff",
            "c1": "#b01e20",
            "c2": "#460c0d",
            "c3": "#dfa5a6"
            }
        tk.Frame.__init__(self, master)
        self.colaP=Cola_prioridad()
        self.createWidgets()

        for i in range(10):
            self.colaP.append({'Nombre': f"a{chr(i+ord('a'))}",'Solicitudes':np.random.randint(2,9),'Prioridad':np.random.randint(1,10), 'Lista':np.random.randint(1,4)})
        self.actualizartabla()
        Contador.get().next()

        self.master.after(1000, self.ciclo)

    def createWidgets(self) -> None:
        GUI.cola=self.colaP
        self.master.geometry('1140x660')
        self.master.resizable(width=False , height=False)
        self.master.config(bg=self.colores['bg'])
        
        client=tk.Frame(self.master,width=260,height=150)
        client.place(x=20,y=20)
        cuali=['Nombre','Solicitudes','Prioridad','Lista']
        dif=120//len(cuali)
        cliente_form={}
        for j,i in enumerate(cuali):
            tk.Label(client,text=i,bg=self.colores['c3'],fg=self.colores['c1']).place(x=0,y=dif*j,width=70,height=dif)
            cliente_form[i]=tk.Entry(client)
            cliente_form[i].place(x=70,y=dif*j,width=190,height=dif)
        boton=tk.Button(client,text="ACEPTAR",bg=self.colores['c2'],fg=self.colores['bg'],command=lambda:  self.agregarCliente(cliente_form))
        boton.place(x=0,y=120,width=260,height=30)


        self.ctabla1=Tabla2(self.master,'ROUND ROBINS (1)', 260,150,self.colores['c2'],self.colores['bg'])
        self.ctabla1.setHeaders('Nombre,Rafaga,Priodidad'.split(','))
        self.ctabla1.place(x=320, y=20)

        self.ctabla2=Tabla2(self.master,'SRTT (2)', 260,150,self.colores['c2'],self.colores['bg'])
        self.ctabla2.setHeaders('Nombre,Rafaga,Priodidad'.split(','))
        self.ctabla2.place(x=590, y=20)

        self.ctabla3=Tabla2(self.master,'PRIORIDAD (3)', 260,150,self.colores['c2'],self.colores['bg'])
        self.ctabla3.setHeaders('Nombre,Rafaga,Priodidad'.split(','))
        self.ctabla3.place(x=860, y=20)

        self.bloqueados=Tabla2(self.master,'BLOQUEADOS', 380,200,self.colores['c2'],self.colores['bg'])
        self.bloqueados.setHeaders('Nombre,Rafaga,Priodidad'.split(','))
        self.bloqueados.place(x=20, y=190)

        self.procesos=Tabla2(self.master,'PROCESOS', 380,200,self.colores['c2'],self.colores['bg'])
        self.procesos.setHeaders('P,TL,R,TC,TF,TR,TE,PR'.split(','))
        self.procesos.place(x=20, y=420)

        fig = Figure(figsize=(3,3))
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.get_tk_widget().place(x=430,y=190,width=690,height=430)
    
    def agregarCliente(self,cliente) -> None:
        cliente_info={c: cliente[c].get() for c in cliente}
        self.colaP.append(cliente_info)
        self.actualizartabla()

    def actualizartabla(self) -> None:  
        self.ctabla1.actualizar2(self.colaP.colas[1].clientes[:-1])
        self.ctabla2.actualizar2(self.colaP.colas[2].clientes[:-1])
        self.ctabla3.actualizar2(self.colaP.colas[3].clientes[:-1])
        self.bloqueados.actualizar2(bloqueados_t)
        V=self.colaP.colas[1].GenTab()
        self.procesos.actualizar(V)
    
    def actualizarFigura(self,libre=False):
        fig,ax=self.colaP.colas[1].diagram()
        self.canvas.figure=fig
        ax.scatter([-1],[.5],label=f'$t={Contador.get().t-1}$', marker='')
        (ax.scatter([-1],[.5],color='green',label='Libre') if libre else ax.scatter([-1],[.5],color='red',label='En uso'))
        ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.2))
        self.canvas.draw()

    def ciclo(self) -> None:
        proceso_actual=self.colaP.proceso_actual()
        self.colaP.atender()
        self.colaP.bloqueados()
        proceso_siguiente=self.colaP.proceso_actual()
        self.colaP.t+=1
        self.actualizartabla()
        print(proceso_actual,proceso_siguiente)
        if proceso_actual!= proceso_siguiente:
            self.actualizarFigura(True)
            self.master.after(1000, self.actab)
        else:
            self.actab()

    def actab(self):
        self.actualizarFigura()
        self.master.after(500, self.ciclo)

if __name__ == '__main__':
    app = GUI()
    app.master.title('Proyecto - sistemas operativos')
    app.mainloop()
import tkinter as tk
from Colas_prioridad import Cola_prioridad
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from elementos.Tabla2 import Tabla2

class GUI(tk.Frame):
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
        self.master.after(1000, self.ciclo)

    def createWidgets(self) -> None:

        self.master.geometry('1140x660')
        self.master.resizable(width=False , height=False)
        self.master.config(bg=self.colores['bg'])
        
        client=tk.Frame(self.master,width=260,height=150)
        client.place(x=20,y=20)
        cuali=['Nombre','Rafaga','Prioridad','Lista']
        dif=120//len(cuali)
        cliente_form={}
        for j,i in enumerate(cuali):
            tk.Label(client,text=i,bg=self.colores['c3'],fg=self.colores['c1']).place(x=0,y=dif*j,width=70,height=dif)
            cliente_form[i]=tk.Entry(client)
            cliente_form[i].place(x=70,y=dif*j,width=190,height=dif)
        boton=tk.Button(client,text="ACEPTAR",bg=self.colores['c2'],fg=self.colores['bg'],command=lambda:  self.agregarCliente(cliente_form))
        boton.place(x=0,y=120,width=260,height=30)


        self.ctabla1=Tabla2(self.master,'ROUND ROBINS (1)', 260,150,self.colores['c2'],self.colores['bg'])
        self.ctabla1.setHeaders('Nombre,Rafaga,Priodidad,Lista'.split(','))
        self.ctabla1.place(x=320, y=20)

        self.ctabla2=Tabla2(self.master,'SRTT (2)', 260,150,self.colores['c2'],self.colores['bg'])
        self.ctabla2.setHeaders('Nombre,Rafaga,Priodidad,Lista'.split(','))
        self.ctabla2.place(x=590, y=20)

        self.ctabla3=Tabla2(self.master,'PRIORIDAD (3)', 260,150,self.colores['c2'],self.colores['bg'])
        self.ctabla3.setHeaders('Nombre,Rafaga,Priodidad,Lista'.split(','))
        self.ctabla3.place(x=860, y=20)

        self.bloqueados=Tabla2(self.master,'BLOQUEADOS', 380,200,self.colores['c2'],self.colores['bg'])
        self.bloqueados.setHeaders('Nombre,Rafaga,Priodidad,Lista'.split(','))
        self.bloqueados.place(x=20, y=190)

        self.procesos=Tabla2(self.master,'PROCESOS', 380,200,self.colores['c2'],self.colores['bg'])
        self.procesos.setHeaders('P,TL,R,TC,TF,TR,TE,PR'.split(','))
        self.procesos.place(x=20, y=420)

        fig = Figure(figsize=(3,3))
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.get_tk_widget().place(x=430,y=190,width=690,height=430)
    
    def agregarCliente(self,cliente) -> None:
        cliente_info={c: cliente[c].get() for c in cliente}
        c=self.cajero.append(cliente_info)
        self.actualizartabla(c,self.cajero.bloqueados)

    def actualizartabla(self,clientes,bloqueados) -> None:  
        pass
    
    def actualizarFigura(self):
        pass

    def ciclo(self) -> None:
        self.colaP.atender()
        self.colaP.bloqueados()
        self.colaP.t+=1
        self.master.after(500, self.ciclo)


if __name__ == '__main__':
    app = GUI()
    app.master.title('Cajero')
    app.mainloop()
import tkinter as tk
from tkinter import ttk
from Cajero import Cajero
import time


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
        self.master.after(1000, self.atender)

    def createWidgets(self) -> None:
        self.master.geometry('300x400')
        self.master.resizable(width=False , height=False)
        self.master.config(bg=self.colores['bg'])
        client=tk.Frame(self.master,width=260,height=120)
        client.place(x=20,y=20)
        cuali=['Nombre','Solicitudes']
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

        tk.Label(ctabla,text="Cajero",bg=self.colores['c2'],fg=self.colores['bg']).place(x=0,y=0,width=260,height=30)

        self.tabla=tk.Listbox(ctabla)
        self.tabla.place(x=0,y=30,width=240,height=180)
        scrollbar = ttk.Scrollbar(master=ctabla,orient=tk.VERTICAL,command=self.tabla.yview)
        scrollbar.place(x=240,y=0,width=20,height=210)
        
    def atender(self) -> None:
        if self.cajero.clientes[0]==self.cajero.clientes:
            time.sleep(.1)
        else:
            c,k=self.cajero.atender(True)
            time.sleep(k/5)
            self.actualizartabla(c)
        self.master.after(1000, self.atender)

    def agregarCliente(self,cliente) -> None:
        cliente_info={c: cliente[c].get() for c in cliente}
        c=self.cajero.append(cliente_info)
        print(c)
        self.actualizartabla(c)
    
    def actualizartabla(self,clientes) -> None:
        self.tabla.delete(0, tk.END)
        for i in clientes[:-1]:
            self.tabla.insert(tk.END,f"{i['Nombre']:5} {i['Solicitudes']}")
    
if __name__ == '__main__':
    app = GUI(cajero=Cajero())
    app.master.title('Cajero')
    app.mainloop()
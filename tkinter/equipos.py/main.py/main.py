from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from os import path
from tkinter import Menu
class aplicacion:
    def __init__(self, _master):
        self.master = _master
        self.master.title("A simple GUI")
        self.master.geometry('500x500')
        self.ingresarDatos()
        self.verDatos()
    def ingresarDatos(self):
        self.btDatos=Button(self.master,text="ingresar datos")
        self.btDatos.grid(column=10,row=40)
    def verDatos(self):
        self.btVerDatos=Button(root,text="ver Datos")
        self.btVerDatos.grid(column=10,row=200)


root = Tk()
ventana = aplicacion(root)
root.mainloop()
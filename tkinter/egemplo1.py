from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from os import path
from tkinter import Menu



def Click():
    respuesta="hola como esta "+ txt.get()
    etiqueta.configure(text=respuesta)
    print(select.get())
    messagebox.showinfo('saludo','hola diste click')

    res = messagebox.askquestion('Message title','Message content')
    if res:
        print("hola")
    else :
        print("no")

    res = messagebox.askyesno('Message title','Message content')
    if res:
        print("hola")
    else :
        print("no")

    res = messagebox.askyesnocancel('Message title','Message content')
    if res:
        print("hola")
    else :
        print("no")

    res = messagebox.askokcancel('Message title','Message content')
    if res:
        print("hola")
    else :
        print("no")

    res = messagebox.askretrycancel('Message title','Message content')
    if res:
        print("hola")
    else :
        print("no")

def indicador1():
    print(combo.get())
    if int(combo.get()) ==4:
        print("hola")
    if valorChk.get(): 
        print("pendejo")
    dir=filedialog.askdirectory()
    etiqueta.configure(text=dir)
root =Tk()
root.geometry('100x100')
#root.configure(bg='blue')
root.title('holaMundo')


menu = Menu(root)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='edit')

menu.add_cascade(label='File', menu=new_item)
root.config(menu=menu)

txt=Entry(root,width=40,state='disabled')
txt.grid(column=80,row=30)
txt.focus()

etiqueta= Label(root,text="hola",font=("Arial Bold",10))
etiqueta.grid(column=0,row=0)

valorChk=IntVar()  

combo =Combobox(root)
combo['values']=(1,2,3,4,5,'daniel','sebas','joxe')
combo.current(1)
combo.grid(column=80,row=70)

btn= Button(root,text="aceptar",command=indicador1)
btn.grid(column=200,row=150)


chk=Checkbutton(root,text='validador',variable=valorChk)
chk.grid(column=500,row=100)
select=IntVar()
validadorSircular=Radiobutton(root,text='hola',value=0,variable=select,command=Click)
validadorSircular.grid(column=500,row=300)
texto=scrolledtext.ScrolledText(root,width=40,height=10)
texto.grid(column=600,row=200)
texto.insert(INSERT,'hola mundo')

style=ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar",background='red')
bar = Progressbar(root,length=200,style='black.Horizontal.TProgressbar')
bar['value']=10
bar.grid(column=800,row=300)


file=filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

files = filedialog.askopenfilenames(filetypes = (("Text files","*.txt"),("all files","*.*"),("Text files ","*.py")))

file = filedialog.askopenfilename(initialdir= path.dirname(__file__))



root.mainloop()

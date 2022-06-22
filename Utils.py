
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import heading


class redes:
        
    def __init__(self,window):
        self.wind=window
        self.wind.title('Taller')
        self.wind.resizable(0,0)
        self.wind.eval('tk::PlaceWindow . center')
        frame = LabelFrame(self.wind)
        frame.grid(row = 0, column = 0, columnspan = 2, pady = 20)
        # Label(frame).grid(row = 1, column = 0 )
        # self.name = Entry(frame)
        # self.name.focus()
        # self.name.grid(row = 1, column = 1)
        # ttk.Button(frame, text = 'Buscar', command='' ).grid(row = 3, columnspan = 2, sticky = W + E , padx=10 , pady=10)
        self.message = Label(text = '', fg = 'blue')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        self.tree = ttk.Treeview(height = 10, columns = 2 )
        self.tree.grid(row = 2, column = 0, columnspan = 2 , padx=15 )
        #self.tree.heading('#0', text = 'Emisor', anchor = CENTER)
        #self.tree.heading('#1', text = 'Mensaje', anchor = CENTER )
        #self.tree.insert('', 0 , text='jesus@gmail.com',values="Tengoooooo")

        ttk.Button(text = 'Actualizar', command = '').grid(row = 4, column = 0, sticky = W + E ,  padx=10 , pady=(0,15))
        ttk.Button(text = 'Redactar Correo', command = self.RedaccionCorreo).grid(row = 4, column = 1, sticky = W + E , padx=10 , pady=(0,15))
    
    
    def RedaccionCorreo(self):
        self2=Tk()
        self2.resizable(0,0)
        self2.title('Redaccion Correo')
        self2.eval('tk::PlaceWindow . center')
        self2.geometry('400x400')
        lbl = ttk.Label(self2, text="Correo")
        lbl.pack()
        lbl = ttk.Label(self2, text="Mail from:")
        lbl.pack()

        txt = ttk.Entry(self2,width=50)
        txt.pack()

        lbl = ttk.Label(self2, text="Recep to:")
        lbl.pack()

        txt = ttk.Entry(self2,width=50)
        txt.pack()

        lbl = ttk.Label(self2, text="Subject:")
        lbl.pack()

        txt = ttk.Entry(self2,width=50)
        txt.pack()


        lbl = ttk.Label(self2, text="Cuerpo del mensaje")
        lbl.pack()

        txt = ttk.Entry(self2, width=50)
        txt.pack()

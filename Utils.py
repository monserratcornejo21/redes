
from ast import Pass
from cProfile import label
from cgitb import text
from cmath import e
from tkinter import *
from tkinter import ttk
# from tkinter import _ScreenUnits
from tkinter.tix import ROW
from turtle import width
#from mysqlx import Row
# from Pop3 import IniciarSesion

#from numpy import insert


class redes:
    mail=''
    password=''
    def __init__(self,window):  
        self.wind=window
        self.login(self.wind)
        # if(self.aux==2):
        #     self.wind=window         
    
    def RedaccionCorreo(self):
        window=Tk()
        window.resizable(0,0)
        window.title('Redaccion Correo')
        window.eval('tk::PlaceWindow . center')
        
        frame1 = LabelFrame(window)
        Label(frame1,text='From'+'     '+self.mail).grid(row = 1, column = 0 , padx=(0,15))
        frame1.grid(row = 0, column = 0, columnspan = 2 , pady=5 , padx=(5) , sticky=W)
        
        frame2 = LabelFrame(window)
        frame2.grid(row = 1, column = 0, columnspan = 2 , pady=5 , padx=5 , sticky=W+E)
        Label(frame2,text='To').grid(row = 1, column = 0 )
        window.To = Entry(frame2,width=104)
        window.To.focus()
        window.To.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        frame3 = LabelFrame(window)
        frame3.grid(row = 2, column = 0, columnspan = 2, pady=5 , padx=5 , sticky=W+E)
        Label(frame3,text='Subject').grid(row = 1, column = 0 )
        window.Subject = Entry(frame3,width=100)
        window.Subject.grid(row = 1, column = 1 , padx=15 , pady=5 ,sticky=W+E)
        
        frame4 = LabelFrame(window)
        frame4.grid(row = 3, column = 0, columnspan = 2, pady = 5 , sticky=W+E , padx=5)
        Label(frame4).grid(row = 1, column = 0 )
        window.Messaje = Entry(frame4 ,width=110)
        window.Messaje.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        ttk.Button(window,text = 'Descartar', command = window.destroy).grid(row = 4, column = 0, sticky = W + E , padx=10 , pady=(8,8))
        ttk.Button(window,text = 'Enviar', command = window.enviarcorreo).grid(row = 4, column = 1, sticky = W + E ,  padx=10 , pady=(8,8))   
    def enviarcorreo(self):
        
        
    def login(self,window):
        
        window.title('Iniciar Sesion')
        window.eval('tk::PlaceWindow . center')
        frame = LabelFrame(window)
        frame.grid(row = 0, column = 0, columnspan = 2 , pady=5 , padx=5 , sticky=W+E)
        Label(frame,text='Correo').grid(row = 1, column = 0 )
        window.Mail = Entry(frame,width=35)
        window.Mail.focus()
        window.Mail.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        frame2 = LabelFrame(window)
        frame2.grid(row = 1, column = 0, columnspan = 2 , pady=5 , padx=5 , sticky=W+E)
        Label(frame2,text='Pass').grid(row = 1, column = 0 )
        window.Pass = Entry(frame2,width=37)
        window.Pass.grid(row = 1, column = 1 , padx=15 , pady=5 , sticky=W+E)
        
        # self.mail=window.Mail.get()
        # self.password=window.Pass.get()
    
        ttk.Button(window,text = 'Entrar', command =self.MenuP).grid(row = 4, column = 0, columnspan=5,sticky = W + E , padx=10 , pady=(8,8))
            
    def MenuP(self):
        self.mail=self.wind.Mail.get()
        self.password=self.wind.Pass.get()
        self.wind.destroy()
        window=Tk()
        window.title('Gmailnt')
        window.resizable(0,0)
        window.eval('tk::PlaceWindow . center')
        frame = LabelFrame(window)
        frame.grid(row = 0, column = 0, columnspan = 2, pady = 20)
        # Label(frame).grid(row = 1, column = 0 )
        # self.name = Entry(frame)
        # self.name.focus()
        # self.name.grid(row = 1, column = 1)
        window.message = Label(text = '', fg = 'red')
        window.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        window.tree = ttk.Treeview(height = 10, columns = 2 )
        window.tree.grid(row = 2, column = 0, columnspan = 2 , padx=15 )
        window.tree.heading('#0', text = 'Emisor', anchor = CENTER)
        window.tree.heading('#1', text = 'Mensaje', anchor = CENTER )
        
        # ttk.Button(frame, text = 'Agregar', command= self.actualizarCorreo ).grid(row = 3, columnspan = 2, sticky = W + E , padx=10 , pady=10)
        ttk.Button(text = 'Actualizar', command = '').grid(row = 4, column = 0, sticky = W + E ,  padx=10 , pady=(0,15))
        ttk.Button(text = 'Redactar Correo', command = self.RedaccionCorreo).grid(row = 4, column = 1, sticky = W + E , padx=10 , pady=(0,15))

    
    def actualizarCorreo(self):
        self.tree.insert('', 0 , text='Eo',values=self.name.get())
        
    def d(self):
        self.tree.insert('', 0 , text='Eo',values=self.name.get())
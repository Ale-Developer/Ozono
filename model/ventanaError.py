import os
from tkinter import *

def ventanaError():
    ventanaEror = Tk()
    ventanaEror.title("Ozono")
    ventanaEror.geometry("200x200")
    error = "Hubo un error en la base de datos \nContacte con el administrador"
    errorLabel = Label(ventanaEror, text=error)
    errorLabel.pack()
    ventanaEror.mainloop()
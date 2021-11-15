from tkinter import *
from tkinter import messagebox as mb
import sqlite3
from model.conexion import *

conexion = sqlite3.connect("data/login.db")
tabla = conexion.cursor()
ventanaRegistrar=None


def Registrar():
	global ventanaRegistrar
	def cerrarTop():
		global ventanaRegistrar
		ventanaRegistrar.destroy()
		ventanaRegistrar = None
	if ventanaRegistrar == None:
		ventanaRegistrar=Toplevel()
		ventanaRegistrar.title("Registro de Usuario")
		ventanaRegistrar.geometry("500x600")
		ventanaRegistrar.resizable(False,False)
			
			
		frameLogin = Frame(ventanaRegistrar)
		frameLogin.place(x=0, y=0, width=700, height=600)
			
		FondoEntryNuevo = PhotoImage(file="image/Entry8.png")
		fondolbl0 = Label(frameLogin, image=FondoEntryNuevo)
		fondolbl0.place(x=500000,y=200000)
		entryId = Entry(frameLogin, width=33)
		entryId.place(x=72,y=43)
		entryId.config(relief="flat",state="readonly")
		labelId = Label(frameLogin, text="Id:")
		labelId.place(x=9000000, y=1000000000)

		fondolbl = Label(frameLogin, image=FondoEntryNuevo).place(x=50,y=20)
		entrynombre = Entry(frameLogin, width=33)
		entrynombre.place(x=72,y=43)
		entrynombre.config(relief="flat")
		labelNombre = Label(frameLogin, text="Nombre:")
		labelNombre.place(x=90, y=0)

		fondolbl2 = Label(frameLogin, image=FondoEntryNuevo).place(x=50,y=110)
		entryApellido = Entry(frameLogin, width=33)
		entryApellido.place(x=72,y=133)
		entryApellido.config(relief="flat")
		labelApellido = Label(frameLogin, text="Apellido:")
		labelApellido.place(x=90, y=90)

		fondolbl3 = Label(frameLogin, image=FondoEntryNuevo).place(x=50,y=200)
		entryUsuario = Entry(frameLogin, width=33)
		entryUsuario.place(x=72,y=223)
		entryUsuario.config(relief="flat")
		labelUsuario = Label(frameLogin, text="Usuario:")
		labelUsuario.place(x=90, y=180)

		fondolbl4 = Label(frameLogin, image=FondoEntryNuevo).place(x=50,y=290)
		entryContraseña = Entry(frameLogin, width=33, show="●")
		entryContraseña.place(x=72,y=313)
		entryContraseña.config(relief="flat")
		labelContraseña = Label(frameLogin, text="Contraseña:")
		labelContraseña.place(x=90, y=270)

		fondolbl5 = Label(frameLogin, image=FondoEntryNuevo).place(x=50,y=380)
		entryContraseña2 = Entry(frameLogin, width=33, show="●")
		entryContraseña2.place(x=72,y=403)
		entryContraseña2.config(relief="flat")
		labelContraseña2 = Label(frameLogin, text="Repetir contraseña:")
		labelContraseña2.place(x=90, y=360)

		def registro():
			datos = (entrynombre.get(),entryApellido.get(),entryUsuario.get(),entryContraseña.get(),entryContraseña2.get(),)
			datos1 = (entrynombre.get(),entryApellido.get(),entryUsuario.get(),entryContraseña.get())
			if(entryContraseña.get()==entryContraseña2.get()):
				tabla = conexion.cursor()
				sql = "INSERT INTO usuarios (Nombre, Apellido, Usuario, Pass) VALUES(?,?,?,?)"
				tabla.execute(sql,datos1)
				conexion.commit()
				mb.showinfo(title="Registro correcto", message="Hola "+datos[2]+"\nSu registro fue exitoso.")
			else:
				mb.showerror(title="Contraseña Incorrecta",message="Error!!! \nLas contraseñas no coinciden.")
			tabla.close()
			conexion.close()


			'''Nombre=entrynombre.get()
			Apellido=entryApellido.get()
			Usr_reg=entryUsuario.get()
			Contra_reg=entryContraseña.get()
			Contra_reg_2=entryContraseña2.get()
			if(Contra_reg==Contra_reg_2):
				tabla.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
				conexion.commit()
				mb.showinfo(title="Registro Correcto",message="Hola " + Nombre + " " + Apellido + "!!!" + "\nSu registro fue exitoso.")
				ventanaRegistrar.destroy()
			else:
				mb.showerror(title="Contraseña Incorrecta",message="Error!!! \nLas contraseñas no coinciden.")
			tabla.close()
			conexion.close()'''
		
		
		btRegistrar = PhotoImage(file="image/Registrar.png")
		BotonRegistrar = Button(frameLogin,command=registro, image=btRegistrar,relief="flat",bd=0).place(x=200, y=450)
	ventanaRegistrar.protocol("WM_DELETE_WINDOW",cerrarTop)

	ventanaRegistrar.mainloop()
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from datetime import date,datetime
import sqlite3
import time
import os
from tkinter import font
from tkinter.font import families
from model.signup import *
from model.conexion import *
from model.ventanaError import *
from model.consultas import *
from model.validaciones import *
import random

ventanaAgregar = None
ventanaVenta = None
listadoCompras=[]
listadoVentas=[]

def ventanaLogin():
    ventanaLogin = Tk()
    ventanaLogin.title("Ozono")
    ancho = ventanaLogin.winfo_screenwidth()
    largo = ventanaLogin.winfo_screenheight()
    ancho = ventanaLogin.winfo_screenwidth()
    largo = ventanaLogin.winfo_screenheight()
    x = (ancho // 2) - (400//2)
    y = (largo // 2) - (400//2)
    ventanaLogin.geometry(f"{400}x{400}+{x}+{y}")
    ventanaLogin.resizable(0, 0)


    def ingresoPrograma():
        ventanaLogin.destroy()
        ventanaPrincipal()

    def login():
        create_table()
        usuario=entryusuario.get()
        contr=entryContraseña.get()
        tabla.execute("SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?",(usuario,contr))
        if tabla.fetchall():
            global sesion
            sesion=usuario
            mb.showinfo(title="Login Correcto",message="Bienvenido "+usuario+"!!!")
            ingresoPrograma()
        else:
            mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")
        tabla.close()
        conexion.close()



    frameLogin = Frame(ventanaLogin)
    frameLogin.place(x=0, y=0, width=700, height=500)

    FondoEntry = PhotoImage(file="image/Entry8.png")
    fondolbl = Label(frameLogin, image=FondoEntry).place(x=50, y=50)
    entryusuario = Entry(frameLogin, width=33)
    entryusuario.place(x=72, y=73)
    entryusuario.config(relief="flat")
    labellogin = Label(frameLogin, text="Usuario:")
    labellogin.place(x=90, y=30)
    
    fondolbl2 = Label(frameLogin, image=FondoEntry).place(x=50, y=150)
    entryContraseña = Entry(frameLogin, width=33, show="●")
    entryContraseña.place(x=72, y=173)
    entryContraseña.config(relief="flat")
    labelContraseña = Label(frameLogin, text="Contraseña:")
    labelContraseña.place(x=90, y=130)

    btiniciar = PhotoImage(file="image/Entrar.png")
    BotonIniciar = Button(frameLogin, command=login,image=btiniciar, relief="flat", bd=0).place(x=200, y=230)

    btwhatsapp = PhotoImage(file="image/whatsapp.gif")
    botwhatsapp = Button(frameLogin, image=btwhatsapp, relief="flat", bd=0).place(x=30, y=350)

    btinsta = PhotoImage(file="image/insta.gif")
    botinsta = Button(frameLogin, image=btinsta, relief="flat", bd=0).place(x=80, y=350)

    btface = PhotoImage(file="image/face.gif")
    botface = Button(frameLogin, image=btface, relief="flat", bd=0).place(x=130, y=350)

    labelRegistro = Label(frameLogin, text="¿No tienes cuenta?")
    labelRegistro.place(x=180, y=295)
    btRegistrar = PhotoImage(file="image/Registrar.png")
    BotonRegistrar = Button(frameLogin, command=Registrar, image=btRegistrar, relief="flat", bd=0).place(x=200, y=320)



    ventanaLogin.mainloop()



ventanaPrincipal = None
def ventanaPrincipal():
    root1 = Tk()
    root1.title("Ozono")
    ancho = root1.winfo_screenwidth()
    largo = root1.winfo_screenheight()
    x = (ancho // 2) - (1000//2)
    y = (largo // 2) - (700//2)
    root1.geometry(f"{1000}x{600}+{x}+{y}")
    root1.resizable(0,0)

    global esDia
    esDia = True

    def borrarListarCliente():
        for dato in tablaListarCliente.get_children():
            tablaListarCliente.delete(dato)

    def borrarListarProveedor():
        for dato in tablaListarProveedor.get_children():
            tablaListarProveedor.delete(dato)
            
    def borrarListarCompra():
        for dato in tablaListarCompra.get_children():
            tablaListarCompra.delete(dato)
            
    def borrarListarArticulos():
        for dato in tablaListarArticulos.get_children():
            tablaListarArticulos.delete(dato)

    # Menu

    menubar = Menu(root1)
    root1.config(menu=menubar)

    # Funciones de menu
    def helpm():
        mb.showinfo(
            "Bienvenido", "Gracias por elejir Ozono, brindamos nuestro servicio para que su negocio sea más organizado.")

    def about():
        mb.showinfo(
            "Acerca de...", "Propiedad intelectual: Alejandro Espinosa / Version: 1.0 / Date: 25/08/21 / Python: 3.8 ")

    def contact():
        mb.showinfo("Contacto", "Contacto: miguel.espinosa77696@gmail.com")

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Salir", command=root1.quit)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Bienvenido", command=helpm)
    helpmenu.add_command(label="Contacto", command=contact)
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...", command=about)

    # Menus en pantalla
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    # Panel de pestañas
    nb = ttk.Notebook(root1)
    nb.pack(side=LEFT,fill=BOTH,expand=1)

    # Pestañas
    p1 = ttk.Frame(nb)
    p2 = ttk.Frame(nb)
    p3 = ttk.Frame(nb)
    p4 = ttk.Frame(nb)
    p5 = ttk.Frame(nb)

    # Pestaña Cliente   #########################################################################

    # Funciones
    def vaciarEntryCliente():
        entryIdCliente.config(state="normal")
        entryIdCliente.delete(0, END)
        entryIdCliente.config(state="readonly")
        entryRSocialCliente.delete(0, END)
        entryCuitCliente.config(state="normal")
        entryCuitCliente.delete(0, END)
        entryDireccionCliente.delete(0, END)
        entryLocalidadCliente.delete(0, END)
        entryProvinciaCliente.delete(0, END)
        entryCPCliente.delete(0, END)
        entryTelefonoCliente.delete(0, END)
        entryIvaCliente.delete(0, END)


    def listarClientes():
        borrarListarCliente()
        tabla = conexion.cursor()
        sql = "SELECT idClientes,razonSocialCliente,cuitCliente,direccionCliente,localidadCliente,provinciaCliente,codigoPostalCliente,telefonoCliente,ivaCliente FROM Clientes"
        tabla.execute(sql)
        datosListar = tabla.fetchall()
        for dato in datosListar:
            tablaListarCliente.insert("", END, text=dato["idClientes"], values=(dato["razonSocialCliente"], dato["cuitCliente"], dato["direccionCliente"],
                                    dato["localidadCliente"], dato["provinciaCliente"], dato["codigoPostalCliente"], dato["telefonoCliente"], dato["ivaCliente"]))

    def modificarCliente():
        entryIdCliente.config(state="normal")
        datosClientes = (entryRSocialCliente.get(), 
                        entryCuitCliente.get(), 
                        entryDireccionCliente.get(), 
                        entryLocalidadCliente.get(), 
                        entryProvinciaCliente.get(), 
                        entryCPCliente.get(), 
                        entryTelefonoCliente.get(), 
                        entryIvaCliente.get(), 
                        entryCuitCliente.get())
        entryIdCliente.config(state="readonly")
        if (datosClientes[8] != ""):
            if(vacios(datosClientes)):
                tabla = conexion.cursor()
                sql = "UPDATE Clientes SET razonSocialCliente=?,cuitCliente=?,direccionCliente=?,localidadCliente=?,provinciaCliente=?,codigoPostalCliente=?,telefonoCliente=?,ivaCliente=? WHERE cuitCliente=?"
                tabla.execute(sql, datosClientes)
                conexion.commit
                tabla.close
                vaciarEntryCliente()
                mb.showinfo("Sistema", "Se ha modificado correctamente")
            else:
                mb.showinfo("Sistema", "Complete todos los campos")
        else:
            mb.showwarning("Sistema", "Debe ingresar un dato ha modificar")

    
    def getDatoCliente():
        datos = (entryRSocialCliente.get(), 
                        entryCuitCliente.get(), 
                        entryDireccionCliente.get(), 
                        entryLocalidadCliente.get(), 
                        entryProvinciaCliente.get(), 
                        entryCPCliente.get(), 
                        entryTelefonoCliente.get(), 
                        entryIvaCliente.get())
        return datos

    def borrarCliente():
        datos = (entryIdCliente.get(),)
        nombreTabla = "Clientes"
        nombreCampos = "idClientes"
        valores = "?"
        eliminar(conexion,datos,nombreTabla,nombreCampos,valores,vaciarEntryCliente)
            

    def guardarCliente():
        datosCliente = getDatoCliente()
        if (vacios(datosCliente)):
            if (SoloLetras(datosCliente[0]) and soloNumeros(datosCliente[6])):
                nombreTabla = "Clientes"
                nombreCampos = "razonSocialCliente,cuitCliente,direccionCliente,localidadCliente,provinciaCliente,codigoPostalCliente,telefonoCliente,ivaCliente"
                valores = "?,?,?,?,?,?,?,?"
                guardar(conexion,getDatoCliente(),nombreTabla,nombreCampos,valores,vaciarEntryCliente)
            else:
                mb.showwarning("Ozono","Verifique los datos ingresados")
        else:
            mb.showinfo("Ozono", "Complete todos los campos")

    labelFrameCliente = LabelFrame(p3, text="Clientes")
    labelFrameCliente.config(width=1440//4, height=1100//2)
    labelFrameCliente.place(x=10, y=10)
    

    labelIdCliente = Label(labelFrameCliente, text="ID: ")
    labelIdCliente.place(x=30, y=30)
    entryIdCliente = Entry(labelFrameCliente, width=33)
    entryIdCliente.config(state="readonly")
    entryIdCliente.place(x=120, y=30)

    labelRSocialCliente = Label(labelFrameCliente, text="Razon Social: ")
    labelRSocialCliente.place(x=30, y=80)
    entryRSocialCliente = Entry(labelFrameCliente, width=33)
    entryRSocialCliente.place(x=120, y=80)

    labelCuitCliente = Label(labelFrameCliente, text="CUIT: ")
    labelCuitCliente.place(x=30, y=130)
    entryCuitCliente = Entry(labelFrameCliente, width=33)
    entryCuitCliente.place(x=120, y=130)

    labelDireccionCliente = Label(labelFrameCliente, text="Dirección: ")
    labelDireccionCliente.place(x=30, y=180)
    entryDireccionCliente = Entry(labelFrameCliente, width=33)
    entryDireccionCliente.place(x=120, y=180)

    labelLocalidadCliente = Label(labelFrameCliente, text="Localidad: ")
    labelLocalidadCliente.place(x=30, y=230)
    entryLocalidadCliente = Entry(labelFrameCliente, width=33)
    entryLocalidadCliente.place(x=120, y=230)

    labelProvinviaCliente = Label(labelFrameCliente, text="Provincia: ")
    labelProvinviaCliente.place(x=30, y=280)
    entryProvinciaCliente = Entry(labelFrameCliente, width=33)
    entryProvinciaCliente.place(x=120, y=280)

    labelCPCliente = Label(labelFrameCliente, text="Código postal: ")
    labelCPCliente.place(x=30, y=330)
    entryCPCliente = Entry(labelFrameCliente, width=33)
    entryCPCliente.place(x=120, y=330)

    labelTelefonoCliente = Label(labelFrameCliente, text="Teléfono: ")
    labelTelefonoCliente.place(x=30, y=380)
    entryTelefonoCliente = Entry(labelFrameCliente, width=33)
    entryTelefonoCliente.place(x=120, y=380)

    labelIvaCliente = Label(labelFrameCliente, text="I.V.A: ")
    labelIvaCliente.place(x=30, y=430)
    entryIvaCliente = Entry(labelFrameCliente, width=33)
    entryIvaCliente.place(x=120, y=430)

    botonCliente = Button(
        labelFrameCliente, text="Guardar", command=guardarCliente)
    botonCliente.place(x=100, y=490)

    botonCliente = Button(labelFrameCliente, text="Limpiar",
                        command=vaciarEntryCliente)
    botonCliente.place(x=25, y=490)

    botonCliente = Button(
        labelFrameCliente, text="Modificar", command=modificarCliente)
    botonCliente.place(x=175, y=490)
    
    botonCliente = Button(
        labelFrameCliente, text="Borrar", command=borrarCliente)
    botonCliente.place(x=260, y=490)

    # Buscar Cliente en grid:

    def BuscarClienteCiut():
        datosCuit = ("%"+entryBuscarCliente.get()+"%",)
        if (vacios(datosCuit)):
            tabla = conexion.cursor()
            sql = "SELECT * FROM Clientes WHERE cuitCliente LIKE ?"
            tabla.execute(sql, datosCuit)
            datosCliente = tabla.fetchall()
            if(len(datosCliente) > 0):
                vaciarEntryCliente()
                for dato in datosCliente:
                    entryIdCliente.config(state="normal")
                    entryIdCliente.insert(END, dato["idClientes"])
                    entryIdCliente.config(state="readonly")
                    entryRSocialCliente.insert(END, dato["razonSocialCliente"])
                    entryCuitCliente.config(state="normal")
                    entryCuitCliente.insert(END, dato["cuitCliente"])
                    entryDireccionCliente.insert(END, dato["direccionCliente"])
                    entryLocalidadCliente.insert(END, dato["localidadCliente"])
                    entryProvinciaCliente.insert(END, dato["provinciaCliente"])
                    entryCPCliente.insert(END, dato["codigoPostalCliente"])
                    entryTelefonoCliente.insert(END, dato["telefonoCliente"])
                    entryIvaCliente.insert(END, dato["ivaCliente"])
                    mb.showwarning("Sistema", "Busqueda Completada")
            else:
                mb.showwarning("Sistema", "El dato ingresado no existe")
                vaciarEntryCliente()
        else:
            mb.showwarning("Sistema", "Debe ingresar el C.U.I.T")

    labelFrameCliente = LabelFrame(p3, text="Buscar clientes")
    labelFrameCliente.config(width=2450//4, height=1100//2)
    labelFrameCliente.place(x=380, y=10)

    tablaListarCliente = ttk.Treeview(labelFrameCliente, columns=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
    tablaListarCliente.column("#0", width=2)

    tablaListarCliente.column("col1", width=33, anchor=CENTER)
    tablaListarCliente.column("col2", width=33, anchor=CENTER)
    tablaListarCliente.column("col3", width=33, anchor=CENTER)
    tablaListarCliente.column("col4", width=33, anchor=CENTER)
    tablaListarCliente.column("col5", width=33, anchor=CENTER)
    tablaListarCliente.column("col6", width=20, anchor=CENTER)
    tablaListarCliente.column("col7", width=33, anchor=CENTER)
    tablaListarCliente.column("col8", width=7, anchor=CENTER)

    tablaListarCliente.heading("#0", text="ID", anchor=CENTER)
    tablaListarCliente.heading("col1", text="Razon Social", anchor=CENTER)
    tablaListarCliente.heading("col2", text="CUIT", anchor=CENTER)
    tablaListarCliente.heading("col3", text="Dirección", anchor=CENTER)
    tablaListarCliente.heading("col4", text="Localidad", anchor=CENTER)
    tablaListarCliente.heading("col5", text="Provincia", anchor=CENTER)
    tablaListarCliente.heading("col6", text="CP", anchor=CENTER)
    tablaListarCliente.heading("col7", text="Teléfono", anchor=CENTER)
    tablaListarCliente.heading("col8", text="I.V.A", anchor=CENTER)
    
    tablaListarCliente.place(x=4, y=10, width=600, height=250)
    
    def infoCliente(evento):
        index= tablaListarCliente.item(tablaListarCliente.selection())['text']
        detalles=tablaListarCliente.item(tablaListarCliente.selection())['values']
        rSocial=f"{detalles[0]}"
        cuit=f"{detalles[1]}"
        direccion=f"{detalles[2]}"
        localidad=f"{detalles[3]}"
        provincia=f"{detalles[4]}"
        cPostal=f"{detalles[5]}"
        telefono=f"{detalles[6]}"
        iva=f"{detalles[7]}"
        entryIdCliente.config(state="normal")
        entryRSocialCliente.config(state="normal")
        entryIdCliente.delete(0,END)
        entryIdCliente.insert(END,index)
        entryRSocialCliente.delete(0,END)
        entryRSocialCliente.insert(END,rSocial)
        entryCuitCliente.delete(0,END)
        entryCuitCliente.insert(END,cuit)
        entryDireccionCliente.delete(0,END)
        entryDireccionCliente.insert(END,direccion)
        entryLocalidadCliente.delete(0,END)
        entryLocalidadCliente.insert(END,localidad)
        entryProvinciaCliente.delete(0,END)
        entryProvinciaCliente.insert(END,provincia)
        entryCPCliente.delete(0,END)
        entryCPCliente.insert(END,cPostal)
        entryTelefonoCliente.delete(0,END)
        entryTelefonoCliente.insert(END,telefono)
        entryIvaCliente.delete(0,END)
        entryIvaCliente.insert(END,iva)
        entryIdCliente.config(state="readonly")
        entryRSocialCliente.config(state="normal")
    tablaListarCliente.bind("<<TreeviewSelect>>",infoCliente)
    
    # Buscar clientes con ciut
    labelBuscarCliente = Label(labelFrameCliente, text="CUIT:")
    labelBuscarCliente.place(x=4, y=400)
    entryBuscarCliente = Entry(labelFrameCliente, width=33)
    entryBuscarCliente.place(x=50, y=400)
    botonBuscarCliente = Button(
    labelFrameCliente, text="Buscar", command=BuscarClienteCiut)
    botonBuscarCliente.place(x=300, y=400)

    botonListarCliente = Button(
    labelFrameCliente, text="Listar", command=listarClientes)
    botonListarCliente.place(x=400, y=400)


    '''def buscarPorNombre(evento):
        buscar = ("%"+.get()+"%",
                  "%"+entryBuscarPorNombre.get()+"%",)
        tabla = conexion.cursor()
        tabla.execute(
            "SELECT * FROM Clientes WHERE razonSocialCliente LIKE ? OR cuitCliente LIKE ?", buscar)
        datosListar = tabla.fetchall()
        for filas in tablaListarCliente.get_children():
            tablaListarCliente.delete(filas)
        for dato in datosListar:
            tablaListarCliente.insert("", END, text=dato["idClientes"], values=(dato["razonSocialCliente"], dato["cuitCliente"], dato["direccionCliente"],
                                      dato["localidadCliente"], dato["provinciaCliente"], dato["codigoPostalCliente"], dato["telefonoCliente"], dato["ivaCliente"]))'''

    #entryBuscarPorNombre.bind("<Key>", buscarPorNombre)
    
    def modoOscuro():
        labelFrameCliente.config(background= "Gray26")
        labelBuscarCliente.config(background="Gray26")
    def modoDia():
        labelFrameCliente.config(background= "Gray95")
        labelBuscarCliente.config(background= "Gray95")

##### PROVEEDORES   ################################################################################
    ## Funciones
    def vaciarEntryProveedor():
        entryIdProveedor.config(state="normal")
        entryIdProveedor.delete(0, END)
        entryIdProveedor.config(state="readonly")
        entryRSocialProveedor.delete(0, END)
        entryCuitProveedor.config(state="normal")
        entryCuitProveedor.delete(0, END)
        entryDireccionProveedor.delete(0, END)
        entryLocalidadProveedor.delete(0, END)
        entryProvinciaProveedor.delete(0, END)
        entryCPProveedor.delete(0, END)
        entryTelefonoProveedor.delete(0, END)
        entryIvaProveedor.delete(0, END)

    def listarProveedor():
        borrarListarProveedor()
        tabla = conexion.cursor()
        sql = "SELECT idProveedor,razonSocialProveedor,cuitProveedor,direccionProveedor,localidadProveedor,provinciaProveedor,codigoPostalProveedor,telefonoProveedor,ivaProveedor FROM Proveedores"
        tabla.execute(sql)
        datosListar = tabla.fetchall()
        for dato in datosListar:
            tablaListarProveedor.insert("", END, text=dato["idProveedor"], 
            values=(dato["razonSocialProveedor"], 
            dato["cuitProveedor"], 
            dato["direccionProveedor"],
            dato["localidadProveedor"], 
            dato["provinciaProveedor"], 
            dato["codigoPostalProveedor"], 
            dato["telefonoProveedor"], 
            dato["ivaProveedor"]))

    def modificarProveedor():
        entryIdProveedor.config(state="normal")
        datosProveedor = (entryRSocialProveedor.get(), 
        entryCuitProveedor.get(), 
        entryDireccionProveedor.get(), 
        entryLocalidadProveedor.get(), 
        entryProvinciaProveedor.get(), 
        entryCPProveedor.get(), 
        entryTelefonoProveedor.get(), 
        entryIvaProveedor.get(), 
        entryCuitProveedor.get())
        entryIdProveedor.config(state="readonly")
        if (datosProveedor[8] != ""):
            if(vacios(datosProveedor)):
                tabla = conexion.cursor()
                sql = "UPDATE Proveedores SET razonSocialProveedor=?,cuitProveedor=?,direccionProveedor=?,localidadProveedor=?,provinciaProveedor=?,codigoPostalProveedor=?,telefonoProveedor=?,ivaProveedor=? WHERE cuitProveedor=?"
                tabla.execute(sql, datosProveedor)
                conexion.commit
                tabla.close
                mb.showinfo("Sistema", "Se ha modificado correctamente")
            else:
                mb.showinfo("Sistema", "Complete todos los campos")
        else:
            mb.showwarning("Sistema", "Debe ingresar un dato ha modificar")

    def getDatosProveedor():
        datos = (entryRSocialProveedor.get(),
                entryCuitProveedor.get(), 
                entryDireccionProveedor.get(), 
                entryLocalidadProveedor.get(), 
                entryProvinciaProveedor.get(), 
                entryCPProveedor.get(), 
                entryTelefonoProveedor.get(), 
                entryIvaProveedor.get())
        return datos

    def borrarProveedor():
        datos = (entryIdProveedor.get(),)
        nombreTabla = "Proveedores"
        nombreCampos = "idProveedor"
        valores = "?"
        eliminar(conexion,datos,nombreTabla,nombreCampos,valores,vaciarEntryProveedor)

    def guardarProveedor():
        datos = getDatosProveedor()
        if (vacios(datos)):
            if (SoloLetras(datos[0]) and soloNumeros(datos[6])):
                nombreTabla = "Proveedores"
                nombreCampos = "razonSocialProveedor,cuitProveedor,direccionProveedor,localidadProveedor,provinciaProveedor,codigoPostalProveedor,telefonoProveedor,ivaProveedor"
                valores = "?,?,?,?,?,?,?,?"
                guardar(conexion,getDatosProveedor(),nombreTabla,nombreCampos,valores,vaciarEntryProveedor)
            else:
                mb.showwarning("Ozono", "Verifique los datos ingresados")
        else:
            mb.showinfo("Ozono", "Complete todos los campos")

    labelFrameProveedor = LabelFrame(p4, text="Proveedores")
    labelFrameProveedor.config(width=1440//4, height=1100//2)
    labelFrameProveedor.place(x=10, y=10)

    labelIdProveedor = Label(labelFrameProveedor, text="ID: ")
    labelIdProveedor.place(x=30, y=30)
    entryIdProveedor = Entry(labelFrameProveedor, width=33)
    entryIdProveedor.config(state="readonly")
    entryIdProveedor.place(x=120, y=30)

    labelRSocialProveedor = Label(labelFrameProveedor, text="Razon Social: ")
    labelRSocialProveedor.place(x=30, y=80)
    entryRSocialProveedor = Entry(labelFrameProveedor, width=33)
    entryRSocialProveedor.place(x=120, y=80)

    labelCuitProveedor = Label(labelFrameProveedor, text="CUIT: ")
    labelCuitProveedor.place(x=30, y=130)
    entryCuitProveedor = Entry(labelFrameProveedor, width=33)
    entryCuitProveedor.place(x=120, y=130)

    labelDireccionProveedor = Label(labelFrameProveedor, text="Dirección: ")
    labelDireccionProveedor.place(x=30, y=180)
    entryDireccionProveedor = Entry(labelFrameProveedor, width=33)
    entryDireccionProveedor.place(x=120, y=180)

    labelLocalidadProveedor = Label(labelFrameProveedor, text="Localidad: ")
    labelLocalidadProveedor.place(x=30, y=230)
    entryLocalidadProveedor = Entry(labelFrameProveedor, width=33)
    entryLocalidadProveedor.place(x=120, y=230)

    labelProvinviaProveedor = Label(labelFrameProveedor, text="Provincia: ")
    labelProvinviaProveedor.place(x=30, y=280)
    entryProvinciaProveedor = Entry(labelFrameProveedor, width=33)
    entryProvinciaProveedor.place(x=120, y=280)

    labelCPProveedor = Label(labelFrameProveedor, text="Código postal: ")
    labelCPProveedor.place(x=30, y=330)
    entryCPProveedor = Entry(labelFrameProveedor, width=33)
    entryCPProveedor.place(x=120, y=330)

    labelTelefonoProveedor = Label(labelFrameProveedor, text="Teléfono: ")
    labelTelefonoProveedor.place(x=30, y=380)
    entryTelefonoProveedor = Entry(labelFrameProveedor, width=33)
    entryTelefonoProveedor.place(x=120, y=380)

    labelIvaProveedor = Label(labelFrameProveedor, text="I.V.A: ")
    labelIvaProveedor.place(x=30, y=430)
    entryIvaProveedor = Entry(labelFrameProveedor, width=33)
    entryIvaProveedor.place(x=120, y=430)

    botonProveedor = Button(
        labelFrameProveedor, text="Guardar", command=guardarProveedor)
    botonProveedor.place(x=100, y=490)

    botonProveedor = Button(labelFrameProveedor, text="Limpiar",
                        command=vaciarEntryProveedor)
    botonProveedor.place(x=25, y=490)

    botonProveedor = Button(
        labelFrameProveedor, text="Modificar", command=modificarProveedor)
    botonProveedor.place(x=175, y=490)
    
    botonProveedor = Button(
        labelFrameProveedor, text="Borrar", command=borrarProveedor)
    botonProveedor.place(x=260, y=490)

    # Buscar proveedor en grid:

    def BuscarProveedorCiut():
        datosCuit = ("%"+entryBuscarProveedor.get()+"%",)
        if (vacios(datosCuit)):
            tabla = conexion.cursor()
            sql = "SELECT * FROM Proveedores WHERE cuitProveedor LIKE ?"
            tabla.execute(sql, datosCuit)
            datosProveedor = tabla.fetchall()
            if(len(datosProveedor) > 0):
                vaciarEntryProveedor()
                for dato in datosProveedor:
                    entryIdProveedor.config(state="normal")
                    entryIdProveedor.insert(END, dato["idProveedor"])
                    entryIdProveedor.config(state="readonly")
                    entryRSocialProveedor.insert(END, dato["razonSocialProveedor"])
                    entryCuitProveedor.insert(END, dato["cuitProveedor"])
                    entryCuitProveedor.config(state="disabled")
                    entryDireccionProveedor.insert(END, dato["direccionProveedor"])
                    entryLocalidadProveedor.insert(END, dato["localidadProveedor"])
                    entryProvinciaProveedor.insert(END, dato["provinciaProveedor"])
                    entryCPProveedor.insert(END, dato["codigoPostalProveedor"])
                    entryTelefonoProveedor.insert(END, dato["telefonoProveedor"])
                    entryIvaProveedor.insert(END, dato["ivaProveedor"])
                    mb.showwarning("Sistema", "Busqueda Completada")
            else:
                mb.showwarning("Sistema", "El dato ingresado no existe")
                vaciarEntryProveedor()
        else:
            mb.showwarning("Sistema", "Debe ingresar el C.U.I.T")

    labelFrameProveedor = LabelFrame(p4, text="Buscar Proveedores")
    labelFrameProveedor.config(width=2450//4, height=1100//2)
    labelFrameProveedor.place(x=380, y=10)

    tablaListarProveedor = ttk.Treeview(labelFrameProveedor, columns=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
    tablaListarProveedor.column("#0", width=2)

    tablaListarProveedor.column("col1", width=33, anchor=CENTER)
    tablaListarProveedor.column("col2", width=33, anchor=CENTER)
    tablaListarProveedor.column("col3", width=33, anchor=CENTER)
    tablaListarProveedor.column("col4", width=33, anchor=CENTER)
    tablaListarProveedor.column("col5", width=33, anchor=CENTER)
    tablaListarProveedor.column("col6", width=20, anchor=CENTER)
    tablaListarProveedor.column("col7", width=33, anchor=CENTER)
    tablaListarProveedor.column("col8", width=7, anchor=CENTER)

    tablaListarProveedor.heading("#0", text="ID", anchor=CENTER)
    tablaListarProveedor.heading("col1", text="Razon Social", anchor=CENTER)
    tablaListarProveedor.heading("col2", text="CUIT", anchor=CENTER)
    tablaListarProveedor.heading("col3", text="Dirección", anchor=CENTER)
    tablaListarProveedor.heading("col4", text="Localidad", anchor=CENTER)
    tablaListarProveedor.heading("col5", text="Provincia", anchor=CENTER)
    tablaListarProveedor.heading("col6", text="CP", anchor=CENTER)
    tablaListarProveedor.heading("col7", text="Teléfono", anchor=CENTER)
    tablaListarProveedor.heading("col8", text="I.V.A", anchor=CENTER)

    tablaListarProveedor.place(x=4, y=10, width=600, height=250)

    def infoProovedor(evento):
        index= tablaListarProveedor.item(tablaListarProveedor.selection())['text']
        detalles=tablaListarProveedor.item(tablaListarProveedor.selection())['values']
        rSocial=f"{detalles[0]}"
        cuit=f"{detalles[1]}"
        direccion=f"{detalles[2]}"
        localidad=f"{detalles[3]}"
        provincia=f"{detalles[4]}"
        cPostal=f"{detalles[5]}"
        telefono=f"{detalles[6]}"
        iva=f"{detalles[7]}"
        entryIdProveedor.config(state="normal")
        entryRSocialProveedor.config(state="normal")
        entryIdProveedor.delete(0,END)
        entryIdProveedor.insert(END,index)
        entryRSocialProveedor.delete(0,END)
        entryRSocialProveedor.insert(END,rSocial)
        entryCuitProveedor.delete(0,END)
        entryCuitProveedor.insert(END,cuit)
        entryDireccionProveedor.delete(0,END)
        entryDireccionProveedor.insert(END,direccion)
        entryLocalidadProveedor.delete(0,END)
        entryLocalidadProveedor.insert(END,localidad)
        entryProvinciaProveedor.delete(0,END)
        entryProvinciaProveedor.insert(END,provincia)
        entryCPProveedor.delete(0,END)
        entryCPProveedor.insert(END,cPostal)
        entryTelefonoProveedor.delete(0,END)
        entryTelefonoProveedor.insert(END,telefono)
        entryIvaProveedor.delete(0,END)
        entryIvaProveedor.insert(END,iva)
        entryIdProveedor.config(state="readonly")
        entryRSocialProveedor.config(state="normal")
    tablaListarProveedor.bind("<<TreeviewSelect>>",infoProovedor)

    # Buscar Proveedor con ciut
    labelBuscarProveedor = Label(labelFrameProveedor, text="CUIT:")
    labelBuscarProveedor.place(x=4, y=400)
    entryBuscarProveedor = Entry(labelFrameProveedor, width=33)
    entryBuscarProveedor.place(x=50, y=400)
    botonBuscarProveedor = Button(
    labelFrameProveedor, text="Buscar", command=BuscarProveedorCiut)
    botonBuscarProveedor.place(x=300, y=400)

    botonListarProveedor = Button(
    labelFrameProveedor, text="Listar", command=listarProveedor)
    botonListarProveedor.place(x=400, y=400)

    '''entryBuscarPorNombre = Entry(labelFrameProveedor, width=33)
    entryBuscarPorNombre.place(x=50, y=300)

    def buscarPorNombre(evento):
        buscar = ("%"+entryBuscarPorNombre.get()+"%",
                "%"+entryBuscarPorNombre.get()+"%",)
        tabla = conexion.cursor()
        tabla.execute(
            "SELECT * FROM Proveedores WHERE razonSocialProveedor LIKE ? OR cuitProveedor LIKE ?", buscar)
        datosListar = tabla.fetchall()
        for filas in tablaListarProveedor.get_children():
            tablaListarProveedor.delete(filas)
        for dato in datosListar:
            tablaListarProveedor.insert("", END, text=dato["idProveedor"], values=(dato["razonSocialProveedor"], dato["cuitProveedor"], dato["direccionProveedor"],
                                    dato["localidadProveedor"], dato["provinciaProveedor"], dato["codigoPostalProveedor"], dato["telefonoProveedor"], dato["ivaProveedor"]))

    entryBuscarPorNombre.bind("<Key>", buscarPorNombre)'''

    ########################################

    # Funcion de modo oscuro
    def switch():
        global esDia
        # determina si es dia o noche
        if esDia:
            modoOscuro()
            diaBoton.config(image=noche)
            esDia = False
        else:
            modoDia()
            diaBoton.config(image=dia)
            esDia = True
            

    # Imagenes del modo oscuro
    dia = PhotoImage(file="image/mododia.png")
    noche = PhotoImage(file="image/modonoche.png")

    # Boton del modo oscuro
    diaBoton = Button(labelFrameCliente, image=dia,bd=0,command=switch)
    diaBoton.place(x=450,y=450)
    

    #Pestaña Compra #######################################################################

    #Treeview de compra--------------------
    
    labelFrameCompra = LabelFrame(p1, text="Listado de articulos")
    labelFrameCompra.config(width=3900//4, height=1100//2)
    labelFrameCompra.place(x=10, y=10)
    
    tablaListarCompra = ttk.Treeview(labelFrameCompra, columns=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
    tablaListarCompra.column("#0", width=2)

    tablaListarCompra.column("col1", width=33, anchor=CENTER)
    tablaListarCompra.column("col2", width=33, anchor=CENTER)
    tablaListarCompra.column("col3", width=33, anchor=CENTER)
    tablaListarCompra.column("col4", width=33, anchor=CENTER)
    tablaListarCompra.column("col5", width=33, anchor=CENTER)
    tablaListarCompra.column("col6", width=20, anchor=CENTER)
    tablaListarCompra.column("col7", width=20, anchor=CENTER)
    tablaListarCompra.column("col8", width=20, anchor=CENTER)
    
    tablaListarCompra.heading("#0", text="ID", anchor=CENTER)
    tablaListarCompra.heading("col1", text="Marca", anchor=CENTER)
    tablaListarCompra.heading("col2", text="Modelo", anchor=CENTER)
    tablaListarCompra.heading("col3", text="EAN", anchor=CENTER)
    tablaListarCompra.heading("col4", text="Precio", anchor=CENTER)
    tablaListarCompra.heading("col5", text="Cantidad", anchor=CENTER)
    tablaListarCompra.heading("col6", text="Subtotal", anchor=CENTER)
    tablaListarCompra.heading("col7", text="I.V.A", anchor=CENTER)
    tablaListarCompra.heading("col8", text="Total", anchor=CENTER)
    
    tablaListarCompra.place(x=4, y=10, width=960, height=300)
    
    def deleteArticuloCompra():
        selected_item = tablaListarCompra.selection()[0]
        tablaListarCompra.delete(selected_item)
        
    def borrarTodoArticuloCompra():
        x = tablaListarCompra.get_children()
        for item in x:
            tablaListarCompra.delete(item)
    
    def carritoCompra():
        global ventanaAgregar
        def cerrarTop():
            global ventanaAgregar
            ventanaAgregar.destroy()
            ventanaAgregar = None
        if ventanaAgregar == None:
            ventanaAgregar = Toplevel()
            ancho = ventanaAgregar.winfo_screenwidth()
            largo = ventanaAgregar.winfo_screenheight()
            x = (ancho // 2) - (1000//2)
            y = (largo // 2) - (700//2)
            ventanaAgregar.geometry(f"{600}x{630}+{x}+{y}")
            ventanaAgregar.resizable(0,0)
            ventanaAgregar.title("Compra de articulos")
            
            def listarArticulosCompra():
                borrarListarArticulos()
                tabla = conexion.cursor()
                sql = "SELECT codigoArticulo,marcaArticulo,modeloArticulo,EAN,categoriaArticulo,stockArticulo,precioCosto,precioVenta FROM Articulos"
                tabla.execute(sql)
                datosListar = tabla.fetchall()
                tabla.close()
                for dato in datosListar:
                    tablaListarCarritoCompra.insert("", END, text=dato["codigoArticulo"], values=(dato["marcaArticulo"], 
                                            dato["modeloArticulo"],dato["EAN"]))
            
            labelFrameCarritoCompra = ttk.Labelframe(ventanaAgregar, text="Compra")
            labelFrameCarritoCompra.config(width=1150//2, height=1200//2)
            labelFrameCarritoCompra.place(x=10,y=10)
            
            tablaListarCarritoCompra = ttk.Treeview(labelFrameCarritoCompra, columns=(
                                            "col1", "col2", "col3"))
            tablaListarCarritoCompra.column("#0", width=15)

            tablaListarCarritoCompra.column("col1", width=33, anchor=CENTER)
            tablaListarCarritoCompra.column("col2", width=33, anchor=CENTER)
            tablaListarCarritoCompra.column("col3", width=33, anchor=CENTER)
                        
            tablaListarCarritoCompra.heading("#0", text="ID", anchor=CENTER)
            tablaListarCarritoCompra.heading("col1", text="Marca", anchor=CENTER)
            tablaListarCarritoCompra.heading("col2", text="Modelo", anchor=CENTER)
            tablaListarCarritoCompra.heading("col3", text="EAN", anchor=CENTER)
            
            tablaListarCarritoCompra.place(x=4, y=10, width=550, height=250)
            
            labelCodigoCompra = Label(ventanaAgregar, text="Código: ")
            labelCodigoCompra.place(x=30, y=300)
            entryCodigoCompra = Entry(ventanaAgregar, width=33)
            entryCodigoCompra.place(x=120, y=300)
            
            labelMarcaCompra = Label(ventanaAgregar, text="Marca: ")
            labelMarcaCompra.place(x=30, y=340)
            entryMarcaCompra = Entry(ventanaAgregar, width=33)
            entryMarcaCompra.place(x=120, y=340)
            
            labelModeloCompra = Label(ventanaAgregar, text="Modelo: ")
            labelModeloCompra.place(x=30, y=380)
            entryModeloCompra = Entry(ventanaAgregar, width=33)
            entryModeloCompra.place(x=120, y=380)
            
            labelEanCompra = Label(ventanaAgregar, text="EAN: ")
            labelEanCompra.place(x=30, y=420)
            entryEanCompra = Entry(ventanaAgregar, width=33)
            entryEanCompra.place(x=120, y=420)
            
            labelCantidadCompra = Label(ventanaAgregar, text="Cantidad: ")
            labelCantidadCompra.place(x=30, y=460)
            entryCantidadCompra = Entry(ventanaAgregar, width=33)
            entryCantidadCompra.place(x=120, y=460)
            
            labelPrecioCompra = Label(ventanaAgregar, text="Precio: ")
            labelPrecioCompra.place(x=30, y=500)
            entryPrecioCompra = Entry(ventanaAgregar, width=33)
            entryPrecioCompra.place(x=120, y=500)
            
            labelIvaCompra = Label(ventanaAgregar, text="I.V.A: ")
            labelIvaCompra.place(x=30, y=540)
            entryIvaCompra = Entry(ventanaAgregar, width=33)
            entryIvaCompra.place(x=120, y=540)
            
            def vaciarIngresarArticulo():
                entryCodigoCompra.config(state="readonly")
                entryMarcaCompra.config(state="readonly")
                entryModeloCompra.config(state="readonly")
                entryEanCompra.config(state="readonly")
            
            def ingresarArticulo():
                entryCodigoCompra.config(state="normal")
                entryMarcaCompra.config(state="normal")
                entryModeloCompra.config(state="normal")
                entryEanCompra.config(state="normal")
                codigoArt = entryCodigoCompra.get()
                marca= entryMarcaCompra.get()
                modelo= entryModeloCompra.get()
                ean= entryEanCompra.get()
                cantidad= entryCantidadCompra.get()
                if (soloNumeros(cantidad)):
                    precioUnitario=(entryPrecioCompra.get())
                    if (soloFloat(precioUnitario)):
                        subtotal = float(precioUnitario)*int(cantidad)
                        iva = (int(entryIvaCompra.get())*float(subtotal))/100
                        if (soloFloat(iva)):
                            total = subtotal+float(iva)
                            tablaListarCompra.insert("",END,text=codigoArt,values=(marca,modelo,ean,"$"+str(precioUnitario),cantidad,subtotal,iva,total))
                            vaciarIngresarArticulo()
                            datos = [codigoArt,
                                    marca,
                                    modelo,
                                    precioUnitario,
                                    cantidad,
                                    subtotal,
                                    iva,
                                    total,
                                    ean]
                            listadoCompras.append(datos)
                        else:
                            vaciarIngresarArticulo()
                            mb.showwarning("Ozono","Ingrese solo números.")
                    else:
                        vaciarIngresarArticulo()
                        mb.showwarning("Ozono","Ingrese solo números.")
                else:
                    vaciarIngresarArticulo()
                    mb.showwarning("Ozono","Ingrese solo números.")
            botonIngresarArticulo = Button(ventanaAgregar,text="Ingresar Articulo",command=ingresarArticulo)
            botonIngresarArticulo.place(x=180,y=580)
            
            botonListarArticulos = Button(
            ventanaAgregar, text="Listar", command=listarArticulosCompra)
            botonListarArticulos.place(x=110, y=580)
            
            def infoCompraArticulo(evento):
                index= tablaListarCarritoCompra.item(tablaListarCarritoCompra.selection())['text']
                detalles=tablaListarCarritoCompra.item(tablaListarCarritoCompra.selection())['values']
                marca=f"{detalles[0]}"
                modelo=f"{detalles[1]}"
                ean=f"{detalles[2]}"
                entryCodigoCompra.config(state="normal")
                entryMarcaCompra.config(state="normal")
                entryModeloCompra.config(state="normal")
                entryEanCompra.config(state="normal")
                entryCodigoCompra.delete(0,END)
                entryCodigoCompra.insert(END,index)
                entryMarcaCompra.delete(0,END)
                entryMarcaCompra.insert(END,marca)
                entryModeloCompra.delete(0,END)
                entryModeloCompra.insert(END,modelo)
                entryEanCompra.delete(0,END)
                entryEanCompra.insert(END,ean)
                entryCantidadCompra.delete(0,END)
                entryCodigoCompra.config(state="readonly")
                entryMarcaCompra.config(state="readonly")
                entryModeloCompra.config(state="readonly")
                entryEanCompra.config(state="readonly")
            tablaListarCarritoCompra.bind("<<TreeviewSelect>>",infoCompraArticulo)
            
            ventanaAgregar.protocol("WM_DELETE_WINDOW",cerrarTop)
    botonAgregarArticulos = Button(p1,text="Agregar articulos",command=carritoCompra)
    botonAgregarArticulos.place(x=350,y=350)
        
    def ComprarArticulo():
        total = 0
        iva = 0
        for articulo in listadoCompras:
            total = total + articulo[7]
            iva = iva + float(articulo[6])
        fecha = date.today()
        fechaCompra = fecha.strftime("%d-%m-%Y")
        datos = (fechaCompra,total)
        conexion = conectarBD()
        tabla = conexion.cursor()
        sqlGuardar= "INSERT INTO Compra(fechaCompra,totalCompra) VALUES(?,?)"
        tabla.execute(sqlGuardar,datos)
        conexion.commit()
        sqlMax = "SELECT MAX(numeroCompra) FROM Compra"
        tabla.execute(sqlMax)
        datosBuscados = tabla.fetchall()
        ultimaCompra = datosBuscados[0][0]
        for articulo in listadoCompras:
            cantidadNueva = int(articulo[4])
            idArticulo = (articulo[0],)
            tabla.execute("SELECT stockArticulo FROM Articulos WHERE codigoArticulo=?",idArticulo)
            stockArticulo = tabla.fetchall()
            nuevoStock = stockArticulo[0][0] + cantidadNueva
            actualizarStock = (nuevoStock,articulo[0])
            sql= "UPDATE Articulos SET stockArticulo=? WHERE codigoArticulo=?"
            tabla.execute(sql,actualizarStock)
            conexion.commit()
            datosArticulos=(ultimaCompra,articulo[0],articulo[5])
            tabla.execute("INSERT INTO articulosCompras(numeroCompra,idArticulo,total) VALUES(?,?,?)",datosArticulos)
            conexion.commit()
        tabla.close()
        conexion.close()
        fecha = date.today()
        hora = datetime.now()
        fechaTicket = fecha.strftime("%d-%m-%Y")
        horaTicket = hora.strftime("%H%M%S")
        nombreArchivo = f"Tickets/Compra/Ticket {fechaTicket} {horaTicket}.txt"
        escribir = open(nombreArchivo,"w")
        escribir.write("Ozono")
        escribir.write("\n")
        escribir.write("Ticket de Compra \n")
        
        escribir.write("Fecha: "+ fechaTicket)
        escribir.write("\n")
        escribir.write("***************************************")
        escribir.write("\n")
        for articulo in listadoCompras:
            auxPrint1 = f"{articulo[4]}u.  x   ${articulo[3]}\n"
            auxPrint2 = f"{articulo[1]} {articulo[2]}\n"
            auxPrint3 = f"{articulo[8]}                 "
            auxPrint4 = f"${articulo[7]}\n\n"
            escribir.write(auxPrint1)
            escribir.write(auxPrint2)
            escribir.write(auxPrint3)
            escribir.write(auxPrint4)
        escribir.write("\n\n")
        escribir.write(f"Iva:       {iva}")
        escribir.write("\n")
        escribir.write(f"Total:     {total}")
        mb.showinfo("Ozono","Se ha realizado la compra correctamente!")
        escribir.close()
        
    
    botonAgregarArticulos = Button(p1,text="Comprar",command=ComprarArticulo)
    botonAgregarArticulos.place(x=500,y=350)
    
    botonBorrarArticuloCompra = Button(p1,text="Borrar articulo",command=deleteArticuloCompra)
    botonBorrarArticuloCompra.place(x=650,y=350)
    
    botonBorrarTodoArticuloCompra = Button(p1,text="Borrar Todo",command=borrarTodoArticuloCompra)
    botonBorrarTodoArticuloCompra.place(x=800,y=350)
        
        
    #Pestaña Venta *******************************************************************************
    
    labelFrameVenta = LabelFrame(p2, text="Listado de articulos")
    labelFrameVenta.config(width=3900//4, height=1100//2)
    labelFrameVenta.place(x=10, y=10)

    tablaListarVenta = ttk.Treeview(labelFrameVenta, columns=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
    tablaListarVenta.column("#0", width=2)

    tablaListarVenta.column("col1", width=33, anchor=CENTER)
    tablaListarVenta.column("col2", width=33, anchor=CENTER)
    tablaListarVenta.column("col3", width=33, anchor=CENTER)
    tablaListarVenta.column("col4", width=33, anchor=CENTER)
    tablaListarVenta.column("col5", width=33, anchor=CENTER)
    tablaListarVenta.column("col6", width=20, anchor=CENTER)
    tablaListarVenta.column("col7", width=20, anchor=CENTER)
    tablaListarVenta.column("col8", width=20, anchor=CENTER)

    tablaListarVenta.heading("#0", text="ID", anchor=CENTER)
    tablaListarVenta.heading("col1", text="Marca", anchor=CENTER)
    tablaListarVenta.heading("col2", text="Modelo", anchor=CENTER)
    tablaListarVenta.heading("col3", text="EAN", anchor=CENTER)
    tablaListarVenta.heading("col4", text="Precio", anchor=CENTER)
    tablaListarVenta.heading("col5", text="Cantidad", anchor=CENTER)
    tablaListarVenta.heading("col6", text="Subtotal", anchor=CENTER)
    tablaListarVenta.heading("col7", text="I.V.A", anchor=CENTER)
    tablaListarVenta.heading("col8", text="Total", anchor=CENTER)

    tablaListarVenta.place(x=4, y=10, width=960, height=300)

    def deleteArticuloVenta():
        selected_item = tablaListarVenta.selection()[0]
        tablaListarVenta.delete(selected_item)

    def borrarTodoArticuloVenta():
        x = tablaListarVenta.get_children()
        for item in x:
            tablaListarVenta.delete(item)

    def carritoVenta():
        global ventanaVenta
        def cerrarTopVenta():
            global ventanaVenta
            ventanaVenta.destroy()
            ventanaVenta = None
        if ventanaVenta == None:
            ventanaVenta = Toplevel()
            ancho = ventanaVenta.winfo_screenwidth()
            largo = ventanaVenta.winfo_screenheight()
            x = (ancho // 2) - (1000//2)
            y = (largo // 2) - (700//2)
            ventanaVenta.geometry(f"{600}x{630}+{x}+{y}")
            ventanaVenta.resizable(0,0)
            ventanaVenta.title("Venta de articulos")
            
            def listarArticulosVenta():
                borrarListarArticulos()
                tabla = conexion.cursor()
                sql = "SELECT * FROM Articulos"
                tabla.execute(sql)
                datosListar = tabla.fetchall()
                tabla.close()
                for dato in datosListar:
                    tablaListarCarritoVenta.insert("", END, text=dato["codigoArticulo"], values=(dato["marcaArticulo"], 
                                            dato["modeloArticulo"],dato["EAN"],dato["precioVenta"]))
            
            labelFrameCarritoVenta = ttk.Labelframe(ventanaVenta, text="Venta")
            labelFrameCarritoVenta.config(width=1150//2, height=1200//2)
            labelFrameCarritoVenta.place(x=10,y=10)
            
            tablaListarCarritoVenta = ttk.Treeview(labelFrameCarritoVenta, columns=(
                                            "col1", "col2", "col3","col4"))
            tablaListarCarritoVenta.column("#0", width=15)

            tablaListarCarritoVenta.column("col1", width=33, anchor=CENTER)
            tablaListarCarritoVenta.column("col2", width=33, anchor=CENTER)
            tablaListarCarritoVenta.column("col3", width=33, anchor=CENTER)
            tablaListarCarritoVenta.column("col4", width=33, anchor=CENTER)
                        
            tablaListarCarritoVenta.heading("#0", text="ID", anchor=CENTER)
            tablaListarCarritoVenta.heading("col1", text="Marca", anchor=CENTER)
            tablaListarCarritoVenta.heading("col2", text="Modelo", anchor=CENTER)
            tablaListarCarritoVenta.heading("col3", text="EAN", anchor=CENTER)
            tablaListarCarritoVenta.heading("col4", text="Precio", anchor=CENTER)
            
            tablaListarCarritoVenta.place(x=4, y=10, width=550, height=250)
            
            labelCodigoVenta = Label(ventanaVenta, text="Código: ")
            labelCodigoVenta.place(x=30, y=300)
            entryCodigoVenta = Entry(ventanaVenta, width=33)
            entryCodigoVenta.place(x=120, y=300)
            
            labelMarcaVenta = Label(ventanaVenta, text="Marca: ")
            labelMarcaVenta.place(x=30, y=340)
            entryMarcaVenta = Entry(ventanaVenta, width=33)
            entryMarcaVenta.place(x=120, y=340)
            
            labelModeloVenta = Label(ventanaVenta, text="Modelo: ")
            labelModeloVenta.place(x=30, y=380)
            entryModeloVenta = Entry(ventanaVenta, width=33)
            entryModeloVenta.place(x=120, y=380)
            
            labelEanVenta = Label(ventanaVenta, text="EAN: ")
            labelEanVenta.place(x=30, y=420)
            entryEanVenta = Entry(ventanaVenta, width=33)
            entryEanVenta.place(x=120, y=420)
            
            labelPrecioVenta = Label(ventanaVenta, text="Precio: ")
            labelPrecioVenta.place(x=30, y=460)
            entryPrecioVenta = Entry(ventanaVenta, width=33)
            entryPrecioVenta.place(x=120, y=460)
            
            labelCantidadVenta = Label(ventanaVenta, text="Cantidad: ")
            labelCantidadVenta.place(x=30, y=500)
            entryCantidadVenta = Entry(ventanaVenta, width=33)
            entryCantidadVenta.place(x=120, y=500)
                        
            def ingresarArticuloVenta():
                entryCodigoVenta.config(state="normal")
                entryMarcaVenta.config(state="normal")
                entryModeloVenta.config(state="normal")
                entryEanVenta.config(state="normal")
                entryPrecioVenta.config(state="normal")
                codigoArt = entryCodigoVenta.get()
                marca = entryMarcaVenta.get()
                modelo = entryModeloVenta.get()
                ean = entryEanVenta.get()
                precioVenta = entryPrecioVenta.get()
                cantidad = entryCantidadVenta.get()
                if (soloNumeros(cantidad) and soloFloat(precioVenta)):
                    subtotal = float(entryPrecioVenta.get())*int(cantidad)
                    iva = subtotal * 0.21
                    if (soloFloat(iva)):
                        total = subtotal + iva
                        tablaListarVenta.insert("",END,text=codigoArt,values=(marca,modelo,ean,"$"+str(precioVenta),cantidad,subtotal,iva,total))
                        entryCodigoVenta.config(state="readonly")
                        entryMarcaVenta.config(state="readonly")
                        entryModeloVenta.config(state="readonly")
                        entryEanVenta.config(state="readonly")
                        entryPrecioVenta.config(state="readonly")
                        datos = [codigoArt,
                            marca,
                            modelo,
                            precioVenta,
                            cantidad,
                            subtotal,
                            iva,
                            total,
                            ean]
                        listadoVentas.append(datos)
                    else:
                        mb.showwarning("Ozono","Ingrese solo números.")
                else:
                    entryCodigoVenta.config(state="readonly")
                    entryMarcaVenta.config(state="readonly")
                    entryModeloVenta.config(state="readonly")
                    entryEanVenta.config(state="readonly")
                    entryPrecioVenta.config(state="readonly")
                    mb.showwarning("Ozono","Ingrese solo números.")
            
            botonIngresarArticulo = Button(ventanaVenta,text="Ingresar Articulo",command=ingresarArticuloVenta)
            botonIngresarArticulo.place(x=180,y=580)
            
            botonListarArticulos = Button(
            ventanaVenta, text="Listar", command=listarArticulosVenta)
            botonListarArticulos.place(x=110, y=580)
            
            def infoVentaArticulo(evento):
                index= tablaListarCarritoVenta.item(tablaListarCarritoVenta.selection())['text']
                detalles=tablaListarCarritoVenta.item(tablaListarCarritoVenta.selection())['values']
                marca=f"{detalles[0]}"
                modelo=f"{detalles[1]}"
                ean=f"{detalles[2]}"
                precio=f"{detalles[3]}"
                entryCodigoVenta.config(state="normal")
                entryMarcaVenta.config(state="normal")
                entryModeloVenta.config(state="normal")
                entryEanVenta.config(state="normal")
                entryPrecioVenta.config(state="normal")
                entryCodigoVenta.delete(0,END)
                entryCodigoVenta.insert(END,index)
                entryMarcaVenta.delete(0,END)
                entryMarcaVenta.insert(END,marca)
                entryModeloVenta.delete(0,END)
                entryModeloVenta.insert(END,modelo)
                entryEanVenta.delete(0,END)
                entryEanVenta.insert(END,ean)
                entryPrecioVenta.delete(0,END)
                entryPrecioVenta.insert(END,precio)
                entryCantidadVenta.delete(0,END)
                entryCodigoVenta.config(state="readonly")
                entryMarcaVenta.config(state="readonly")
                entryModeloVenta.config(state="readonly")
                entryEanVenta.config(state="readonly")
                entryPrecioVenta.config(state="readonly")
            tablaListarCarritoVenta.bind("<<TreeviewSelect>>",infoVentaArticulo)
            
                    
            ventanaVenta.protocol("WM_DELETE_WINDOW",cerrarTopVenta)
    botonAgregarArticulos = Button(p2,text="Agregar articulos",command=carritoVenta)
    botonAgregarArticulos.place(x=350,y=350)
        
    def VenderArticulo():
        total = 0
        iva = 0
        subtotal = 0
        for articulo in listadoVentas:
            subtotal = subtotal + articulo[5]
            total = total + articulo[7]
            iva = iva + float(articulo[6])
        fecha = date.today()
        fechaVenta = fecha.strftime("%d-%m-%Y")
        datos = (fechaVenta,subtotal,iva,total)
        conexion = conectarBD()
        tabla = conexion.cursor()
        sqlGuardar= "INSERT INTO Venta(fechaVenta,subtotalVenta,ivaVenta,totalVenta) VALUES(?,?,?,?)"
        tabla.execute(sqlGuardar,datos)
        conexion.commit()
        sqlMax = "SELECT MAX(numeroVenta) FROM Venta"
        tabla.execute(sqlMax)
        datosBuscados = tabla.fetchall()
        ultimaVenta = datosBuscados[0][0]
        for articulo in listadoVentas:
            cantidadNueva = int(articulo[4])
            idArticulo = (articulo[0],)
            tabla.execute("SELECT stockArticulo FROM Articulos WHERE codigoArticulo=?",idArticulo)
            stockArticulo = tabla.fetchall()
            nuevoStock = stockArticulo[0][0] - cantidadNueva
            actualizarStock = (nuevoStock,articulo[0])
            sql= "UPDATE Articulos SET stockArticulo=? WHERE codigoArticulo=?"
            tabla.execute(sql,actualizarStock)
            conexion.commit()
            datosArticulos=(ultimaVenta,articulo[0],articulo[4],articulo[5],articulo[6],articulo[7])
            tabla.execute("INSERT INTO articulosVentas(numeroVenta,codigoArticulo,cantidadArticulo,subtotalArticulo,ivaArticulo,totalArticulo) VALUES(?,?,?,?,?,?)",datosArticulos)
            conexion.commit()
        tabla.close()
        conexion.close()
        fecha = date.today()
        hora = datetime.now()
        fechaTicket = fecha.strftime("%d-%m-%Y")
        horaTicket = hora.strftime("%H%M%S")
        nombreArchivo = f"Tickets/Venta/Ticket {fechaTicket} {horaTicket}.txt"
        escribir = open(nombreArchivo,"w")
        escribir.write("Ozono")
        escribir.write("\n")
        escribir.write("Ticket de venta \n")
        
        escribir.write("Fecha: "+ fechaTicket)
        escribir.write("\n")
        escribir.write("***************************************")
        escribir.write("\n")
        for articulo in listadoVentas:
            auxPrint1 = f"{articulo[4]}u.  x   ${articulo[3]}\n"
            auxPrint2 = f"{articulo[1]} {articulo[2]}\n"
            auxPrint3 = f"{articulo[8]}                 "
            auxPrint4 = f"${articulo[7]}\n\n"
            escribir.write(auxPrint1)
            escribir.write(auxPrint2)
            escribir.write(auxPrint3)
            escribir.write(auxPrint4)
        escribir.write("\n\n")
        escribir.write(f"Iva:                       {iva}")
        escribir.write("\n")
        escribir.write(f"Sub-Total:                 {subtotal}")
        escribir.write("\n")
        escribir.write(f"Total:                     {total}")
        escribir.write("\n")
        escribir.write("\n")
        escribir.write("***************************************")
        escribir.write("\n")
        escribir.write("Defensa del consumidor 08002226678")
        escribir.write("\n")
        escribir.write("        MUCHAS GRACIAS")
        mb.showinfo("Ozono","Se ha realizado la venta correctamente!")
        escribir.close()
        

    botonAgregarArticulos = Button(p2,text="Vender",command=VenderArticulo)
    botonAgregarArticulos.place(x=500,y=350)
    
    botonBorrarArticuloVenta = Button(p2,text="Borrar articulo",command=deleteArticuloVenta)
    botonBorrarArticuloVenta.place(x=650,y=350)
    
    botonBorrarTodoArticuloVenta = Button(p2,text="Borrar Todo",command=borrarTodoArticuloVenta)
    botonBorrarTodoArticuloVenta.place(x=800,y=350)
    
    # Buscar Articulo en grid:

    #Pestaña articulo ****************************************************************************
    
    def vaciarEntryArticulos():
        entryIdArticulos.config(state="normal")
        entryEanArticulos.config(state="normal")
        entryIdArticulos.delete(0, END)
        entryMarcaArticulos.delete(0, END)
        entryModeloArticulos.config(state="normal")
        entryModeloArticulos.delete(0, END)
        entryEanArticulos.delete(0, END)
        comboCategoriaArticulos.delete(0, END)
        entryStockArticulos.delete(0, END)
        entryPrecioCostoArticulos.delete(0, END)
        entryPrecioVentaArticulos.delete(0, END)

    def listarArticulos():
        borrarListarArticulos()
        tabla = conexion.cursor()
        sql = "SELECT codigoArticulo,marcaArticulo,modeloArticulo,EAN,categoriaArticulo,stockArticulo,precioCosto,precioVenta FROM Articulos"
        tabla.execute(sql)
        datosListar = tabla.fetchall()
        tabla.close()
        for dato in datosListar:
            tablaListarArticulos.insert("", END, text=dato["codigoArticulo"], values=(dato["marcaArticulo"], 
                                    dato["modeloArticulo"],dato["EAN"],dato["categoriaArticulo"],dato["stockArticulo"], 
                                    dato["precioCosto"], dato["precioVenta"]))
        

    def modificarArticulos():
        entryIdArticulos.config(state="normal")
        datosArticulos = (entryMarcaArticulos.get(), 
                        entryModeloArticulos.get(),
                        entryEanArticulos.get(), 
                        comboCategoriaArticulos.get(), 
                        entryStockArticulos.get(), 
                        entryPrecioCostoArticulos.get(), 
                        entryPrecioVentaArticulos.get(),
                        entryIdArticulos.get())
        entryIdArticulos.config(state="readonly")
        if(vacios(datosArticulos)):
            tabla = conexion.cursor()
            sql = "UPDATE Articulos SET marcaArticulo=?,modeloArticulo=?,EAN=?,categoriaArticulo=?,stockArticulo=?,precioCosto=?,precioVenta=? WHERE codigoArticulo=?"
            tabla.execute(sql, datosArticulos)
            conexion.commit
            tabla.close
            mb.showinfo("Sistema", "Se ha modificado correctamente")
        else:
            mb.showinfo("Sistema", "Complete todos los campos")



    def getDatoArticulos():
        datos = (entryMarcaArticulos.get(), 
                        entryModeloArticulos.get(), 
                        entryEanArticulos.get(), 
                        comboCategoriaArticulos.get(), 
                        entryStockArticulos.get(), 
                        entryPrecioCostoArticulos.get(), 
                        entryPrecioVentaArticulos.get())
        return datos

    def guardarArticulos():
        datosArticulos = getDatoArticulos()
        if (vacios(datosArticulos)):
            if (soloNumeros(datosArticulos[2]) and soloNumeros(datosArticulos[4]) and soloNumeros(datosArticulos[5]) and soloNumeros(datosArticulos[6])):
                nombreTabla = "Articulos"
                nombreCampos = "marcaArticulo,modeloArticulo,EAN,categoriaArticulo,stockArticulo,precioCosto,precioVenta"
                valores = "?,?,?,?,?,?,?"
                guardar(conexion,getDatoArticulos(),nombreTabla,nombreCampos,valores,vaciarEntryArticulos)
            else:
                mb.showwarning("Ozono","Verifique los datos ingresados")
        else:
            mb.showinfo("Ozono", "Complete todos los campos")

    labelFrameArticulos = LabelFrame(p5, text="Articulos")
    labelFrameArticulos.config(width=1440//4, height=1100//2)
    labelFrameArticulos.place(x=10, y=10)

    labelIdArticulos = Label(labelFrameArticulos, text="ID: ")
    labelIdArticulos.place(x=30, y=30)
    entryIdArticulos = Entry(labelFrameArticulos, width=33)
    entryIdArticulos.config(state="readonly")
    entryIdArticulos.place(x=120, y=30)

    labelMarcaArticulos = Label(labelFrameArticulos, text="Marca: ")
    labelMarcaArticulos.place(x=30, y=80)
    entryMarcaArticulos = Entry(labelFrameArticulos, width=33)
    entryMarcaArticulos.place(x=120, y=80)

    labelModeloArticulos = Label(labelFrameArticulos, text="Modelo: ")
    labelModeloArticulos.place(x=30, y=130)
    entryModeloArticulos = Entry(labelFrameArticulos, width=33)
    entryModeloArticulos.place(x=120, y=130)

    labelEanArticulos = Label(labelFrameArticulos, text="EAN: ")
    labelEanArticulos.place(x=30, y=180)
    entryEanArticulos = Entry(labelFrameArticulos, width=33)
    entryEanArticulos.place(x=120, y=180)

    labelCategoriaArticulos = Label(labelFrameArticulos, text="Categoria: ")
    labelCategoriaArticulos.place(x=30, y=230)
    categoria = ('Almacén','Bebidas','Perecederos','Bazar','Perfumería','Limpieza','Ferretería','Electrónica')
    comboCategoriaArticulos = ttk.Combobox(labelFrameArticulos, width=33)
    comboCategoriaArticulos['values'] = categoria
    comboCategoriaArticulos['state'] = 'readonly'
    comboCategoriaArticulos.place(x=120, y=230)
    

    labelStockArticulos = Label(labelFrameArticulos, text="Stock: ")
    labelStockArticulos.place(x=30, y=280)
    entryStockArticulos = Entry(labelFrameArticulos, width=33)
    entryStockArticulos.place(x=120, y=280)

    labelPrecioCostoArticulos = Label(labelFrameArticulos, text="Precio costo: ")
    labelPrecioCostoArticulos.place(x=30, y=330)
    entryPrecioCostoArticulos = Entry(labelFrameArticulos, width=33)
    entryPrecioCostoArticulos.place(x=120, y=330)

    labelPrecioVentaArticulos = Label(labelFrameArticulos, text="Precio venta: ")
    labelPrecioVentaArticulos.place(x=30, y=380)
    entryPrecioVentaArticulos = Entry(labelFrameArticulos, width=33)
    entryPrecioVentaArticulos.place(x=120, y=380)

    botonArticulos = Button(
        labelFrameArticulos, text="Guardar", command=guardarArticulos)
    botonArticulos.place(x=145, y=490)

    botonArticulos = Button(labelFrameArticulos, text="Limpiar",
                        command=vaciarEntryArticulos)
    botonArticulos.place(x=45, y=490)

    botonArticulos = Button(
        labelFrameArticulos, text="Modificar", command=modificarArticulos)
    botonArticulos.place(x=245, y=490)

    # Buscar Cliente en grid:

    def BuscarEanArticulos():
        datosEan = ("%"+entryBuscarArticulos.get()+"%",)
        if (vacios(datosEan)):
            tabla = conexion.cursor()
            sql = "SELECT * FROM Articulos WHERE EAN LIKE ?"
            tabla.execute(sql, datosEan)
            datosEan = tabla.fetchall()
            if(len(datosEan) > 0):
                vaciarEntryArticulos()
                for dato in datosEan:
                    entryIdArticulos.insert(END, dato["codigoArticulo"])
                    entryIdArticulos.config(state="normal")
                    entryIdArticulos.config(state="readonly")
                    entryMarcaArticulos.insert(END, dato["marcaArticulo"])
                    entryModeloArticulos.insert(END, dato["modeloArticulo"])
                    entryEanArticulos.config(state="normal")
                    entryEanArticulos.insert(END, dato["EAN"])
                    comboCategoriaArticulos.insert(END, dato["categoriaArticulo"])
                    entryStockArticulos.insert(END, dato["stockArticulo"])
                    entryPrecioCostoArticulos.insert(END, dato["precioCosto"])
                    entryPrecioVentaArticulos.insert(END, dato["precioVenta"])
                    tabla.close()
                    mb.showwarning("Sistema", "Busqueda Completada")
            else:
                mb.showwarning("Sistema", "El dato ingresado no existe")
                vaciarEntryArticulos()
        else:
            mb.showwarning("Sistema", "Debe ingresar el EAN")

    labelFrameArticulos = LabelFrame(p5, text="Buscar Articulos")
    labelFrameArticulos.config(width=2450//4, height=1100//2)
    labelFrameArticulos.place(x=380, y=10)

    tablaListarArticulos = ttk.Treeview(labelFrameArticulos, columns=(
        "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
    tablaListarArticulos.column("#0", width=2)

    tablaListarArticulos.column("col1", width=33, anchor=CENTER)
    tablaListarArticulos.column("col2", width=33, anchor=CENTER)
    tablaListarArticulos.column("col3", width=33, anchor=CENTER)
    tablaListarArticulos.column("col4", width=33, anchor=CENTER)
    tablaListarArticulos.column("col5", width=33, anchor=CENTER)
    tablaListarArticulos.column("col6", width=20, anchor=CENTER)
    tablaListarArticulos.column("col7", width=33, anchor=CENTER)

    tablaListarArticulos.heading("#0", text="ID", anchor=CENTER)
    tablaListarArticulos.heading("col1", text="Marca", anchor=CENTER)
    tablaListarArticulos.heading("col2", text="Modelo", anchor=CENTER)
    tablaListarArticulos.heading("col3", text="EAN", anchor=CENTER)
    tablaListarArticulos.heading("col4", text="Categoria", anchor=CENTER)
    tablaListarArticulos.heading("col5", text="Stock", anchor=CENTER)
    tablaListarArticulos.heading("col6", text="P. Costo", anchor=CENTER)
    tablaListarArticulos.heading("col7", text="P. Venta", anchor=CENTER)

    tablaListarArticulos.place(x=4, y=10, width=600, height=250)


    def infoArticulo(evento):
        index= tablaListarArticulos.item(tablaListarArticulos.selection())['text']
        detalles=tablaListarArticulos.item(tablaListarArticulos.selection())['values']
        marca=f"{detalles[0]}"
        modelo=f"{detalles[1]}"
        ean=f"{detalles[2]}"
        categoria=f"{detalles[3]}"
        stock=f"{detalles[4]}"
        pCosto=f"{detalles[5]}"
        pVenta=f"{detalles[6]}"
        entryIdArticulos.config(state="normal")
        entryMarcaArticulos.config(state="normal")
        entryIdArticulos.delete(0,END)
        entryIdArticulos.insert(END,index)
        entryMarcaArticulos.delete(0,END)
        entryMarcaArticulos.insert(END,marca)
        entryModeloArticulos.delete(0,END)
        entryModeloArticulos.insert(END,modelo)
        entryEanArticulos.delete(0,END)
        entryEanArticulos.insert(END,ean)
        comboCategoriaArticulos.delete(0,END)
        comboCategoriaArticulos.insert(END,categoria)
        entryStockArticulos.delete(0,END)
        entryStockArticulos.insert(END,stock)
        entryPrecioCostoArticulos.delete(0,END)
        entryPrecioCostoArticulos.insert(END,pCosto)
        entryPrecioVentaArticulos.delete(0,END)
        entryPrecioVentaArticulos.insert(END,pVenta)
        entryIdArticulos.config(state="readonly")
        entryMarcaArticulos.config(state="normal")
    tablaListarArticulos.bind("<<TreeviewSelect>>",infoArticulo)

    # Buscar clientes con ciut
    labelBuscarArticulos = Label(labelFrameArticulos, text="EAN:")
    labelBuscarArticulos.place(x=4, y=400)
    entryBuscarArticulos = Entry(labelFrameArticulos, width=33)
    entryBuscarArticulos.place(x=50, y=400)
    botonBuscarArticulos = Button(
    labelFrameArticulos, text="Buscar", command=BuscarEanArticulos)
    botonBuscarArticulos.place(x=300, y=400)

    botonListarArticulos = Button(
    labelFrameArticulos, text="Listar", command=listarArticulos)
    botonListarArticulos.place(x=400, y=400)

    entryBuscarPorMarca = Entry(labelFrameArticulos, width=33)
    entryBuscarPorMarca.place(x=50, y=300)

    def buscarPorMarca(evento):
        buscar = ("%"+entryBuscarPorMarca.get()+"%",
                "%"+entryBuscarPorMarca.get()+"%",)
        tabla = conexion.cursor()
        tabla.execute(
            "SELECT * FROM Articulos WHERE marcaArticulo LIKE ? OR modeloArticulos LIKE ?", buscar)
        datosListar = tabla.fetchall()
        for filas in tablaListarArticulos.get_children():
            tablaListarArticulos.delete(filas)
        for dato in datosListar:
            tablaListarArticulos.insert("", END, text=dato["codigoArticulo"], values=(dato["marcaArticulo"], dato["modeloArticulo"], dato["EAN"],
                                    dato["categoriaArticulo"], dato["stockArticulo"], dato["precioCosto"], dato["precioVenta"]))

    entryBuscarPorMarca.bind("<Key>", buscarPorMarca)

    # AGREGAMOS PESTAÑAS CREADAS
    nb.add(p1, text="Compra")
    nb.add(p2, text="Venta")
    nb.add(p3, text="Clientes")
    nb.add(p4, text="Proveedores")
    nb.add(p5, text="Artículos")

    '''fondo = PhotoImage(file="Resto-Vip beta/image/restaurant.png")
    labelFondo = Label(root,image=fondo)
    labelFondo.place(x=0,y=25)'''

    '''labelHora = Label(root,font=("Calibri",20),bg="black",fg="white")
    labelHora.place(x=870,y=550)'''

    # Reloj
    '''def reloj():
        global time1
        time1=""
        time2=time.strftime("%H: %M %S")
        if (time1 != time2):
            labelHora.configure(text=time2)
            labelHora.after(400,reloj)
    reloj()'''


    root1.mainloop()
global conexion
conexion = conectarBD()
if (conexion):
    ventanaLogin()
else:
    ventanaError()
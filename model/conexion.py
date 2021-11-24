import sqlite3
import os
from tkinter import messagebox as mb



def create_table():   
    conexion = sqlite3.connect("data/login.db")
    consulta = conexion.cursor()
    sql = "CREATE TABLE IF NOT EXISTS usuarios(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Nombre TEXT NOT NULL, Apellido TEXT NOT NULL,Usuario TEXT NOT NULL, Pass TEXT NOT NULL)"
    consulta.execute(sql)
    conexion.commit()
    consulta.close()
    conexion.close()

create_table()

ruta = "data"
archivo = "login.db"
baseDeDatosLogin = f"{ruta}/{archivo}"

rutaBD = "data"
archivoBD = "database.db"
baseDeDatos = f"{rutaBD}/{archivoBD}"

def conectar():
    if(os.path.isfile(baseDeDatosLogin) == True):
        global conexion
        conexion = sqlite3.connect(baseDeDatosLogin)
        conexion.row_factory = sqlite3.Row
        return conexion
    else:
        mb.showerror("Ozono","Error en la base de datos/n Contacte al administrador.")
        return False

def conectarBD():
    if(os.path.isfile(baseDeDatos) == True):
        conexion = sqlite3.connect(baseDeDatos)
        conexion.row_factory = sqlite3.Row
        return conexion
    else:
        mb.showerror("Ozono","Error en la base de datos/n Contacte al administrador.")
        return False

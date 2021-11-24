import sqlite3
from tkinter import messagebox as mb

def guardar(conexion,datos,nombreTabla,nombreCampos,valores,vaciarEntry):
    try:
        tabla = conexion.cursor()
        sql = f"INSERT INTO {nombreTabla}({nombreCampos}) VALUES({valores})"
        tabla.execute(sql, datos)
        conexion.commit()
        tabla.close()
        mb.showinfo("Ozono", "Se ha guardado correctamente")
        vaciarEntry()
    except sqlite3.IntegrityError:
        mb.showwarning("Ozono","Ya existe ese registro")

def modificar():
    pass

def buscar():
    pass

def eliminar():
    pass

def listar():
    pass
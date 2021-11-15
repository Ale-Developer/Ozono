import os
from tkinter import *


# Validaciones
def vacios(datos):
    for dato in datos:
        if (dato == ""):
            return False
    return True

def SoloLetras(datos):
    for letra in datos:
        if (ord(letra) != 32):
            if(letra.isalpha() == False):
                return False
    return True

def soloNumeros(datos):
    for numero in datos:
        if(ord(numero) != 46):
            if (numero.isdigit() == False):
                return False
    return True

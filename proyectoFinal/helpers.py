import os
import platform
import re

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    if mensaje: print(mensaje)
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        print(f"La longitud máxima permitida es {longitud_max} y la minima es {longitud_min}")
def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print('DNI incorrecto, debe cumplir el formato')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente")
            return False
    return True
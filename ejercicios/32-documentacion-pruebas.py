"""Este es el docstring del módulo"""

def hola(arg):
    """Este es el docstring de la función"""
    print("Hola", arg, "!")
    

help(hola)


class Clase:
    """Este es el docstring de la clase"""
    def __init__(self):
        """Este es el docstring del constructor de clase"""
        pass
    
    def metodo(self):
        """Este es el docstring del metodo de clase"""
        pass
    
help(__name__)
lista = [1,2,3]

def monitorizar(funcion):
    
    def decorar():
        print("\tSe está a punto de ejectuar la función: ", funcion.__name__)
        funcion()
        print("\tSe ha finalizado la ejecución de la función: ", funcion.__name__)
    return decorar
def monitorizar_args(funcion):
    
    def decorar(*args, **kwargs):
        print("\tSe está a punto de ejectuar la función con argumentos: ", funcion.__name__)
        funcion(*args, **kwargs)
        print("\tSe ha finalizado la ejecución de la función con argumentos: ", funcion.__name__)
    return decorar

@monitorizar_args
def hola(nombre):
    print(f"Hola {nombre}!")
    
@monitorizar_args
def adios(nombre):
    print(f"Adios {nombre}!")


hola("Edgar")
adios("Edgar")

    
import pickle

lista= [1,2,3,4,5]

fichero= open('lista.pckl', 'wb')

pickle.dump(lista, fichero)

fichero.close()

fichero = open('lista.pckl', 'rb')

lista = pickle.load(fichero)

print(lista)


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre
    
nombres = ["Edgar", "Carla", "Ana"]

personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)
    
fichero = open('personas.pckl', 'wb')
pickle.dump(personas, fichero)
fichero.close()
fichero = open('personas.pckl', 'rb')

personas = pickle.load(fichero)
fichero.close()

for p in personas:
    print(p)
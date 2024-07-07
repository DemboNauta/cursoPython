# def doblar(num): return num * 2

# print(doblar(2))

# doblar_lambda=(lambda num: num*2)

# print(doblar_lambda(4))

# impar = lambda num : num%2 != 0

# print(impar(6))
# print(impar(5))

# revertir = lambda cadena: cadena[::-1]

# print(revertir("Edgar"))


# numeros = [2,5,10,23,50,33]

# def multiple(numero):
#     if numero % 5 ==0:
#         return True

# f=filter(multiple, numeros)

# for numero in f:
#     print(numero)
    
# print(list(filter(lambda numero: numero%5 ==0, numeros)))


# class Persona: 
#     def __init__(self, nombre, edad):
#         self.nombre=nombre
#         self.edad=edad
        
#     def __str__(self):
#         return "{} de {} años".format(self.nombre, self.edad)
    
# personas = [
#     Persona("Edgar", 19),
#     Persona("Carla", 21),
#     Persona("Joselete", 10)
# ]

# menores= filter(lambda persona: persona.edad < 18, personas)
# mayores= filter(lambda persona: persona.edad >= 18, personas)

# for menor in menores: print(menor)
# for mayor in mayores: print(mayor)

numeros = [2,5,10,23,50,33]
def doblar(num): return num * 2

m=map(doblar, numeros)

print(list(map(lambda x: x*2, numeros)))

#Multiplicar dos listas
a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(list(map(lambda x,y: x*y, a, b)))


class Persona: 
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)
    
personas = [
    Persona("Edgar", 19),
    Persona("Carla", 21),
    Persona("Joselete", 10)
]

# def incrementar(persona):
#     persona.edad +=1
#     return persona
# personas = map(incrementar, personas)

# for persona in personas: print(persona)

personas = [
    Persona("Edgar", 19),
    Persona("Carla", 21),
    Persona("Joselete", 10)
]

personas = map(lambda persona: Persona(persona.nombre, persona.edad+1), personas)
for persona in personas: print(persona)
for persona in personas: print(persona)

numeros= [2,5,10,12,20,88]

print(list(map(lambda x: x*2, numeros)))
# menores= filter(lambda persona: persona.edad < 18, personas)

numeros = list(filter(lambda numero: numero % 5 == 0, map(lambda numero: numero/2,numeros)))
print(numeros)
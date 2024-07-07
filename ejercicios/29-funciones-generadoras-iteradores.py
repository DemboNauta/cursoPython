print([numero for numero in [0,1,2,3,4,5,6,7,8] if numero%2 ==0])
print([numero for numero in range(0,10) if numero%2 ==0])


def pares(n):
    for numero in range(n+1):
        if numero%2==0:
            yield numero
            
    
            
for numero in pares(10):
    print(numero)
    
print([numero for numero in pares(10)])


pares=pares(8)

print(next(pares))
print(next(pares))

lista = iter([7,8,9])

cadena = iter("Hola")

print(next(lista))
print(next(lista))
print(next(lista))

print(next(cadena))
print(next(cadena))
print(next(cadena))

#Ejercicio
def cuadrados(numero):
    for cuadrado in range (1,numero+1):
        yield (cuadrado, cuadrado**2)       

for numero in cuadrados(5):
    print(numero)    


    


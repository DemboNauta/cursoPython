lista = []

for letra in 'casa':
    lista.append(letra)
    
print(lista)

lista2 = [letra for letra in 'casa']

print(lista2)


lista = []

for numero in range(0,11):
    lista.append(numero**2)
print(lista)

liesta = [numero**2 for numero in range(0,11)]
print(liesta)


lista = []
for numero in range(0,11):
    if numero%2==0:
        lista.append(numero)
print(lista)

lista2 = [numero for numero in range(0,11) if numero %2 ==0]
print(lista2)

pares = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 ==0]
print(pares)

multiples = [numero for numero in range(0,501) if numero %8 == 0 and numero%3==0]
print(multiples)
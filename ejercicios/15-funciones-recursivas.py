def resta(a=None ,b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b


def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*= 2
    
ns = [10,50,100]
doblar_valores(ns)


def cuenta_atras(num):
    num -=1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooom")
    print("Fin de la función", num)    
    

def factorial(num):
    print("Valor incial ->", num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->", num)
    return num

def sumatorio(numero, total=0):
    total+=numero
    numero-=1
    if numero > 0:
        return sumatorio(numero, total)
    return total

print(sumatorio(3))
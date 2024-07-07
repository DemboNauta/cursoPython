def dividir(a, b):
    try:
        return a/b
    except:
        print("No se puede dividir entre cero")
        
print(dividir(4,2))
dividir(4,0)


def par_o_impar(numero):
    if(numero % 2 == 0):
        print("PAR")
    else:
        print("IMPAR")

par_o_impar(1)

def recortar(numero, minimo, maximo):
    if(numero < minimo):
        return minimo
    elif(numero > maximo):
        return maximo
    return numero
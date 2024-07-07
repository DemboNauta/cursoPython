matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

for posicionLinea, linea in enumerate(matriz):
    for posicionColumna, columna in enumerate(linea):
        if(matriz[posicionLinea][posicionColumna]%2==0):
            matriz[posicionLinea][posicionColumna]=0
        else:
            matriz[posicionLinea][posicionColumna]=1

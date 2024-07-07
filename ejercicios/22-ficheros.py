# texto =  "Una línea con texto\nOleeeeeeeeeeeeee"

# fichero = open('fichero.txt', 'w')

# fichero.write(texto)

# fichero.close()

# fichero = open('fichero.txt', 'r')

# linea=fichero.readline()
# print(linea)
# linea=fichero.readline()
# print(linea)
# linea=fichero.readline()
# print(linea)

# with open('fichero.txt', 'r') as fichero:
#     for linea in fichero:
#         print(linea)

# fichero = open('fichero.txt', 'r')
# fichero.seek(33)

# print(fichero.read())


# fichero.close()
# fichero = open('fichero.txt', 'r+')

# fichero.write('sidsadjsad')

# print(fichero.read())


fichero = open('fichero.txt', 'r+')

lineas = fichero.readlines()

lineas[0]="Esta la linea la he modificado en memoria\n"

fichero.seek(0)
fichero.writelines(lineas)
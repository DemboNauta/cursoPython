import re

texto = "En esta cadena se encuentra una palabra mágica"

encontrado = re.search("mágica", texto)

print(encontrado)

if encontrado is not None:
    print('Encontrado')
else:
    print('No encontrado')
    
print(encontrado.start())
print(encontrado.end())
print(encontrado.span())
print(encontrado.string)

texto = "Vamos a dividir esta cadena"

dividido=re.split(' ', texto)

print(dividido)

texto= re.sub('Vamos', 'Prueba', texto)
print(texto)

texto = "hola adios hola hola, hello, by"

holas=re.findall("(hola|hello)", texto)

print(holas)

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

texto = "hla hola hoola hoooola hooooola"
patrones= ["ho", "ho+", "ho*la", "hu*la"]

buscar(patrones, texto)
holas=re.findall("(hola|hello)", texto)

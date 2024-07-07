import json

contactos = [
    ("Edgar", "Desarrollador Web", "edgarmila_10@outlook.com"),
    ("Carla", "Educadora Social", "carla@gmail.es")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre": nombre, "empleo": empleo, "email": email})

with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)
    
datos = None

with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["email"])
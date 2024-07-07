import csv

contactos = [
    ("Edgar", "Desarrollador Web", "edgarmila_10@outlook.com"),
    ("Carla", "Educadora Social", "carla@gmail.es")
]

with open("contactos.csv", "w", newline="\n") as csvfile:
    campos=["nombre", "empleo", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for nombre, empleo, email in contactos:
        writer.writerow({
            "nombre": nombre, "empleo":empleo, "email" :email
        }) 

with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for contacto in reader:
        print(contacto['nombre'], contacto['email'])

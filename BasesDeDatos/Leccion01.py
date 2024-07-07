import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# cursor.execute("INSERT INTO usuarios VALUES('Edgar', 19, 'edgarmila_10@outlook.com')")

# cursor.execute("SELECT * FROM usuarios")
# usuario= cursor.fetchone()
# print(usuario)

# usuarios = [
#     ('Carla', 21, 'carla@gmail.com'),
#     ('Ana', 23, 'ana@gmail.com'),
#     ('Totis', 1, 'totis@gmail.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)",usuarios)

cursor.execute("SELECT * FROM usuarios")
usuarios= cursor.fetchall()
for usuario in usuarios:
    print(f"Nombre: {usuario[0]}, Edad: {usuario[1]}, Email: {usuario[2]}")
conexion.commit()
conexion.close()
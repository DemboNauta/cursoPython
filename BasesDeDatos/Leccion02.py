import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE usuarios(
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
#     ''')

# usuarios = [
#     ('04985632L','Edgar', 19,'edgarmila_10@outlook.com'),
#     ('06985478M','Carla', 21, 'carla@gmail.com'),
#     ('04723548J','Ana', 23, 'ana@gmail.com'),
#     ('04697248I','Totis', 1, 'totis@gmail.com')
# ]
# cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?)",usuarios)

# cursor.execute('''
#     CREATE TABLE productos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
#     ''')

# productos = [
#     ("Teclado", "Logitech", 19.95),
#     ("Pantalla 19'", "LG", 89.95),
# ]

# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

# cursor.execute("SELECT * FROM productos")
# productos=cursor.fetchall()

# for producto in productos:
#     print(producto)

# cursor.execute('''
#         CREATE TABLE usuarios(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             dni VARCHAR(9) UNIQUE,
#             nombre VARCHAR(100),
#             edad INTEGER,
#             email VARCHAR(100)
#         )
#     ''')

# usuarios = [
#     ('04985632L','Edgar', 19,'edgarmila_10@outlook.com'),
#     ('06985478M','Carla', 21, 'carla@gmail.com'),
#     ('04723548J','Ana', 23, 'ana@gmail.com'),
#     ('04697248I','Totis', 1, 'totis@gmail.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)

cursor.execute("INSERT INTO usuarios VALUES(null,'04985632L', 'Edgar', 19, 'edgarmila_10@outlook.com')")


conexion.commit()
conexion.close()
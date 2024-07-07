import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

usuarioId1=cursor.execute("UPDATE usuarios set edad = 23 WHERE nombre = 'Ana'")

print(usuarioId1)

conexion.commit()
conexion.close()
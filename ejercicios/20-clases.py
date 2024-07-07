class Galleta():
    chocolate = False
    def __init__(self, sabor=None, color=None):
        self.sabor = sabor
        self.color = color
        if sabor is not None and color is not None:
            print(f"Se acaba de crear una galleta con sabor {sabor} y con un color {color}")
    
    def chocolatear(self):
        self.chocolate = True
        
    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")



class Pelicula:
    
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película", self.titulo)
        
    def __del__(self):
        print("Se está borrando la película", self.titulo)
        
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)
    
    def __len__(self):
        return self.duracion
p = Pelicula("El Padrino", 175, 1972)
p2 = Pelicula("El Padrino II", 190, 1990)

class Catalogo:
    peliculas = []
    
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"
    
    def __init__(self, peliculas=[]):
        self.peliculas=peliculas
    def agregar(self, p):
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)
    
catalogo = Catalogo()

catalogo.agregar(p)
catalogo.agregar(p2)

catalogo.mostrar()

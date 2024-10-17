class Perro:
    def __init__(self, nombre, edad, raza, color):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau, guau!"


# Estas clases heredan de la clase Perro
class PerroPolicia(Perro):
    def __init__(self, nombre, edad, raza, color, especialidad):  # se le agrega un parametro mas a la clase y ademas se le agregan todas las variables de la clase padre.
        super().__init__(nombre, edad, raza, color)
        self.especialidad = especialidad

    def ladrar(self):
        return f"{self.nombre} tiene {self.edad} años y es un perro de raza {self.raza} y color {self.color} y su especialidad es {self.especialidad}"
    # le podemos agregar mas metodos a las clases hijas de la clase padre "Perro"

class PerroMascota(Perro):
    def __init__(self, nombre, edad, raza, color, juguete_favorito):
        super().__init__(nombre, edad, raza, color)
        self.juguete_favorito = juguete_favorito

    def ladrar(self):
        return f"{self.nombre} tiene {self.edad} años y es un perro de raza {self.raza} y color {self.color} y su juguete favorito es {self.juguete_favorito}"
        
perros = [
    PerroPolicia("PerroPolicia", 3, "Pastor Alemán", "Gris", "Cazador de Drogas"),
    PerroMascota("PerroMascota", 5, "Labrador", "Blanco", "Pelota de goma"),
]

for perro in perros:
    print(perro.ladrar())
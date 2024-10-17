class automovil:
    # crear e inicializar los atributos de la clase
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # metodos
    def arrancar(self):
        print(f"El {self.marca} del modelo {self.modelo} arrancó")

    def frenar(self):
        print(f"El {self.marca} del modelo {self.modelo} frenó")

    def info(self):
        return f"El {self.marca} del modelo {self.modelo} es de {self.año}"

mi_auto = automovil("Toyota", "Corolla", 2020)
mi_campero = automovil("Ford", "F-150", 2021)

#como crear o instanciar el objeto
print(mi_auto.arrancar())
print(mi_auto.frenar())
print(mi_auto.info())
print('\n', mi_campero.arrancar())
print(mi_campero.frenar())
print(mi_campero.info())

#herencia
class autoElectrico(automovil):
    def __init__(self, marca, modelo, año, bateria):
        super().__init__(marca, modelo, año)
        self.bateria = bateria

    def tipo_de_automovil(self):
        return f"El {self.marca} del modelo {self.modelo} es un auto electrico"

        def info(self):
            return f"El {self.marca} del modelo {self.modelo} es de {self.bateria} kw"

autos = [
    autoElectrico("Tesla", "Model S", 2022, "Lithium-Ion"),
    autoElectrico("Nissan", "Leaf", 2021, "Lithium-Ion"),
    # automovil("Toyota", "Corolla", 2020),
    # automovil("Ford", "F-150", 2021),
]

for auto in autos:
    print(auto.tipo_de_automovil())

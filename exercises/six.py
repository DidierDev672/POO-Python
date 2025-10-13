
# todo: Crea una jerarquia de clases para representar Vehiculo, coche, moto y Bicicleta.

class Venicle():
    def __init__(self, name, marca, modelo):
        self.name = name
        self.marca = marca
        self.modelo = modelo

    def information(self):
        return f"Name: {self.name}, marca: {self.marca}, modelo: {self.modelo}"


class Coche(Venicle):
    def __init__(self, name, marca, modelo, kilometraje):
        super().__init__(name, marca, modelo)
        self.kilometraje = kilometraje

    def informarionCoche(self):
        base = super().information()
        return f"{base}, and kilometraje {self.kilometraje} km/h"


class Moto(Venicle):
    def __init__(self, name, marca, modelo, kilometraje):
        super().__init__(name, marca, modelo)
        self.kilometraje = kilometraje

    def informationMoto(self):
        base = super().information()
        return f"{base} and kilometraje {self.kilometraje} km/h"


class Bicicleta(Venicle):
    def __init__(self, name, marca, modelo):
        super().__init__(name, marca, modelo)

    def informationBicleta(self):
        base = super().information()
        return f"{base} bicicleta"


coche = Coche("BMW X1", "BMW", "SUV", 250)
print(coche.informarionCoche())
moto = Moto("Yamaha Mt15", "Yamaha", "2026", 180)
print(moto.informationMoto())

bici = Bicicleta("BICICLETA ARIZONA Z10 8 VELOCIDADES", "MTB", "2026")
print(bici.informationBicleta())

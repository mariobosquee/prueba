class Coche:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad= velocidad
    def acelerar(self, incremento):
        self.velocidad += incremento
    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
    def mostar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad} km/h")

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, velocidad=0, bateria=0):
        super().__init__(marca, modelo, velocidad)
        self.bateria = bateria

    def info(self):
        print(f"{self.marca} {self.modelo} - {self.velocidad} km/h - Bateria: {self.bateria} %")


    def cargar_bateria(self):
        self.bateria = 100
        print("Bateria cargada al 100%")

mi_coche = Coche("Toyota", "Corolla")
mi_coche.acelerar(50)
mi_coche.mostar_informacion()

mi_coche_electrico = CocheElectrico("Tesla", "Model 3", 80)
mi_coche_electrico.acelerar(50)
mi_coche_electrico.info()


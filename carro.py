from mediosTransporteTerrestre import MediosTransporteTerrestre

class Carro(MediosTransporteTerrestre):
    def __init__(self, nombre, capacidad, medioDesplazamiento, marca, cantidadRuedas,placa,modelo):
        super().__init__(nombre, capacidad, medioDesplazamiento, marca, cantidadRuedas)
        self.placa = placa
        self.modelo = modelo
    
    def apagar(self):
        print('el carro se ha apagado')

    def encender(self):
        print('el carro se ha encendido')

    def acelerar(self):
        print('el carro esta acelerando')

    def listar(self):
        print('atributos del carro: nombre',self.nombre,'capacidad',self.capacidad,'medio',self.medioDesplazamiento,'marca',self.marca,'catidad de ruedas',self.cantidadRuedas,'placa',self.placa,'modelo',self.modelo)
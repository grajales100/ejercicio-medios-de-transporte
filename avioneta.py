from medioTransporteAereo import MediosTransporteAereo

class Avioneta(MediosTransporteAereo):
    def __init__(self, nombre, capacidad, medioDesplazamiento, marca):
        super().__init__(nombre, capacidad, medioDesplazamiento, marca)
    
    def planear(self):
        print('para volar la avioneta va planeando la velocidad del viento')

    def listar(self):
        print('atributos de la avioneta: nombre',self.nombre,'capacidad',self.capacidad,'medio',self.medioDesplazamiento,'marca',self.marca)
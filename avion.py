from medioTransporteAereo import MediosTransporteAereo

class Avion(MediosTransporteAereo):
    def __init__(self, nombre, capacidad, medioDesplazamiento, marca):
        super().__init__(nombre, capacidad, medioDesplazamiento, marca)

    def aterrizar(self):
        print('esta bajando el tren de aterrisaje')

    def listar(self):
        print('atributos del avion: nombre',self.nombre,'capacidad',self.capacidad,'medio',self.medioDesplazamiento,'marca',self.marca)
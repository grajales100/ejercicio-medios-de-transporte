from medioTransporteAcuatico import MediosTransporteAcuatico

class Barco(MediosTransporteAcuatico):
    def __init__(self, nombre, capacidad, medioDesplazamiento, marca):
        super().__init__(nombre, capacidad, medioDesplazamiento, marca)

    def anclar(self):
        print('estamos anclando el barco')

    def listar(self):
        print('atributos del barco: nombre',self.nombre,'capacidad',self.capacidad,'medio',self.medioDesplazamiento,'marca',self.marca)
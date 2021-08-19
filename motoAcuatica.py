from medioTransporteAcuatico import MediosTransporteAcuatico

class MotoAcuatica(MediosTransporteAcuatico):
    def __init__(self, nombre, capacidad, medioDesplazamiento, marca):
        super().__init__(nombre, capacidad, medioDesplazamiento, marca)

    def acelerar(self):
            print('la moto acuatica esta acelerando')

    def listar(self):
        print('atributos de la moto acuatica: nombre',self.nombre,'capacidad',self.capacidad,'medio',self.medioDesplazamiento,'marca',self.marca)
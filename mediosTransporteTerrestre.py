from medios_transporte import MediosTransporte

class MediosTransporteTerrestre(MediosTransporte):
    
    def __init__(self, nombre, capacidad, medioDesplazamiento, marca, cantidadRuedas):
        super().__init__(nombre, capacidad, medioDesplazamiento, marca)

        self.cantidadRuedas = cantidadRuedas

    def detenerse (self):
        print('para detenerse debe de utulizar el freno')

    def girar (self,lado):
        if lado=='derecha':
            print('vamos a girar a la derecha')
        elif lado=='izquierda':
            print('vamos a girar a la izquierda')
        else:
            print('el veiculo no entiende la instruccion')
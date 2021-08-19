class MediosTransporte:
    
    def __init__(self,nombre,capacidad,medioDesplazamiento,marca):
        self.nombre = nombre
        self.capacidad = capacidad
        self.medioDesplazamiento = medioDesplazamiento
        self.marca = marca

    def transportar(self):
        print('cada medio de transporte permite desplazarnos de diferentes maneras')    
from carro import Carro
from moto import Moto
from barco import Barco
from motoAcuatica import MotoAcuatica
from avioneta import Avioneta
from avion import Avion
class Main:
    listaCarro=[]
    listaMotos=[]
    listaAviones=[]
    listaAvionetas=[]
    listaBarco=[]
    listaMotoAcuatica=[]
    def menu(self,listaCarro,listaMotos,listaAviones,listaAvionetas,listaBarco,listaMotoAcuatica):
        encendido=True
        while encendido==True:
            print('                       ***BIENVENIDO***')
            print('**** A continuacion debe de elegir lo que quiere realizar*****')
            print('1.crear un medio de trnasporte')
            print('2.listar un medio de transporte')
            print('3.apagar programa')
            opcionP=input()

            if opcionP=='1':

                print('**** A continuacion debe de elegir el medio de transporte que quiere crear *****')
                print('1.crear medio de transporte terrestre')
                print('2.crear medio de transporte aereo')
                print('3.crear medio de transporte acuatico')
                

                opcion=input()

                if opcion =='1':
                    print('**** A continuacion debe de elegir el medio de transporte terrestre que quiere crear *****')
                    print('1.crear carro')
                    print('2.crear moto')
                    
                    opcionT=input()

                    if opcionT =='1':
                        print('vamos a crear un objeto de tipo carro')
                        print('por favor ingrese la marca del carro')
                        marca=input()
                        print('por favor ingrese la placa del carro')
                        placa=input()
                        print('por favor ingrese el modelo del carro')
                        modelo=input()

                        nuevoCarro=Carro('carro', 5, 'medio terrestre', marca, 4,placa,modelo)

                        listaCarro.append(nuevoCarro)

                    elif opcionT =='2':
                        print('vamos a crear un objeto de tipo moto')
                        print('por favor ingrese la marca de la moto')
                        marca=input()
                        print('por favor ingrese la placa de la moto')
                        placa=input()
                        print('por favor ingrese el modelo de la moto')
                        modelo=input()

                        nuevaMoto=Moto('moto', 2, 'medio terrestre', marca, 2,placa,modelo)

                        listaMotos.append(nuevaMoto)

                elif opcion =='2':
                    print('**** A continuacion debe de elegir el medio de transporte aereo que quiere crear *****')
                    print('1.crear avion')
                    print('2.crear avioneta')
                    
                    opcionA=input()

                    if opcionA =='1':
                        print('vamos a crear un objeto de tipo avion')
                        print('por favor ingrese la capacidad del avion')
                        capacidad=input()
                        print('por favor ingrese la marca del avion')
                        marca=input()
                        
                        nuevoAvion=Avion('avion', capacidad, 'medio aereo', marca)

                        listaAviones.append(nuevoAvion)

                    elif opcionA =='2':
                        print('vamos a crear un objeto de tipo avioneta')
                        print('por favor ingrese la capacidad de la avioneta')
                        capacidad=input()
                        print('por favor ingrese la marca de la avioneta')
                        marca=input()
                        
                        nuevaAvioneta=Avioneta('avioneta', capacidad, 'medio aereo', marca)

                        listaAvionetas.append(nuevaAvioneta)

                elif opcion =='3':
                    print('**** A continuacion debe de elegir el medio de transporte acuatico que quiere crear *****')
                    print('1.crear barco')
                    print('2.crear moto acuatica')
                    
                    opcionAC=input()

                    if opcionAC =='1':
                        print('vamos a crear un objeto de tipo barco')
                        print('por favor ingrese la capacidad del barco')
                        capacidad=input()
                        print('por favor ingrese la marca del barco')
                        marca=input()
                        
                        nuevoBarco=Barco('barco', capacidad, 'medio acuatico', marca)

                        listaBarco.append(nuevoBarco)

                    elif opcionAC =='2':
                        print('vamos a crear un objeto de tipo moto acuatica')
                        print('por favor ingrese la capacidad de la moto acuatica')
                        capacidad=input()
                        print('por favor ingrese la marca de la moto acuatica')
                        marca=input()
                    
                        nuevaMotoAcuatica=MotoAcuatica('moto acuatica', capacidad, 'medio acuatico', marca)

                        listaMotoAcuatica.append(nuevaMotoAcuatica)

                else:
                    print('esta opcion no es valida')    

            elif opcionP=='2':

                longitud1=len(listaCarro)
                longitud2=len(listaMotos)
                longitud3=len(listaAviones)
                longitud4=len(listaAvionetas)
                longitud5=len(listaBarco)
                longitud6=len(listaMotoAcuatica)

                print('cantidad de carros',longitud1)
                print('cantidad de motos',longitud2)
                print('cantidad de aviones',longitud3)
                print('cantidad de avionetas',longitud4)
                print('cantidad de barcos',longitud5)
                print('cantidad de motos acuaticas',longitud6)

                if longitud1>=1 or longitud2>=1 or longitud3>=1 or longitud4>=1 or longitud5>=1 or longitud6>=1:

                    print('**** A continuacion debe de elegir el medio de transporte que quiere listar *****')
                    print('1.listar medio de transporte terrestre')
                    print('2.listar medio de transporte aereo')
                    print('3.listar medio de transporte acuatico')

                    opcion=input()

                    if opcion =='1':
                        print('**** A continuacion debe de elegir el medio de transporte terrestre que quiere listar *****')
                        print('1.listar carro')
                        print('2.listar moto')
                        
                        opcionT=input()

                        if opcionT=='1':

                            if longitud1>=1:

                                print('vamos a listar los carros')

                                for car in listaCarro:
                                    print(car.listar())

                            else:
                                print('no hay ningun carro')
                          

                        elif opcionT =='2':

                            if longitud2>=1:

                                print('vamos a listar las motos')                               

                                for mo in listaMotos:
                                    print(mo.listar())

                            else:
                                print('no hay ninguna moto')

                        else:

                            print('la opcion no es valida')                          

                    elif opcion =='2':
                        print('**** A continuacion debe de elegir el medio de transporte aereo que quiere listar *****')
                        print('1.listar avion')
                        print('2.listar avioneta')
                        
                        opcionA=input()

                        if opcionA =='1':

                            if longitud3>=1:

                                print('vamos a listar los aviones')
                                for avio in listaAviones:
                                    print(avio.listar())

                            else:
                                print('no hay ningun avion')
                    

                        elif opcionA =='2':

                            if longitud4>=1:

                                print('vamos a listar las avionetas')
                                for neta in listaAvionetas:
                                    print(neta.listar())

                            else:
                                print('no hay ninguna avioneta')

                        else:

                            print('la opcion no es valida')

                    elif opcion =='3':
                        print('**** A continuacion debe de elegir el medio de transporte acuatico que quiere listar *****')
                        print('1.listar barco')
                        print('2.listar moto acuatica')
                        
                        opcionAC=input()

                        if opcionAC =='1':

                            if longitud5>=1:

                                print('vamos a listar los barcos')
                                for Bar in listaBarco:
                                    print(Bar.listar3())

                            else:
                                print('no hay ningun barco')

                        elif opcionAC =='2':

                            if longitud6>=1:
                            
                                print('vamos a listar las motos acuaticas')
                                for MotoAc in listaMotoAcuatica:
                                    print(MotoAc.listar3())

                            else:
                                print('no hay ninguna moto acuatica')

                        else:

                            print('la opcion no es valida')
                            
                    else:
                        print('esta opcion no es valida')

                else:
                    print('no hay ningun objeto en ninguna lista')

            elif opcionP=='3':
                print('gracias por utilizar el programa')
                encendido=False

listaCarro=[]
listaMotos=[]
listaAviones=[]
listaAvionetas=[]
listaBarco=[]
listaMotoAcuatica=[]
principal=Main()
principal.menu(listaCarro,listaMotos,listaAviones,listaAvionetas,listaBarco,listaMotoAcuatica)
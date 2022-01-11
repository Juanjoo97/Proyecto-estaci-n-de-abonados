from tono import *
from factura import *
from random import choice
from time import time, sleep
import pyglet


class Central:
    def __init__(self):
        self.abonado = ""
        self.listaDisponibles = []
        self.listaOcupados = []
        self.listaFueraServicio = []
       
        self.numerollamado = ""
        self.numerollamante = ""
        self.numerofacturado =""
        self.tonos = ["tonoMarcando.wav", "tonoOcupado.wav", "tonoFueradeServicio.wav"]
        self.duracion = 00.00
        self.costo = 1.88  # Pesos por segundo valor iva incluido ($ 113 por minuto)
        self.valor = 0

    def conversaciones(self):
        conversacion = ["conversacion1.wav","conversacion2.wav", "conversacion3.wav"]
        x = choice(conversacion)
        return x

    def IniciandoAbonados(self):
     for i in range(1, 21):
        self.abonado= int(8666600 + int(i))
        self.listaDisponibles.append(str(self.abonado))
     for i in range(1, 4):
        lo = choice(self.listaDisponibles)
        self.listaOcupados.append(lo)
        self.listaDisponibles.remove(lo)
     for i in range(1, 6):
        fs = choice(self.listaDisponibles)
        self.listaFueraServicio.append(fs)
        self.listaDisponibles.remove(fs)
     

     print("\nAbonados Disponibles: " + str(self.listaDisponibles))
     print("Abonados Ocupados: " + str(self.listaOcupados))
     print("Abonados Fuera de Servicio: " + str(self.listaFueraServicio))



    def Llamadas(self):
        print("\nPor favor ingrese el número de teléfono llamante: ")
        sonar()
        print('\n')
        llamante=input()
        self.numerollamante=llamante
        player = pyglet.media.Player()
        if (self.numerollamante in self.listaDisponibles):
            print("Por favor ingrese el número de teléfono que  desea llamar: ")
            sonar()
            print('\n')
            llamado=input()
            self.numerollamado=llamado
            if(self.numerollamante != self.numerollamado):
                if (self.numerollamado in self.listaDisponibles):
                    print("Marcando...")
                    marcacion = pyglet.resource.media('tonoMarcando.wav')
                    player.queue(marcacion)
                    player.play()
                    ti=time()
                    player.next_source()
                    conversacion = pyglet.resource.media(self.conversaciones())
                    player.queue(conversacion)
                    player.play()
                    sleep(conversacion.duration)
                    tf=time()
                    self.duracion=int(tf-ti)
                    print("\nSu tiempo de llamada fue de : ",self.duracion,"segundos")
                    print("")
                    factura.tarifa(self)
                    factura.factura(self)
                    sleep(5)
                    while True:
                        el=input("¿deseas realizar otra llamada? (s/[presiona enter]")
                        
                        if not el: break
                        repetir.Llamadarepetida(self)
                elif (self.numerollamado in self.listaOcupados):
                    print("El número marcado esta ocupado")
                    music = pyglet.resource.media('tonoOcupado.wav')
                    music.play()
                elif (self.numerollamado in self.listaFueraServicio):
                    print("El número marcado esta fuera de servicio")
                    music= pyglet.resource.media('tonoFueradeServicio.wav')
                    music.play()
                else:
                    print("El número marcado es invalido")
            else:
                print("Esta marcando el mismo numero de telefono")

        elif (self.numerollamante in self.listaOcupados):
            print("El telefono llamante esta ocupado")

        elif (self.numerollamante in self.listaFueraServicio):
            print("El telefono llamante esta fuera de servicio")

        else:
            print("No ingresó un numero de telefono valido")

class repetir:           
    def Llamadarepetida(self):
        player = pyglet.media.Player()
        if (self.numerollamante in self.listaDisponibles):
            print("Por favor ingrese el número de teléfono que  desea llamar: ")
            sonar()
            print('\n')
            llamado=input()
            self.numerollamado=llamado
            if(self.numerollamante != self.numerollamado):
                if (self.numerollamado in self.listaDisponibles):
                    print("Marcando...")
                    marcacion = pyglet.resource.media('tonoMarcando.wav')
                    player.queue(marcacion)
                    player.play()
                    ti=time()
                    player.next_source()
                    conversacion = pyglet.resource.media(self.conversaciones())
                    player.queue(conversacion)
                    player.play()
                    sleep(conversacion.duration)
                    tf=time()
                    self.duracion=int(tf-ti)
                    print("\nSu tiempo de llamada fue de : ",self.duracion,"segundos")
                    print("")
                    factura.tarifa(self)
                    factura.factura(self)
                    sleep(5)

                elif (self.numerollamado in self.listaOcupados):
                    print("El número marcado esta ocupado")
                    music = pyglet.resource.media('tonoOcupado.wav')
                    music.play()
                elif (self.numerollamado in self.listaFueraServicio):
                    print("El número marcado esta fuera de servicio")
                    music= pyglet.resource.media('tonoFueradeServicio.wav')
                    music.play()
                else:
                    print("El número marcado es invalido")
            else:
                print("Esta marcando el mismo numero de telefono")

        elif (self.numerollamante in self.listaOcupados):
            print("El telefono llamante esta ocupado")

        elif (self.numerollamante in self.listaFueraServicio):
            print("El telefono llamante esta fuera de servicio")

        else:
            print("No ingresó un numero de telefono valido")

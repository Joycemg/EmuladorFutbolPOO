#M
import random
import time
from club import club
from jugadores import jugadores
from partido import partido


#Lista de nombres de jugadores y de paises para automatizar la instancia
listaNombres = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Gerard Pique', 'Luis Suarez', 'Sergio Aguero', 'Sergio Ramos', 'Kylian Mbappe', 'Eden Hazard',
                'Toni Kross', 'Luka Modric', 'Andres Iniesta', 'Diego Armando Maradona', 'Karim Benzema', 'Angel Di Maria', 'Sergio Busquets', 'Antoine Griezmann', 'Philippe Coutinho', 'Zlatan Ibrahimovic', 'Edinson Cavani', 'Marcelinho Pitinho Chiquinho', 'Pierre Emerick Aubameyang', 'Paulo Dybala', 'Thiago Silva', 'James Rodriguez', 'Jordi Alba', 'Harry Kane', 'Paul Pogba', 'Marco Reus', 'Romelu Lukaku', 'Eemquielin culin-rotin']

listaPaises = ['Argentina', 'Brasil', 'Mexico', 'Uruguay', 'chile', 'España', 'Alemania']

#------------------------------------------------------------------------------------------

#Construccion de equipos[1]
def generar_instanciaEquipo(nombre, colorA, colorB, pais, nombres, paises):
    equipo = club(nombre, colorA, colorB, pais)
    for i in range(0,11):
        nombre = random.choice(nombres)
        edad = random.randint(18, 33)
        pais = random.choice(paises)
        listaNombres.remove(nombre)
        dorsal = random.randint(1, 60)
        jugador = jugadores(nombre, edad, pais, dorsal)
        equipo.agregar_plantel(jugador)    #[1]

    return equipo
 
def jugar(partidoInicia, duracion):
    inicio_partido = time.time()
    tiempo_partido = duracion

    #Probabilidades
    probabilidadPases = 0.80
    probabilidadGol = 0.20

    # def emulacion(equipoA, equipoB, duracion):
    #     while time.time() < inicio_partido + tiempo_partido:
    #         time.sleep(1)
    #         if partidoInicia.hacer_pases(probabilidadPases):
    #             partidoInicia.hacer_disparo(probabilidadGol)
    #         else:
    #             pass





#Creacion de equipos y partido
equipoA = generar_instanciaEquipo('Arsenal', 'Rojo', 'Blanco', 'Italia', listaNombres, listaPaises)
equipoB = generar_instanciaEquipo('River', 'Amarillo', 'Azul', 'Italia', listaNombres, listaPaises)
partido1 = partido('La bombonera', 'Marcos tragachele', equipoA, equipoB, 2)

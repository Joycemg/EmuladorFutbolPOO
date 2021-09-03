#M
import random
import time
from typing import Counter
from club import club
from jugadores import jugadores
from partido import partido

plantelA = []
plantelB = []

#Lista de nombres de jugadores y de paises para automatizar la instancia
listaNombres = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Gerard Pique', 'Luis Suarez', 'Sergio Aguero', 'Sergio Ramos', 'Kylian Mbappe', 'Eden Hazard',
                'Toni Kross', 'Luka Modric', 'Andres Iniesta', 'Diego Armando Maradona', 'Karim Benzema', 'Angel Di Maria', 'Sergio Busquets', 'Antoine Griezmann', 'Philippe Coutinho', 'Zlatan Ibrahimovic', 'Edinson Cavani', 'Marcelinho Pitinho Chiquinho', 'Pierre Emerick Aubameyang', 'Paulo Dybala', 'Thiago Silva', 'James Rodriguez', 'Jordi Alba', 'Harry Kane', 'Paul Pogba', 'Marco Reus', 'Romelu Lukaku', 'Eemquielin culin-rotin']

listaPaises = ['Argentina', 'Brasil', 'Mexico', 'Uruguay', 'chile', 'España', 'Alemania']

#------------------------------------------------------------------------------------------

#Instancia Jugadores y equipo club[1]
def generar_instanciaEquipo(nombre, colorA, colorB, pais, players, nombres, paises):
    equipo = club(nombre, colorA, colorB, pais)
    for i in range(0,11):
        nombre = random.choice(nombres)
        edad = random.randint(18, 33)
        pais = random.choice(paises)
        listaNombres.remove(nombre)
        dorsal = random.randint(1, 60)
        jugador = jugadores(nombre, edad, pais, dorsal)
        equipo.agregar_plantel(jugador.nombre)    #[1]
        players.append(jugador)

    return equipo

# def pases():
#         cont_pases = 0

#         while cont_pases < 100:
#             pase = random.randint(0, 100) 

#             if pase >= 50:
#                 cont_pases += 1
                

                
#             else:
#                 break

    
def jugar(partidoInicia, duracion):
    inicio_partido = time.time()
    tiempo_partido = duracion

    #Probabilidades
    probabilidadPases = 0.20
    probabilidadGol = 0.20

    while time.time() < inicio_partido + tiempo_partido:
        time.sleep(1)
        if partidoInicia.hacer_pases(probabilidadPases):
            partidoInicia.hacer_disparo(probabilidadGol)





equipoA = generar_instanciaEquipo('Arsenal', 'Rojo', 'Blanco', 'Italia', plantelA, listaNombres, listaPaises)
equipoB = generar_instanciaEquipo('River', 'Amarillo', 'Azul', 'Italia', plantelB, listaNombres, listaPaises)
partido1 = partido('La bombonera', 'Marcos tragachele', equipoA, equipoB)

jugar(partido1, 5)

partido1.mostrar_gol(equipoA)
partido1.mostrar_pases(equipoA)
# equipoA.mostrar_plantel()
# equipoA.mostrar_equipo()


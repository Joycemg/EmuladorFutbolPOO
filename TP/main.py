#M
import random
import time
from club import Club
from jugadores import Jugador
from partido import partido


#Lista de nombres de jugadores y de paises para automatizar la instancia
listaNombres = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Gerard Pique', 'Luis Suarez', 'Sergio Aguero', 'Sergio Ramos', 'Kylian Mbappe', 'Eden Hazard',
                'Toni Kross', 'Luka Modric', 'Andres Iniesta', 'Diego Armando Maradona', 'Karim Benzema', 'Angel Di Maria', 'Sergio Busquets', 'Antoine Griezmann', 'Philippe Coutinho', 'Zlatan Ibrahimovic', 'Edinson Cavani', 'Marcelinho Pitinho Chiquinho', 'Pierre Emerick Aubameyang', 'Paulo Dybala', 'Thiago Silva', 'James Rodriguez', 'Jordi Alba', 'Harry Kane', 'Paul Pogba', 'Marco Reus', 'Romelu Lukaku', 'Eemquielin culin-rotin']

listaPaises = ['Argentina', 'Brasil', 'Mexico', 'Uruguay', 'chile', 'España', 'Alemania']

#------------------------------------------------------------------------------------------

#Construccion de equipos[1]
def generar_instanciaEquipo(nombre, colorA, colorB, pais, nombres, paises):
    equipo = Club(nombre, colorA, colorB, pais)
    for i in range(0,11):
        nombre = random.choice(nombres)
        edad = random.randint(18, 33)
        pais = random.choice(paises)
        listaNombres.remove(nombre)
        dorsal = random.randint(1, 60)
        jugador = Jugador(nombre, edad, pais, dorsal, equipo.nombreC)
        time.sleep(0.1)
        equipo.comprar_jugador(jugador)    #[1]

    return equipo
 

#Creacion de equipos y partido
equipoA = generar_instanciaEquipo('Tigres', 'Rojo', 'Blanco', 'Italia', listaNombres, listaPaises)
equipoB = generar_instanciaEquipo('Leones', 'Amarillo', 'Azul', 'Italia', listaNombres, listaPaises)

primerPartido = partido('Estado del sur', 'tiago perder', equipoA, equipoB, 20)

primerPartido.mostrar_inicio()
primerPartido.sorteo_saque()
primerPartido.equipo_ganadorDeSorteo()
primerPartido.jugar()
primerPartido.mostrar_ganador()
primerPartido.mostrar_info()
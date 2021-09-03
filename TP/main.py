
import random
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

    
def disparos(juego):
        cont_shot = 0

        while cont_shot < 100:
            goles = random.randint(0, 150)

            if goles >= 80:
                cont_shot += 1
                juego.actualizar_gol()
            else:
                break




equipoA = generar_instanciaEquipo('Arsenal', 'Rojo', 'Blanco', 'Italia', plantelA, listaNombres, listaPaises)
equipoB = generar_instanciaEquipo('River', 'Amarillo', 'Azul', 'Italia', plantelB, listaNombres, listaPaises)
partido1 = partido('La bombonera', 'Marcos tragachele', equipoA, equipoB)

disparos(partido1)

partido1.mostrar_gol(equipoA)
# equipoA.mostrar_plantel()
# equipoA.mostrar_equipo()


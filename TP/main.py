import random
from club import club
from jugadores import jugadores


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
        equipo.agregar_jugadores(jugador.nombre)    #[1]
        players.append(jugador)

    return equipo

plantelA = []
plantelB = []

equipoA = generar_instanciaEquipo('Arsenal', 'Rojo', 'Blanco', 'Italia', plantelA, listaNombres, listaPaises)
equipoB = generar_instanciaEquipo('Arsenal', 'Rojo', 'Blanco', 'Italia', plantelB, listaNombres, listaPaises)

equipoA.mostrar_plantel()
equipoA.mostrar_equipo()
plantelA[0].mostrar_jugadores()





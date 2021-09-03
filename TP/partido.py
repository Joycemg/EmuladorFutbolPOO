import random
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB):
        self.cancha = cancha
        self.arbitro = arbitro
        self.pases = 0
        self.gol = 0
        self.equipoA = equipoA
        self.equipoB = equipoB


    def mostrar_gol(self, club):
        print(f''' 
        El equipo {club.nombreC} hizo {self.gol} goles.''')



    def mostrar_pases(self, equipo):
        print(f''' 
        {equipo.nombreC} hizo {self.pases} pases exitosos''')



    def hacer_pases(self, probabilidadPases):
        cont_pases = 0
        while cont_pases < 4:
            Pases = random.randint(0, 100) * probabilidadPases
            if Pases >= 1:
                cont_pases += 1
                self.actualizar_pases()
            else:
                pass

        if cont_pases == 4:
            return True

    def hacer_disparo(self, probabilidadGol):
        disparo = random.randint(10, 100) * probabilidadGol
        if disparo >= 1:
            self.actualizar_gol()



    def actualizar_gol(self):
        self.gol += 1

    def actualizar_pases(self):
        self.pases += 1
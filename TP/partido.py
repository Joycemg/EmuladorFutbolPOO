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
        

    def actualizar_gol(self):
        self.gol += 1

    # def mostrar_pases(self, equipo):
    #     print(f''' 
    #     {equipo.nombreC} hizo {self.pases} exitosos''')

    # def actualizar_pases(self):
    #     self.pases += 1
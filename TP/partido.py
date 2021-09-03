import random
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB, duracion):
        self.cancha = cancha
        self.arbitro = arbitro
        self.pases = 0
        self.gol = 0
        self.equipoA = equipoA
        self.equipoB = equipoB
        self.duracion = duracion


    def mostrar_inicio(self):
        print(f'''
        Duracion:   {self.duracion} minutos     
        Arbitro :   {self.arbitro}     
        Cancha  :   {self.cancha}
        {'-' * 60}
        Equipos :   {self.equipoA.nombreC}         VS           {self.equipoB.nombreC}
        Colores :   {self.equipoA.colores[0]} | {self.equipoA.colores[1]}                {self.equipoB.colores[0]} | {self.equipoB.colores[1]}
        Pais    :   {self.equipoA.pais}                       {self.equipoB.pais}
        {'-' * 60}''')

    def mostrar_gol(self):
        pass

    def mostrar_pases(self):
        pass



    def hacer_pases(self, probabilidadPases):
        cont_pases = 0
        while cont_pases < 4:
            Pases = random.randint(0, 100) * probabilidadPases
            if Pases >= 80:
                cont_pases += 1
                self.actualizar_pases()
            else:
                pass
        if cont_pases == 4:
            return True

    def hacer_disparo(self, probabilidadGol):
        disparo = random.randint(0, 100) * probabilidadGol
        if disparo >= 80:
            self.actualizar_gol()

    def sorteo_saque(self, equipoA, equipoB):
        arreglo = [equipoA, equipoB]
        ganador_saque = random.choice(arreglo)
        return ganador_saque



    def actualizar_gol(self):
        self.gol += 1

    def actualizar_pases(self):
        self.pases += 1
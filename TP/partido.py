import random
import time
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB, duracion):
        self.cancha = cancha
        self.arbitro = arbitro
        self.pases = 0
        self.gol = 0
        self.equipos = (equipoA, equipoB)
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

    def mostrar_sanciones(self):
        pass



        ##Metodo incompleto y nada funcional
    def jugar(self):
        self.cont_pases = 0
        self.contador = 0
        self.inicio_partido = time.time()
        self.tiempo_partido = self.duracion

        #Probabilidades
        self.probabilidadPases = 0.80
        self.probabilidadGol = 5.20

        while time.time() < self.inicio_partido + self.tiempo_partido:
            time.sleep(1)
            # self.contador += 1
            # print(self.contador)

            if self.hacer_pases(self.probabilidadPases):
                self.hacer_disparo(self.probabilidadGol)
            else:
                pass


    def hacer_pases(self, probabilidadPases):
        Pases = random.randint(0, 100) * probabilidadPases
        self.numero = random.randint(0,10)
        if Pases >= 30:
            self.equipos[0].plantel[self.numero].agarra_pelota()
            self.cont_pases += 1
        else:
            self.equipos[0].plantel[self.numero].pierde_pelota()

            self.cont_pases = 0

        if self.cont_pases == 4:
            self.actualizar_pases()
            self.cont_pases = 0
            
            return True

    def hacer_disparo(self, probabilidadGol):
        disparo = random.randint(0, 100) * probabilidadGol
        if disparo >= 50:
            self.actualizar_gol()
            print('                     GOOOL')
        else:

            print('                     FALLO')

    # def sorteo_saque(self):
    #     self.ganador_saque = random.choice(self.equipos)
    #     if self.ganador_saque == self.equipos[0]:
    #         self.equipos[0].estado_ofensivo()
    #     else:
    #         self.equipos[1].estado_ofensivo()

    
    # def equipo_local(self):
    #     print(f'''
    #     El equipo local va ser {self.ganador_saque.nombreC}''')



    def actualizar_gol(self):
        self.gol += 1

    def actualizar_pases(self):
        self.pases += 1

    
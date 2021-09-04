import random
import time
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB, duracion):
        self.cancha = cancha
        self.arbitro = arbitro
        self.goles = 0
        self.pases = 0
        self.equipos = [equipoA, equipoB]
        self.duracion = duracion
        self.cont_pasesE = 0

    def mostrar_inicio(self):
        print(f'''
        Duracion:   {self.duracion} minutos     
        Arbitro :   {self.arbitro}     
        Cancha  :   {self.cancha}
        {'-' * 60}
        Equipos :   {self.equipos[0].nombreC}         VS           {self.equipos[1].nombreC}
        Colores :   {self.equipos[0].colores[0]} | {self.equipos[0].colores[1]}                {self.equipos[1].colores[0]} | {self.equipos[1].colores[1]}
        Pais    :   {self.equipos[0].pais}                       {self.equipos[1].pais}
        {'-' * 60}''')

    # def mostrar_goles(self):
    #     print(f'''
    #     {self.gol} goles''')

    # def mostrar_pases(self):
    #     print(f'''
    #     {self.gol} pases exitosos''')

    def mostrar_sanciones(self):
        pass



        ##Metodo incompleto y nada funcional
    def jugar(self):
        
        self.index = 0
        self.contador = 0
        self.inicio_partido = time.time()
        self.tiempo_partido = self.duracion

        
        #Probabilidades
        self.probabilidadPases = 0.80
        self.probabilidadGol = 10.20

        while time.time() < self.inicio_partido + self.tiempo_partido:
            time.sleep(1)
            self.contador += 1
            print(self.contador)

            if self.hacer_pases(self.probabilidadPases):
                self.hacer_disparo(self.probabilidadGol)
            else:
                pass


    def hacer_pases(self, probabilidadPases):
        Pases = random.randint(0, 100) * probabilidadPases


        if self.equipos[0].modo == True:
            if Pases >= 35:
                self.equipos[0].plantel[0].agarra_pelota()
                self.cont_pasesE += 1
            else:
                self.equipos[0].plantel[0].pierde_pelota()
                self.equipos[0].modo_defensa()
                self.equipos[1].modo_ofensivo()
                self.cont_pasesE = 0
        else:
            if Pases >= 40:
                self.equipos[1].plantel[0].agarra_pelota()
                self.cont_pasesE += 1
            else:
                self.equipos[1].plantel[0].pierde_pelota()
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()
                self.cont_pasesE = 0

        if self.cont_pasesE == 4:
            self.actualizar_pases()
            self.cont_pasesE = 0
            return True

    def hacer_disparo(self, probabilidadGol):
        disparo = random.randint(0, 100) * probabilidadGol

        if disparo >= 50:
            self.actualizar_goles()
            print('                     GOOOL')
        else:

            print('                     FALLO')

    def sorteo_saque(self):
        self.ganador_saque = random.choice(self.equipos)
        if self.ganador_saque == self.equipos[0]:
            self.equipos[0].modo_ofensivo()
        else:
            self.equipos[1].modo_ofensivo()

    
    def equipo_ganadorDeSorteo(self):
        print(f'''
        El equipo local va ser {self.ganador_saque.nombreC}''')



    def actualizar_goles(self):
        self.goles += 1

    def actualizar_pases(self):
        self.pases += 1

    
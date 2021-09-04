import random
import time
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB, duracion):
        self.cancha = cancha
        self.arbitro = arbitro
        self.goles = [0, 0]
        self.golesF = [0, 0]
        self.pases = [0, 0]
        self.equipos = (equipoA, equipoB)
        self.duracion = duracion

        self.cont_pasesE = 0

    def mostrar_inicio(self):
        print(f'''
        {'-' * 60}''')
        print(f'''
        Duracion:   {self.duracion} minutos     
        Arbitro :   {self.arbitro}     
        Cancha  :   {self.cancha}
        {'-' * 60}
        Equipos :   {self.equipos[0].nombreC}         VS            {self.equipos[1].nombreC}
        Colores :   {self.equipos[0].colores[0]} | {self.equipos[0].colores[1]}                {self.equipos[1].colores[0]} | {self.equipos[1].colores[1]}
        Pais    :   {self.equipos[0].pais}                       {self.equipos[1].pais}
        {'-' * 60}''')

    def mostrar_ganador(self):
        print('-'*40)
        print(f'            {self.equipos[0].nombreC}   [{self.goles[0]}]')
        print(f'            {self.equipos[1].nombreC}   [{self.goles[1]}]')
        if self.goles[0] == self.goles[1]:
            print(f'                        Los equipos empataron      ')
        elif self.goles[0] < self.goles[1]:
            print(f'            {self.equipos[1].nombreC}  Gano')
        else:
            print(f'            {self.equipos[0].nombreC}  Gano')
        print('-'*40)     
    def mostrar_goles(self):
        print(f'''{self.equipos[0].nombreC} realizaron {self.goles[0]} goles''')
        print(f'''{self.equipos[1].nombreC} realizaron {self.goles[1]} goles''')
    def mostrar_pases(self):
        print(f'''{self.equipos[0].nombreC}     realizo     {self.pases[0]} pases''')
        print(f'''{self.equipos[1].nombreC}     realizo     {self.pases[1]} pases''')
    def mostrar_info(self):
        print(f'Equipo:    {self.equipos[0].nombreC}    Goles: [{self.goles[0]}] Goles Fallidos: [{self.golesF[0]}]    Pases: [{self.pases[0]}]')
        print(f'Equipo:    {self.equipos[1].nombreC}    Goles: [{self.goles[1]}] Goles Fallidos: [{self.golesF[1]}]    Pases: [{self.pases[1]}]')
        pass

    def mostrar_sanciones(self):


        pass



        ##Metodo incompleto y nada funcional
    def jugar(self):
        
        self.inicio_partido = time.time()
        self.tiempo_partido = self.duracion

        
        #Probabilidades
        self.probabilidadPases = 1.80
        self.probabilidadGol = 1.20

        while time.time() < self.inicio_partido + self.tiempo_partido:
            time.sleep(0.1)

            if self.hacer_pases(self.probabilidadPases):
                self.hacer_disparo(self.probabilidadGol)
            else:
                pass


    def hacer_pases(self, probabilidadPases):
        Pases = random.randint(0, 100) * probabilidadPases


        if Pases >= 60:
            if self.equipos[0].modo == True:
                print(self.equipos[0].nombreC)
                self.equipos[0].plantel[0].agarra_pelota()
                self.pases[0] += 1
                self.cont_pasesE += 1
            else:
                print(self.equipos[1].nombreC)
                self.equipos[1].plantel[0].agarra_pelota()
                self.pases[1] += 1
                self.cont_pasesE += 1

        else:
            if self.equipos[0].modo == True:
                self.equipos[0].modo_defensa()
                self.equipos[1].modo_ofensivo()
                print(self.equipos[0].nombreC)
                self.equipos[0].plantel[0].pierde_pelota()
                self.pases[1] += 1
                self.cont_pasesE = 0
            else:
                print(self.equipos[1].nombreC)
                self.equipos[1].plantel[0].pierde_pelota()
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()
                self.pases[0] += 1
                self.cont_pasesE = 0

        if self.cont_pasesE == 4:
            self.cont_pasesE = 0
            return True

    def hacer_disparo(self, probabilidadGol):

        disparo = random.randint(0, 100) * probabilidadGol
        if disparo >= 50:
            if self.equipos[0].modo == True:
                self.goles[0] += 1
                print(f'GOOOL DE {self.equipos[0].nombreC}')
            else:
                print(f'GOOOL DE {self.equipos[1].nombreC}')
                self.goles[1] += 1
        else:
            if self.equipos[0].modo == True:
               print(f'{self.equipos[0].nombreC} fallaron un gol')
               self.golesF[0] += 1
            else:
                print(f'{self.equipos[1].nombreC} fallaron un gol')
                self.golesF[1] += 1


    def sorteo_saque(self):
        self.ganador_saque = random.choice(self.equipos)
        if self.ganador_saque == self.equipos[0]:
            self.equipos[0].modo_ofensivo()
        else:
            self.equipos[1].modo_ofensivo()

    
    def equipo_ganadorDeSorteo(self):
        print(f'''
        El equipo local va ser {self.ganador_saque.nombreC}''')


    
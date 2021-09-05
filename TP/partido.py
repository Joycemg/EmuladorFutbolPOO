
import random
import time
from funciones import show
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB, duracion):
        self.cancha      = cancha
        self.arbitro     = arbitro
        self.goles       = [0, 0]
        self.golesF      = [0, 0]
        self.pases       = [0, 0]
        self.equipos     = (equipoA, equipoB)
        self.expulsados  = []
        self.duracion    = duracion

        self.cont_pasesE = 0
        self.index       = 0
        self.indexA      = [0,1,2,3,4,5,6,7,8,9,10]
        self.indexB      = [0,1,2,3,4,5,6,7,8,9,10]
        self.indexPasado = 0

    def mostrar_inicio(self):
        show(f'''
        {'-' * 60}''')
        print(f'''
        Duracion:   {self.duracion} minutos     
        Arbitro :   {self.arbitro}     
        Cancha  :   {self.cancha}
        {'-' * 60}
        Equipos :   {self.equipos[0].nombreC}         VS            {self.equipos[1].nombreC}
        Colores :   {self.equipos[0].colores[0]} | {self.equipos[0].colores[1]}                {self.equipos[1].colores[0]} | {self.equipos[1].colores[1]}
        Pais    :   {self.equipos[0].pais}                       {self.equipos[1].pais}
        {'-' * 60}
        ''')

        time.sleep(2)


    def mostrar_ganador(self):
        show(f'''            
        {self.equipos[0].nombreC}   [{self.goles[0]}]''')
        show(f'''            
        {self.equipos[1].nombreC}   [{self.goles[1]}]''')
        if self.goles[0] == self.goles[1]:
            print(f''' Los equipos empataron     ''')
        elif self.goles[0] < self.goles[1]:
            print(' ')
            print(f''' {self.equipos[1].nombreC}  Gano''')
        else:
            print(f''' {self.equipos[0].nombreC}  Gano''')
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

        for x in range(0,2):
            for i in range(0,11):
                if self.equipos[x].plantel[i].goles == 1:
                    print(f'''
{self.equipos[x].nombreC} > {self.equipos[x].plantel[i].dorsal}-{self.equipos[x].plantel[i].nombre} hizo {self.equipos[x].plantel[i].goles} gol''')
                if self.equipos[x].plantel[i].tarjetasA == 1:
                    print(f'''
{self.equipos[x].nombreC} > {self.equipos[x].plantel[i].dorsal}-{self.equipos[x].plantel[i].nombre} recibio {self.equipos[x].plantel[i].tarjetasA} una amarilla
                    ''')
                if self.equipos[x].plantel[i].tarjetasR == 1:
                    print(f'''
{self.equipos[x].nombreC} > {self.equipos[x].plantel[i].dorsal}-{self.equipos[x].plantel[i].nombre} recibio {self.equipos[x].plantel[i].tarjetasR} una Roja
                    ''')

                elif self.equipos[x].plantel[i].goles >= 2:
                    print(f'''
{self.equipos[x].nombreC} > {self.equipos[x].plantel[i].dorsal}-{self.equipos[x].plantel[i].nombre} hizo {self.equipos[x].plantel[i].goles} goles''')
    def mostrar_sanciones(self):


        pass



        ##Metodo incompleto y nada funcional
    def jugar(self):
        # contador = 0
        self.inicio_partido     = time.time()
        self.tiempo_partido     = self.duracion

        
        #Probabilidades
        self.probabilidadPases  = 1.80 #5
        self.probabilidadGol    = 0.80

        while time.time() < self.inicio_partido + self.tiempo_partido:
            time.sleep(0.1)
            # contador += 1
            # print(contador)

            if self.hacer_pases(self.probabilidadPases):
                self.hacer_disparo(self.probabilidadGol)

            else:
                pass


    def hacer_pases(self, probabilidadPases):
        Pases = random.randint(0, 100) * probabilidadPases

        if Pases >= 60:
            if self.equipos[0].modo == True:
                self.equipos[0].plantel[self.index].quitar_pelota()
                self.indexPasado  = self.index
                self.index        = random.choice(self.indexA)
                self.pases[0]    += 1
                self.cont_pasesE += 1
                self.equipos[0].plantel[self.index].dar_pelota()
                self.equipos[0].da_pase(self.indexPasado, self.index)
                    
            else:
                self.equipos[1].plantel[self.index].quitar_pelota()
                self.indexPasado = self.index
                self.index       = random.choice(self.indexB)
                self.pases[1]    += 1
                self.cont_pasesE += 1
                self.equipos[1].da_pase(self.indexPasado, self.index)
                self.equipos[1].plantel[self.index].dar_pelota()

        else:
            if self.equipos[0].modo == True:
                self.equipos[0].plantel[self.index].quitar_pelota()
                self.indexPasado = self.index
                self.index       = random.choice(self.indexA)
                self.pases[1]   += 1
                self.cont_pasesE = 0
                self.equipos[0].modo_defensa()
                self.equipos[1].modo_ofensivo()
                self.equipos[1].pierde_pase(self.index, self.indexPasado, self.equipos[0])
                self.equipos[1].plantel[self.index].dar_pelota()

            else:
                self.equipos[1].plantel[self.index].quitar_pelota()
                self.indexPasado = self.index
                self.index       = random.choice(self.indexB)
                self.pases[0]   += 1
                self.cont_pasesE = 0
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()
                self.equipos[0].pierde_pase(self.index, self.indexPasado, self.equipos[1])
                self.equipos[0].plantel[self.index].dar_pelota()

        if self.cont_pasesE == 4:
            self.cont_pasesE = 0
            return True

    def hacer_disparo(self, probabilidadGol):

        disparo = random.randint(0, 100) * probabilidadGol
        if disparo >= 50:
            if self.equipos[0].modo == True:
                self.goles[0]       += 1
                self.equipos[0].golazo(self.index)
                self.equipos[0].modo_defensa()
                self.equipos[1].modo_ofensivo()
                self.equipos[0].plantel[self.index].goles += 1
                self.equipos[0].plantel[self.index].quitar_pelota()
                self.equipos[1].plantel[self.index].dar_pelota()

            else:
                self.goles[1]      += 1
                self.equipos[1].plantel[self.index].goles += 1
                self.equipos[1].golazo(self.index)
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()
                self.equipos[1].plantel[self.index].quitar_pelota()
                self.equipos[0].plantel[self.index].dar_pelota()
        else:
            if self.equipos[0].modo == True:
                   self.equipos[0].fallazo(self.index)
                   self.golesF[0]   += 1
                   self.equipos[0].plantel[self.index].quitar_pelota()
                   self.equipos[1].plantel[self.index].dar_pelota()
                   self.equipos[0].modo_defensa()
                   self.equipos[1].modo_ofensivo()
            else:
                self.equipos[1].fallazo(self.index)
                self.golesF[1]      += 1
                self.equipos[1].plantel[self.index].quitar_pelota()
                self.equipos[0].plantel[self.index].dar_pelota()
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()



    def sanciones(self):
        sancion = random.randint(0, 100)
        if sancion >= 3:
            if self.equipos[0].modo == True:
                print(f'{self.equipos[1].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.index].nombre} cometio falta a {self.equipos[0].plantel[self.index].dorsal}-{self.equipos[0].plantel[self.indexPasado].nombre}')
                if self.equipos[1].plantel[self.index].tarjetasA == 1:
                    self.equipos[1].plantel[self.index].tarjetasR = 1
                    print(f'{self.equipos[1].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.index].nombre} RECIBE ROJA')
                elif self.equipos[1].plantel[self.index].tarjetasA == 0:
                    self.equipos[1].plantel[self.index].tarjetasA += 1
                    print(f'{self.equipos[1].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.index].nombre} RECIBE AMARILLA')
            else:
                print(f'{self.equipos[0].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.index].nombre} cometio falta a {self.equipos[1].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.indexPasado].nombre}')
                if self.equipos[1].plantel[self.index].tarjetasA == 1:
                    self.equipos[1].plantel[self.index].tarjetasR = 1
                    print(f'{self.equipos[0].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.index].nombre} RECIBE ROJA')
                elif self.equipos[1].plantel[self.index].tarjetasA == 0:
                    self.equipos[1].plantel[self.index].tarjetasA += 1
                    print(f'{self.equipos[0].plantel[self.index].dorsal}-{self.equipos[1].plantel[self.index].nombre} RECIBE AMARILLA')
        else:
            pass


    



    def sorteo_saque(self):
        self.defiende         = ''
        self.index            = random.randint(0,10)
        self.ganador_saque    = self.equipos[random.randint(0,1)].nombreC
        if self.ganador_saque == self.equipos[0].nombreC:
            self.defiende     = self.equipos[1].nombreC
            self.cont_pasesE += 1
            self.equipos[0].modo_ofensivo()
            self.equipos[0].plantel[self.index].dar_pelota()

        else:
            self.defiende     = self.equipos[0].nombreC
            self.cont_pasesE += 1
            self.equipos[1].modo_ofensivo()
            self.equipos[1].plantel[self.index].dar_pelota()

    



    def equipo_ganadorDeSorteo(self):
        print(f'''
        Ganador del sorteo  =    {self.ganador_saque}
        Ataca               =    {self.ganador_saque}
        Defiende            =    {self.defiende}''')

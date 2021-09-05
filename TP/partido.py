# Ezequiel Diaz | Marcelo Cabral | Marcos Wamba
import random
import time
from funciones import centrar
class partido:
    def __init__(self, cancha, arbitro, equipoA, equipoB, duracion):
        self.cancha      = cancha
        self.arbitro     = arbitro
        self.goles       = [0, 0]
        self.golesF      = [0, 0]
        self.pases       = [0, 0]
        self.equipos     = (equipoA, equipoB)
        self.expulsados  = [[],[]]
        self.duracion    = duracion

        self.cont_pasesE = 0
        self.index       = 0
        self.indexA      = [0,1,2,3,4,5,6,7,8,9,10]
        self.indexB      = [0,1,2,3,4,5,6,7,8,9,10]
        self.indexPasado = 0
        self.falta = False

    def mostrar_inicio(self):
        print(f'''
{'-' * 60}
Duracion:   {self.duracion} minutos     
Arbitro :   {self.arbitro}     
Cancha  :   {self.cancha}
{'-' * 60}
Equipos :   {self.equipos[0].nombreC}           VS            {self.equipos[1].nombreC}
Colores :   {self.equipos[0].colores[0]} | {self.equipos[0].colores[1]}                     {self.equipos[1].colores[0]} | {self.equipos[1].colores[1]}
Pais    :   {self.equipos[0].pais}                          {self.equipos[1].pais}
{'-' * 60}
''')
        time.sleep(2)


    def mostrar_ganador(self):
        print('')
        centrar('-'*40) 
        centrar(f'{self.equipos[0].nombreC}[{self.goles[0]}] [{self.goles[1]}]{self.equipos[1].nombreC}')

        if self.goles[0] == self.goles[1]:
            centrar('Los equipos empataron')
        elif self.goles[0] < self.goles[1]:
            centrar(f'{self.equipos[1].nombreC}  Gano')
        else:
            centrar(f'{self.equipos[0].nombreC}  Gano')

    def mostrar_goles(self):
        centrar(f'{self.equipos[0].nombreC} realizaron {self.goles[0]} goles')
        centrar(f'{self.equipos[1].nombreC} realizaron {self.goles[1]} goles')
    def mostrar_pases(self):
        centrar(f'{self.equipos[0].nombreC}     realizo     {self.pases[0]} pases')
        centrar(f'{self.equipos[1].nombreC}     realizo     {self.pases[1]} pases')
    def mostrar_info(self):
        centrar('-'*40)
        centrar(f'{self.equipos[0].nombreC}    Goles: [{self.goles[0]}] Goles Fallidos: [{self.golesF[0]}]    Pases: [{self.pases[0]}]')
        centrar(f'{self.equipos[1].nombreC}    Goles: [{self.goles[1]}] Goles Fallidos: [{self.golesF[1]}]    Pases: [{self.pases[1]}]')


   
        for i in range(0,2):
            if self.goles[i] == 0:
                continue
            centrar('-'*40)
            centrar(f'Goles del equipo {self.equipos[i].nombreC}')
            centrar('-'*40)
            for x in range(0,11):
                if self.equipos[i].plantel[x].goles == 1:
                    centrar(f'|{self.equipos[i].plantel[x].dorsal}|{self.equipos[i].plantel[x].nombre} hizo {self.equipos[i].plantel[x].goles} gol')
                elif self.equipos[i].plantel[x].goles > 1:
                    centrar(f'|{self.equipos[i].plantel[x].dorsal}|{self.equipos[i].plantel[x].nombre} hizo {self.equipos[i].plantel[x].goles} goles')

        if self.falta == True:
            print(f'Tarjetas de {self.equipos[i].nombreC}')

            for x in range(0, 2):
                for i in range(0, 11):
                    if self.equipos[x].plantel[i].tarjetasA == 1:
                        print(f' |{self.equipos[x].plantel[i].dorsal}|{self.equipos[x].plantel[i].nombre} recibio {self.equipos[x].plantel[i].tarjetasA} una amarilla')
                    elif self.equipos[x].plantel[i].tarjetasA > 2:
                        print(f' |{self.equipos[x].plantel[i].dorsal}|{self.equipos[x].plantel[i].nombre} recibio {self.equipos[x].plantel[i].tarjetasA} una amarillas')


        for x in range(0,2):
            if self.expulsados[x] == []:
                continue
            print(f'Jugadores expulsados {self.equipos[x].nombreC}')
            for i in self.expulsados[x]:
                print(f' |{self.equipos[x].plantel[i].dorsal}|{self.equipos[x].plantel[i].nombre}')



        ##Metodo incompleto y nada funcional
    def jugar(self):
        # contador = 0
        self.inicio_partido     = time.time()
        self.tiempo_partido     = self.duracion

        
        #Probabilidades
        self.probabilidadPases  = 4.00 #5
        self.probabilidadGol    = 2.80

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

        if Pases >= 70:
            if self.equipos[0].modo == True:
                self.indexPasado  = self.index
                self.index        = random.choice(self.indexA)
                self.pases[0]    += 1
                self.cont_pasesE += 1
                self.equipos[0].da_pase(self.indexPasado, self.index)
                    
            else:
                self.indexPasado = self.index
                self.index       = random.choice(self.indexB)
                self.pases[1]    += 1
                self.cont_pasesE += 1
                self.equipos[1].da_pase(self.indexPasado, self.index)

        else:
            if self.equipos[0].modo == True:
                self.indexPasado = self.index
                self.index       = random.choice(self.indexB)
                self.pases[1]   += 1
                self.cont_pasesE = 0
                self.equipos[1].pierde_pase(self.index, self.indexPasado, self.equipos[0])
                if self.sanciones():
                    self.equipos[0].modo_defensa()
                    self.equipos[1].modo_ofensivo()
                else:
                    self.index        = random.choice(self.indexA)
                    self.equipos[0].saca(self.indexPasado, self.index)

            else:
                self.indexPasado = self.index
                self.index       = random.choice(self.indexA)
                self.pases[0]   += 1
                self.cont_pasesE = 0
                self.equipos[0].pierde_pase(self.index, self.indexPasado, self.equipos[1])
                if self.sanciones():
                    self.equipos[1].modo_defensa()
                    self.equipos[0].modo_ofensivo()
                else:
                    self.index        = random.choice(self.indexB)
                    self.equipos[1].saca(self.indexPasado, self.index)

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

            else:
                self.goles[1]      += 1
                self.equipos[1].plantel[self.index].goles += 1
                self.equipos[1].golazo(self.index)
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()
        else:
            if self.equipos[0].modo == True:
                   self.equipos[0].fallazo(self.index)
                   self.golesF[0]   += 1
                   self.equipos[0].modo_defensa()
                   self.equipos[1].modo_ofensivo()
            else:
                self.equipos[1].fallazo(self.index)
                self.golesF[1]      += 1
                self.equipos[1].modo_defensa()
                self.equipos[0].modo_ofensivo()



    def sanciones(self):
        sancion = random.randint(0, 100)
        if sancion >= 75:
            if self.equipos[0].modo == True:
                self.equipos[1].falta(self.index, self.indexPasado, self.equipos[0])
                if self.equipos[1].plantel[self.index].tarjetasA == 1 or sancion > 90:
                    self.equipos[1].plantel[self.index].tarjetasA += 1
                    self.equipos[1].plantel[self.index].tarjetasR = 1
                    self.equipos[1].recibio_tarjA(self.index)
                    self.equipos[1].recibio_tarjR(self.index)

                else:
                   self.equipos[1].plantel[self.index].tarjetasA += 1
                   self.equipos[1].recibio_tarjA(self.index)

                if self.equipos[1].plantel[self.index].tarjetasR == 1:
                    self.indexB.pop(self.index)
                    self.expulsados[1].append(self.index)
                    self.equipos[1].expulsion(self.index)

        

            else:
                self.equipos[0].falta(self.index, self.indexPasado, self.equipos[1])
                if self.equipos[0].plantel[self.index].tarjetasA == 1 or sancion > 90:
                    self.equipos[0].plantel[self.index].tarjetasA += 1
                    self.equipos[0].plantel[self.index].tarjetasR = 1
                    self.equipos[0].recibio_tarjA(self.index)
                    self.equipos[0].recibio_tarjR(self.index)
                else:
                   self.equipos[0].plantel[self.index].tarjetasA += 1
                   self.equipos[0].recibio_tarjA(self.index)

                if self.equipos[0].plantel[self.index].tarjetasR == 1:
                    self.indexA.pop(self.index)
                    self.expulsados[0].append(self.index)
                    self.equipos[0].expulsion(self.index)

            self.falta = True
        else:
            return True
    



    def sorteo_saque(self):
        self.defiende         = ''
        self.index            = random.randint(0,10)
        self.ganador_saque    = self.equipos[random.randint(0,1)].nombreC
        if self.ganador_saque == self.equipos[0].nombreC:
            self.defiende     = self.equipos[1].nombreC
            self.cont_pasesE += 1
            self.equipos[0].modo_ofensivo()

        else:
            self.defiende     = self.equipos[0].nombreC
            self.cont_pasesE += 1
            self.equipos[1].modo_ofensivo()

    



    def equipo_ganadorDeSorteo(self):
        centrar('-'*40)
        centrar(f'| Ganador del sorteo  =    {self.ganador_saque}   |')
        centrar(f'| Ataca               =    {self.ganador_saque}   |')
        centrar(f' | Defiende            =    {self.defiende}   |')
        centrar('-'*40)

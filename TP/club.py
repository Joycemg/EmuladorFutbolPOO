
class Club:
    def __init__(self, nombreC, color1, color2, pais):
        self.nombreC = nombreC
        self.colores = (color1, color2)
        self.pais = pais
        self.plantel = []
        self.partidoGanados = 0
        self.partidoPerdidos = 0
        self.modo = False
        

    def comprar_jugador(self, jugadores):
        self.plantel.append(jugadores)
        # print(f'''
        # {self.nombreC} compro al jugador {jugadores.nombre} ''')

    def mostrar_plantel(self):
        for i in range(0,11):
            print(f'''
            {self.plantel[i]}''')

    def mostrar_equipo(self):
        print(f'''
            Equipo: {self.nombreC} | Colores: {self.colores}
                        Pais: {self.pais}
                        ''')
    
    def modo_ofensivo(self):
        self.modo = True

    def modo_defensa(self):
        self.modo = False

    def da_pase(self, indexPasado, index):
        print(f'''
            {self.nombreC} tiene la pelota
            {self.plantel[indexPasado].dorsal}-{self.plantel[indexPasado].nombre} se la paso a {self.plantel[index].dorsal}-{self.plantel[index].nombre}''')

    def pierde_pase(self, indexPasado, index):
        print(f'''
            {self.nombreC} pierde la pelota
            {self.plantel[index].dorsal}-{self.plantel[index].nombre} se la quito a {self.plantel[indexPasado].dorsal}-{self.plantel[indexPasado].nombre}''')

    def golazo(self, index):
        print(f'''
            {self.plantel[index].dorsal}-{self.plantel[index].nombre} Dispara al arco [  GOOOOOL!!] de {self.nombreC}''')
    def fallazo(self, index):
        print(f'''
            {self.plantel[index].dorsal}-{self.plantel[index].nombre} Dispara al arco [  FALLO!!  ] de {self.nombreC}''')

    def actualizar_partidosGanados(self):
        pass
    def actualizar_partidosPerdidos(self):
        pass

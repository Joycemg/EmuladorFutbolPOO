
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




    def actualizar_partidosGanados(self):
        pass
    def actualizar_partidosPerdidos(self):
        pass

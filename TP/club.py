from funciones import show
class Club:
    def __init__(self, nombreC, color1, color2, pais):
        self.nombreC = nombreC
        self.colores = (color1, color2)
        self.pais = pais
        self.plantel = []
        self.modo = False
        

    def comprar_jugador(self, jugadores):
        self.plantel.append(jugadores)
        # show(f'''
        #  {self.nombreC} compro al jugador {jugadores.nombre} ''', vd=0.002)

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
        show(f'''
            {self.nombreC} tiene la pelota
            {self.plantel[indexPasado].dorsal}-{self.plantel[indexPasado].nombre} se la paso a {self.plantel[index].dorsal}-{self.plantel[index].nombre}
            
            ''', vd=0.015)

    def pierde_pase(self, index, indexPasado, equipo):
        show(f'''
            {self.nombreC} pierde la pelota

            {self.plantel[index].dorsal}-{self.plantel[index].nombre} se la quito a {equipo.plantel[indexPasado].dorsal}-{equipo.plantel[indexPasado].nombre}
            
            ''', vd=0.015)

    def golazo(self, index):
        show(f'''
            {self.plantel[index].dorsal}-{self.plantel[index].nombre} Dispara al arco [  GOOOOOL!!] de {self.nombreC}
            
            ''', vd=0.020)
    def fallazo(self, index):
        show(f'''
            {self.plantel[index].dorsal}-{self.plantel[index].nombre} Dispara al arco [  FALLO!!  ] de {self.nombreC}
            
            ''', vd=0.020)


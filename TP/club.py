
class club:
    def __init__(self, nombreC, color1, color2, pais):
        self.nombreC = nombreC
        self.colores = (color1, color2)
        self.pais = pais
        self.plantel = []
    

    def agregar_plantel(self, jugadores):
        self.plantel.append(jugadores)

    def mostrar_plantel(self):
        for i in range(0,11):
            print(f'''
            {self.plantel[i]}''')

    def mostrar_equipo(self):
        print(f'''
            Equipo: {self.nombreC} | Colores: {self.colores}
                        Pais: {self.pais}
                        ''')

    def mostrar_pases(self):
        pass

    def actualizar_pases(self):
        pass
    
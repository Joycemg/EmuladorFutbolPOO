class jugadores:
    def __init__(self, nombre, edad, pais, dorsal):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.dorsal = dorsal
        self.tarjetasA = int
        self.tarjetasR = int
        self.goles = int

    def mostrar_jugador(self):
                print(f'''
            Nombre: {self.nombre} | Edad: {self.edad}
            Pais: {self.pais} | dorsal: {self.dorsal}
                        ''')

    def mostrar_tarjetas(self):
         print(f'''
            Tarjeta Amarilla {self.tarjetasA}
            Tarjeta ROja {self.tarjetasR}        
                      ''')

    def actualizar_tarjetas(self):
        pass

    def mostrar_goles(self):
        pass

    def actualizar_goles(self):
        pass
    
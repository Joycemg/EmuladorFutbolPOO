class Jugador:
    def __init__(self, nombre, edad, pais, dorsal, equipo):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.dorsal = dorsal
        self.equipo = equipo
        self.tarjetasA =  0
        self.tarjetasR = 0
        self.goles = 0
        self.golesFallidos = 0

    def mostrar_jugador(self):
                print(f'''
            Nombre: {self.nombre} | Edad: {self.edad}
            Pais: {self.pais} | dorsal: {self.dorsal}
            Equipo: {self.equipo}            ''')

    def mostrar_tarjetas(self):
         print(f'''
            Tarjeta Amarilla {self.tarjetasA}
            Tarjeta ROja {self.tarjetasR}        
                      ''')
    

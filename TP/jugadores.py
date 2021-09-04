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
        self.pelota = False

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


    def agarra_pelota(self):
        self.pelota = True
        print(f'''
        {self.nombre} tiene la pelota''')
        
    def pierde_pelota(self):
        self.pelota = False
        print(f'''
        {self.nombre} pierde la pelota''')


    def actualizar_tarjetas(self):
        pass

    def mostrar_goles(self):
        pass

    def mostrar_golesFallidos(self):
        pass

    def actualizar_goles(self):
        pass
    def actualizar_golesFallidos(self):
        pass
    

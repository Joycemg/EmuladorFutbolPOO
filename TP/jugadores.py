class jugadores:
    def __init__(self, nombre, edad, pais, dorsal):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.dorsal = dorsal

    def mostrar_jugadores(self):
                print(f'''
            Nombre: {self.nombre} | Edad: {self.edad}
            Pais: {self.pais} | dorsal: {self.dorsal}
                        ''')
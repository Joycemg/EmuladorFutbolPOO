import time
import os
import shutil
def show(variable, vd = 0.005): # Estilo del print
    for letra in variable:
        time.sleep(vd)
        print(letra, end='',flush=True)

def centrar(texto):
    cols, rows = shutil.get_terminal_size()
    print(texto.center(cols))

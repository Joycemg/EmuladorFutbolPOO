import time
def show(variable, vd = 0.005): # Estilo del print
    for letra in variable:
        time.sleep(vd)
        print(letra, end='',flush=True)
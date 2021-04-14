import os

procesos = int(input("Cuantos procesos hijos quiere a generar?"))

def proceso_hijo():
    if os.fork() == 0:
        print("Soy:", os.getpid(), ",Mi Padre es:", os.getppid())

for i in range(procesos):
    proceso_hijo()
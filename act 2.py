import sys
import getopt
import os

(opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:')

print("Opciones:", opt)

for (op, ar) in opt:
    if op in '-i':
        texto1 = ar
    elif op == '-o':
        texto2 = ar
    else:
        print("Opcion Invalida")

if os.path.isfile(texto1):
    print("El Archivo Existe")
    file = open(texto1, 'r')
    contenido = file.read()
    file.close()
    file_2 = open(texto2, 'a+')
    file_2.write(contenido)
    print("Se Copio el Contenido")
    file_2.close()
else:
    print("No Existe el Archivo")
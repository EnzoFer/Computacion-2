import sys
import getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')


for (op, ar) in opt:
    if op in '-o':
        operador = ar
    elif op == '-n':
        num1 = ar
    elif op == '-m':
        num2 = ar
    else:
        print("Opcion Invalida")

if operador == '+':
    print( num1, "+", num2, "es:", int(num1) + int(num2))
elif operador == '-':
    print( num1, "-", num2, "es:", int(num1) - int(num2))
elif operador == '*':
    print( num1, "*", num2, "es:", int(num1) * int(num2))
elif operador == '/':
    print( num1, "/", num2, "es:", int(num1) / int(num2))

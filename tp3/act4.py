import sys
import os


def proceso_hijo():

    if os.fork() == 0:

        if os.fork() or os.fork():
            os.fork()
            print("Soy el hijo, mi pid es:", os.getpid())
            print("Pid:", os.getpid(), "finalizado")
            print("---------------------------------")
            sys.exit(0)


def proceso_padre():
    print("---------------------------------------")
    print("mi hijo, pid:", os.getpid(), "termino")
    print("---------------------------------------")
    os.fork()
    print("Soy el padre, mi pid es:", os.getppid(), ", mi hijo es:", os.getpid())
    print("----------------------------------------------------------------------")


proceso_hijo()
proceso_padre()
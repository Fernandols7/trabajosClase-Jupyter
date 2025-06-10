# Invocar la clase OperacionesAritmeticas

import os
os.system('cls' if os.name == 'nt' else 'clear')


from claseOpAritmeticas import OperacionesAritmeticas

op = OperacionesAritmeticas(10, 2)

op.suma()
op.resta()
op.multiplicacion()
op.division()
op.potencia()
op.residuo()
op.raizCuadrada()
# Ciclo While tabla de multiplicar

import os
os.system('cls' if os.name == 'nt' else 'clear')


num = int(input("Ingrese un numero: "))
i = 1

while i <= 10:
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    i += 1
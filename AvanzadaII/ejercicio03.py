import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ciclo for para mostrar las tablas de multiplicar


numero = int(input("Ingrese un numero: "))

for i in range(1,11):
    print(f"{numero}X{i} = {numero*i}")
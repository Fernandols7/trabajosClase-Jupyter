# Operaciones aritmeticas con funciones

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Suma
def suma(a,b):
    return a+b

# Resta
def resta(a,b):
    return a-b

# Multiplicacion
def multi(a,b):
    return a*b

# Division
def division(a,b):
    return a/b

# Potencia
def potencia(a,b):
    return a**b

# Raiz cuadrada
def raiz(a):
    if a < 0:
        return "Error: raiz negativa"
    return a ** 0.5


print(f"La suma es: {suma(1,1)}")
print(f"La resta es: {resta(1,1)}")
print(f"La multiplicacion es: {multi(1,1)}")
print(f"La division es: {division(1,1)}")
print(f"La potencia es: {potencia(2,3)}")
print(f"La raiz cuadrada de 9 es: {raiz(9)}")
# Ejercicio para saber si una persona es mayor de edad

import os
os.system('cls' if os.name == 'nt' else 'clear')


print("PROGRAMA QUE CALCULA LA EDAD EN PYTHON")
edad = int(input("Ingrese su año de nacimiento: "))
aActual = 2025

edadActual = aActual - edad
print(f"Su edad es de: {edadActual} años")

if edadActual >= 21:
    print(f"Ya tienes {edadActual} años por lo tanto ya te andan los cutes")
else:
    print(f"Ya tiene {edadActual} años la bb")
    if edadActual >= 18:
        print(f"Ya puedes votar por RIXI o x Nasralla o x Papi, eres ciudadano")
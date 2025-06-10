# Ejercicio de operaciones aritmeticas con clases

import os
os.system('cls' if os.name == 'nt' else 'clear')


class OperacionesAritmeticas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        print(f"La suma de {self.a} + {self.b} = {self.a + self.b}")

    def resta(self):
        print(f"La resta de {self.a} - {self.b} =  {self.a - self.b}")

    def multiplicacion(self):
        print(f"La multiplicacion de {self.a} x {self.b} = {self.a * self.b}")

    def division(self):
        print(f"La division de {self.a} / {self.b} =  {self.a / self.b}")

    def potencia(self):
        print(f"La potencia de {self.a} elevado a {self.b} es: {self.a ** self.b}")

    def residuo(self):
        print(f"El residuo de {self.a} % {self.b} = {self.a % self.b}")

    def raizCuadrada(self):
        print(f"La raiz cuadrada de {self.a} es: {self.a ** 0.5}")
        print(f"La raiz cuadrada de {self.b} es: {self.b ** 0.5}")
        

op = OperacionesAritmeticas(10, 2)

op.suma()
op.resta()
op.multiplicacion()
op.division()
op.potencia()
op.residuo()
op.raizCuadrada()
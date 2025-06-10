# Creacion de la clase Animal

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def correr(self):
        print(f"{self.nombre} esta corriendo")

class Perro(Animal):

    def ladrar(self):
        print(f"Guau guau guau, corran que ahi viene {self.nombre}")

miPerro = Perro("Shelsea")

miPerro.ladrar()
miPerro.correr()
miPerro.comer()

# Definir un objeto para usar la clase

perro = Animal("Firulais")
perro.correr()
perro.comer()

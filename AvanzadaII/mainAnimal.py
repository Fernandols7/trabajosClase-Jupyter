# Invocar la clase Animal

import os
os.system('cls' if os.name == 'nt' else 'clear')


from clase01 import Perro

miPerro = Perro("Shelsea")

miPerro.ladrar()
miPerro.correr()
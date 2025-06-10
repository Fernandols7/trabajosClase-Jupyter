# Funciones 

# Definimos la funcion
def saludo(nombre):
    print(f"Hola {nombre}")

def _PI():
    return 3.1416

def suma(a,b):
    return a+b

# Invocamos la funcion
saludo("Funes")

# CALCULAR EL DIAMETRO DE UN CIRCULO
r = 1
diametro=2*_PI*r
print(f"Diametro: {diametro}")

# Funcion suma
print(f"Funcion suma: {suma(1,1)}")
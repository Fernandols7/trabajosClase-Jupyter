# Elaborar un programa que muestre el total de una compra de un solo producto 
# calculando el isv y dar un descuento solamente cuando el importe de la compra 
# sea mayor a 10,000 el descuento sera de un 25%

import os
os.system('cls' if os.name == 'nt' else 'clear')


def cal_subtotal(precio, cantidad):
    return precio * cantidad

def cal_descuento(subtotal):
    if subtotal >= 10000:
        descuento = subtotal * 0.25
        subtotal -= descuento
        print(f"Descuento: L. {descuento}")
    else:
        descuento = 0
    return subtotal, descuento

def cal_isv(subtotal):
    return subtotal * 0.15

def cal_total(subtotal, isv):
    return subtotal + isv

def resultado(subtotal, isv, total):
    print(f"Subtotal: L. {subtotal}")
    print(f"ISV: L. {isv}")
    print(f"Total a pagar: L. {total}")


precio = 200
cantidad = float(input("Ingrese la cantidad: "))

subtotal = cal_subtotal(precio, cantidad)
subtotal, descuento = cal_descuento(subtotal)
isv = cal_isv(subtotal)
total = cal_total(subtotal, isv)

resultado(subtotal, isv, total)
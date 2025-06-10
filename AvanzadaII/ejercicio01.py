# Elaborar un programa que muestre el total de una compra de un solo producto 
# calculando el isv y dar un descuento solamente cuando el importe de la compra 
# sea mayor a 10,000 el descuento sera de un 25%

precio = 200
cantidad = float(input("Ingrese la cantidad: "))
subTotal = precio * cantidad
isv = subTotal * 0.15
total = subTotal + isv

print(f"Subtotal: {subTotal}")

if subTotal >= 10000:
    descuento = subTotal * 0.25
    subTotal = subTotal - descuento
    print(f"Descuento: {descuento}")
else:
    descuento = 0

isv = subTotal * 0.15
total = subTotal + isv

print(f"ISV: {isv}")
print(f"Total a pagar: {total}")

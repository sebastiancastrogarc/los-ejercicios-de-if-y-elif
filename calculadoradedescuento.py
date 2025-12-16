precio = float(input("Ingresa el precio del producto: "))

if precio < 50:
    descuento = 0
    print("El descuento es:", descuento)
elif precio <= 100:
    descuento = precio * 0.15
    print("El descuento es:", descuento)
elif precio > 100:  
    descuento = precio * 0.30
    print("El descuento es:", descuento)

    
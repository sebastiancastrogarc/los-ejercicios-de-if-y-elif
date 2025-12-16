a = float(input(("Ingresa el primer numero: ")))
b = float(input(("Ingresa el segundo numero: ")))

if a > b:
    print("El numero mayor es:", a)
elif b > a:
    print("El numero mayor es:", b)
elif a == b:
    print("Los numeros son iguales")
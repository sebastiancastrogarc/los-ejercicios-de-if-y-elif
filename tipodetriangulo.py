a = float(input("Ingresa el primer lado: "))
b = float(input("Ingresa el segundo lado: "))
c = float(input("Ingresa el tercer lado: "))

if a == b and b == c:
    print("El triángulo es equilátero")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles")
elif True:
    print("El triángulo es escaleno")
peso = float (input("Ingresa tu peso en kilogramos: "))
altura = float (input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidad")
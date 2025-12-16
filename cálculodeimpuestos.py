salario = float(input("Ingresa el salario: "))
if salario > 30000:
    impuesto = salario * 0.20
    print("El impuesto a pagar es:", impuesto) 
elif salario < 10000:   
    print("El impuesto es: 0")
elif salario <= 30000:
    impuesto = salario * 0.10
    print("El impuesto a pagar es:", impuesto)
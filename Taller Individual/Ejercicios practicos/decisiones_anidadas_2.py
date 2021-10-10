entero = int(input("Digite un número entero:" ))

if entero >= 10 ^ entero <= 99:
        print("El número es positivo y tiene dos digitos")
elif entero >= 0 ^ entero <= 10:
        print("El número es positivo y no tiene dos digitos")
elif entero >= -999 ^ entero <= -100:
        print("El número es negativo y tiene tres digitos")
else:
        print("El número es negativo y no tiene tres digitos")
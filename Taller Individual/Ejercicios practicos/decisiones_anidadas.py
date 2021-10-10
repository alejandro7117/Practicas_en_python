#programa Decisiones_Anidadas
def numero():

    entero = int(input("Digite un número entero:" ))

    if entero > 0:
        if entero >= 10 and entero <= 99:
            return("El número es positivo y tiene dos digitos")
        else:
            return("El número es positivo y no tiene dos digitos")

        
    else:
        if entero >= -999 and entero <= -100:
            return("El número es negativo y tiene tres digitos")
        else:
            return("El número es negativo y no tiene tres digitos")

print(numero())
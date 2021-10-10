def telefono():
    numero = input("Ingrese el numero telefonico en formato: \n+57-numero-extension: ")
    cortar = numero[4:-3]
    return cortar

print(telefono())
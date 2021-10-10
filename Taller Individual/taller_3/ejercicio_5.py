def name_letras():
    nombre = input("Ingrese su nombre: ")

    longitud = len(nombre)
    mayuscula = nombre.upper()

    return f"{mayuscula}\nel numero de letras que tiene su nombre es {longitud}"

print(name_letras())

def saludo():
    name = input("¿Cual es tu nombre?: ")
    return f"¡Hola {name}!"
    
    
def saludo_1(nombre):
    return f"¡Hola {nombre}!"

print(saludo())
print(saludo_1("alejandro"))


def name():
    nombre = input("Ingresa tu nombre: ")
    repetir = input("Ingresa un numero entero:" )

    #validar
    if int(repetir) <= 0 or repetir is float(repetir):
        return "Ingrese un numero entero positivo"

    #_____________________________________________________________________________
    #algoritmo    
    if int(repetir) >= 1:
        x = (nombre + "\n") * int(repetir)
        return x 
        
   
print(name())
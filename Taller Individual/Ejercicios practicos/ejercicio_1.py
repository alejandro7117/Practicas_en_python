# operacion para que el resulatdo de 1
operacion_1 = 6 // (2 * 2 + 1)

#operacion para que de el resulatdo correcto 9
operacion_2 = 6 // 2 * (2 + 1)

print("Cual es el resultado correcto de la siguinete operación?")  
elegir =  int(input("6 / 2 * (2 + 1) : 1 ó 9 :  "))

if elegir == 1:
        print("6 / 2 * (2 + 1) es =", operacion_1)
        print("esta resultado es incorrecto por que no se sigue las reglas de precedencia de operadores ")
        print("ya que primero se debe realizar la operacion de (), luego la divison y por ultimo la multiplicación")
elif elegir == 9:
        print("6 / 2 * (2 + 1) es =", operacion_2 )
        print("Esta es la respuesta correcta")
else:
        print("PORFAVOR DIGITE UNA DE LAS DOS OPCIONES")
    
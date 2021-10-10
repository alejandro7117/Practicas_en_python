#entradas
_5 = 2 + 2 + 2 - 2 // 2
_6 = 2 + 2 + 2 + 2 - 2
_7 = 2 * 2 + 2 + 2 // 2
_8 = 2 * 2 * 2 + 2 - 2
_9 = 2 * 2 * 2 + 2 // 2
_10 = 2 + 2 + 2 + 2 + 2

#procedimiento
print("Que numero deseas recibir utilizando cinco 2´s")

elegir = int(input("5, 6, 7, 8, 9, 10 : "))

if elegir == 5:
    print("2 + 2 + 2 - 2 / 2 =", _5)
elif elegir == 6:
    print("2 + 2 + 2 + 2 - 2 =", _6)
elif elegir == 7:
    print("2 * 2 + 2 + 2 / 2 =", _7)
elif elegir == 8:
    print("2 * 2 * 2 + 2 - 2 =", _8)
elif elegir == 9:
    print("2 * 2 * 2 + 2 / 2 =", _9)
elif elegir == 10:
    print("2 + 2 + 2 + 2 + 2 =", _10)
else:
    print("OPCION INVALIDA")
    print("DIGITE UNA OPCIÓN CORRECTA")
    
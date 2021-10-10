#entradas
cajas = int(input("Cuantas cajas se compraron? : "))
latas_en_cajas = int(input("Cuantas latas vienen por caja? : "))
invitados = int(input("Cantidad de invitados? : "))

#procedimiento
x = cajas * latas_en_cajas
y = x // invitados
z = x % invitados

print("Cada invitado podra tomar",y, "latas de refrescos")
print("Sobran",z,"latas de refresco")

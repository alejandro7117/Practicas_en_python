#entradas
vueltas = int(input("Cantidad de vueltas en un minuto? : "))
tiempo_decimal = 640 / 60
tiempo_entero = 640 // 60

#procedimiento
vueltas_total_seg = vueltas * tiempo_decimal
vueltas_total_seg_1 = vueltas * tiempo_entero

entero_decimal = str(input("Desea el valor en decimal ó entero? : "))
if entero_decimal == "decimal":
    print("El spinner dio", vueltas_total_seg," vueltas en 640 segundos")
elif entero_decimal == "entero":
    print("El spinner dio",vueltas_total_seg_1," vueltas en 640 segundos")


    

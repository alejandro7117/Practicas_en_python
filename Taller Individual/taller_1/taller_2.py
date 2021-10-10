#entradas

costo_inicial_celular = int(input("valor del celular? : "))
porcentaje_incremento = 20
iva = 21

#procedimiento
incremento_dia= int(costo_inicial_celular * porcentaje_incremento / 100)    #para sacar el valor del incremento
costo_con_incremento = costo_inicial_celular + incremento_dia               #costo del celular con el incremento 
celular_con_iva = int(costo_con_incremento * iva / 100)                     #para sacar el valor del iva

costo_final = celular_con_iva + costo_con_incremento                        #suma del celular, el iva y el incremento
print("El costo final del celular es ", costo_final)

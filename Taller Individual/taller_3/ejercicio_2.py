def pago_nomina(horas_trabajadas,tarifa_de_pago):

    #validar
    if horas_trabajadas < 40:
        return f"su salario es {horas_trabajadas * tarifa_de_pago}"
    #__________________________________________________________________________________________________________
    #algoritmo
    if horas_trabajadas > 40:
    
       tarifa_incremento =tarifa_de_pago + (tarifa_de_pago * 50 // 100)
       horas_trabajadas_extras = horas_trabajadas - 40
       salario = (horas_trabajadas_extras * tarifa_incremento) + (40 * tarifa_de_pago) 
       return f"su salario es {salario}"

print(pago_nomina(6,5000))
print(pago_nomina(50,5000))


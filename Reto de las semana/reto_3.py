def simulador_prestamo_baniscutp(datos_prestamo: dict) -> dict:
    #recolectar datos a cada variable
    EA = datos_prestamo["interes anual"]
    prestamo = datos_prestamo["prestamo"]
    gastos_documentacion = datos_prestamo["gastos documentacion"]
    cuotas = datos_prestamo["cuotas"]
    #formulas tmv
    TMV = (1+(EA/100))**(1/12)-1
    #formula de cuota
    saldo_a_financiar = prestamo + gastos_documentacion
    nuevo = saldo_a_financiar

    cuota = 1-(1+TMV)**(-cuotas)
    cuota= cuota / TMV
    cuota= saldo_a_financiar / cuota
    #amortizacion  
    datos = []

    for i in range (1,cuotas+1):
        if i == cuotas:
            valor_interes=round(saldo_a_financiar*TMV,2) 
            tabla=(i,round(saldo_a_financiar,2),valor_interes,round(saldo_a_financiar+valor_interes,2),0.00)
            datos.append(tabla)
        else:  
            valor_interes=round(saldo_a_financiar*TMV,2)
            capital_abonado=round(cuota)-valor_interes
            saldo_a_financiar=saldo_a_financiar - capital_abonado
            tabla=(i,round(capital_abonado,2),valor_interes,round(cuota,0),round(saldo_a_financiar,2))
            datos.append(tabla)
    
    dicionario = {
        "saldo financiar": nuevo,
        "cuota": round(cuota,0),
        "amortizacion": datos
    }
    
    return dicionario
    

print(simulador_prestamo_baniscutp({"prestamo": 2000000.0,"gastos documentacion": 0.0,"cuotas": 6,"interes anual": 28.99}))
print(simulador_prestamo_baniscutp({ "prestamo": 1200000.0, "gastos documentacion": 100000.0, "cuotas": 12, "interes anual": 25.13 }))

venta = { "prestamo": 2000000.0, "gastos documentacion": 0.0, "cuotas": 6, "interes anual": 28.99 }
print(simulador_prestamo_baniscutp(venta))

venta = { "prestamo": 1200000.0, "gastos documentacion": 100000.0, "cuotas": 12, "interes anual": 25.13 }
print(simulador_prestamo_baniscutp(venta))
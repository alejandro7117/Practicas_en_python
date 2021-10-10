def compra_camisas(valor_camisas,cantidad_camisas):
    #validar
    if cantidad_camisas <= 0:
        return"Opción invalida"
    #_____________________________________________________________________________
    # algoritmo
    total_comprado = cantidad_camisas * valor_camisas

    if cantidad_camisas  >= 3:
        descuento_20 = total_comprado * 20 // 100
        total = total_comprado - descuento_20
        return f"el valor a pagar son {total}"
    elif cantidad_camisas <= 2:
        descuento_10 = total_comprado * 10 // 100
        total_1 = total_comprado - descuento_10
        return f"el valor a pagar son {total_1}"

print(compra_camisas(5000,5))
print(compra_camisas(5000,2))
print(compra_camisas(5000,0))
print(compra_camisas(5000,1))
print(compra_camisas(5000,-2))




    
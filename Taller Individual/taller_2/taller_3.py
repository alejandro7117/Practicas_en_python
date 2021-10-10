def aplicar_iva(cantidad_sin_iva,iva = 21):
    return cantidad_sin_iva + cantidad_sin_iva * iva // 100

print(aplicar_iva(2500,19))
print(aplicar_iva(2500))
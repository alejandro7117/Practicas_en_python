def descuento_articulo(articulo):
    if articulo < 0 or articulo is float(articulo):
        return "opcion invalido, ingrese un valor entero positivo"


    mensaje = "el valor de descuento es"

    if articulo > 0 and articulo <= 100000:
        descuento1 = articulo
        return f"{mensaje} {descuento1}"
    elif articulo > 100000 and articulo <= 225000:
        descuento2 = round(articulo * 0.015)
        return f"{mensaje} {descuento2}"
    elif articulo > 225000 and articulo <= 375000:
        descuento3 = round(articulo * 0.038) 
        return f"{mensaje} {descuento3}"
    else:
        descuento4 = round(articulo * 0.015)
        return f"{mensaje} {descuento4}"


print(descuento_articulo(50000))
print(descuento_articulo(150000))
print(descuento_articulo(230000))
print(descuento_articulo(400000))
print(descuento_articulo(1))
print(descuento_articulo(0))
print(descuento_articulo(-20000))
print(descuento_articulo(150.000))




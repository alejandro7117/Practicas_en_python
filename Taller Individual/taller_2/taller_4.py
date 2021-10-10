def area_circulo(radio):
    PI = 3.1415
    return PI * radio ** 2

def volumen_del_cilindro(radio,altura):
    return area_circulo(radio) * altura

print(volumen_del_cilindro(4,8))



import math

def camas_a_mover(camas_actuales,ocupacion_actual,ocupacion_esperada = 70):
    camas_ocupadas = math.ceil(camas_actuales * (ocupacion_actual / 100))
    z = math.ceil(camas_ocupadas * (100 / ocupacion_esperada))
    camas_uci_a_mover = math.ceil(z - camas_actuales)
    return(f"las camas uci a mover para bajar la cupacion a {ocupacion_esperada}% son {camas_uci_a_mover} camas")


print(camas_a_mover(100,90))
print(camas_a_mover(257,80.25,68.5))
print(camas_a_mover(350,100,1))

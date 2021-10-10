
def nacimineto():
    print("Ingresa tu fecha de nacimiento en el siguiente formato")
    usuario = input("dd/mm/aaaa: ")
    a=usuario[6:]
    if a >= 1700 and a <= 1799:
        a= +5
    elif a >= 1800 and a <= 1899:
        a= +3
    elif a >= 1900 and a <= 1999:
        a= +1
    elif a >= 2000 and a <= 2099:
        a= 0
    elif a >= 2100 and a <= 2199:
        a= -2
    elif a >= 2200 and a <= 2299:
        a= -4   
    
    

print(nacimineto())
#2
b=usuario[8:]
B=(b//4) + b

#3

#4




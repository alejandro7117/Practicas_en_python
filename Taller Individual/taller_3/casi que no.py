def numero_par(numero):
    #validar
    if  numero < 10 or numero > 99 or numero is float(numero) :
        return (f"{numero} Opción inavlida. Igrese un numero entero de dos digitos")
    
    numero_total = str(numero)
    numero_1 = numero_total[0]
    numero_2 = numero_total[1]

    if numero % 2 == 0:
        if int(numero_1) % 2 == 0 and int(numero_2) % 2 == 0:
            return f"{numero}:es par     {numero_1}:es par          {numero_2}:es par "
        elif int(numero_1) % 2 == 0 and int(numero_2) % 2 != 0:
            return f"{numero}:es par     {numero_1}:es par          {numero_2}:no es par "
        elif int(numero_1) % 2 != 0 and int(numero_2) % 2 == 0:
            return f"{numero}:es par     {numero_1}:no es par          {numero_2}:es par "
        elif int(numero_1) % 2 != 0 and  int(numero_2) % 2 != 0:
            return f"{numero}:es par     {numero_1}:no es par          {numero_2}:no es par "
    
    else:
        if int(numero_1) % 2 == 0 and int(numero_2) % 2 == 0:
            return f"{numero}:no es par     {numero_1}:es par          {numero_2}:es par "
        elif int(numero_1) % 2 == 0 and int(numero_2) % 2 != 0:
            return f"{numero}:no es par     {numero_1}:es par          {numero_2}:no es par "
        elif int(numero_1) % 2 != 0 and int(numero_2) % 2 == 0:
            return f"{numero}:no es par     {numero_1}:no es par          {numero_2}:es par "
        elif int(numero_1) % 2 != 0 and  int(numero_2) % 2 != 0:
            return f"{numero}:no es par     {numero_1}:no es par          {numero_2}:no es par "


# SEGUNDA FORMA DE REALIZARLO
   # if int(numero_1) % 2 == 0 and int(numero_2) % 2 == 0:
    #    if (numero) % 2 == 0:
     #       return f"{numero} es par     {numero_1}: es par          {numero_2}: es par "
      #  else:
       #     return f"{numero} no es par  {numero_1}: es par          {numero_2}: es par "

    #if int(numero_1) % 2 == 0 and int(numero_2) % 2 != 0:
     #   if (numero) % 2 == 0:
      #      return f"{numero} es par     {numero_1}: es par          {numero_2}:no es par "
       # else:
        #    return f"{numero} no es par  {numero_1}: es par      {numero_2}: no es par"

    #if int(numero_1) % 2 != 0 and int(numero_2) % 2 == 0:
     #   if (numero) % 2 == 0:
      #      return f"{numero} es par     {numero_1}:no es par          {numero_2}: es par "
       # else:
        #    return f"{numero} no es par {numero_1}: no es par       {numero_2}: es par"

    #if int(numero_1) % 2 != 0 and  int(numero_2) % 2 != 0:
     #   if (numero) % 2 == 0:
      #      return f"{numero} es par     {numero_1}: no es par          {numero_2}:no es par "
       # else:
        #    return f"{numero} no es par y ninguno de los dos digitos son  pares"
    
print(numero_par(0))
print(numero_par(10))
print(numero_par(99))
print(numero_par(100))
print(numero_par(30))
print(numero_par(2.5))
print(numero_par(-20))
print(numero_par(24))
print(numero_par(27.8))
def notas(nota1,nota2,nota3):
    notas_x = nota1 or nota2 or nota3
    if notas_x < 0 or notas_x > 5:
        return "invalido"
    
    else:
        if float(notas_x) > 0 or float(notas_x)  <= 5:
            promedio = (nota1 + nota2 + nota3) // 3
        if promedio > 3:
            return f"su promedio fue {promedio}  Aprobo" 
        else:
            return f"su promedio fue {promedio}  Reprobo"

print(notas(0,9,4))
print(notas(-7,4,1))
print(notas(8,2,1))
print(notas(2.5,5.0,3.5))
print(notas(4,3.5,4))
print(notas(4.0,4.5,5.0))
print(notas(4,5,4))






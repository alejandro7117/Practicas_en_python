def funcion_cuadratica(a,b,c):
    if b**2 -(4*a*c) <= 0 and a != 0:
        return "sin solución"
    else:
        from math import sqrt

        x_positivo = (-b + sqrt(b**2-(4*a*c)))/(2*a)
        x_negativo = (-b - sqrt(b**2-(4*a*c)))/(2*a)
        return f"las solucion de la ecuacion:\n{x_positivo}\n{x_negativo}"

print(funcion_cuadratica(3,4,6))
print(funcion_cuadratica(1,-5,6))
print(funcion_cuadratica(2,-7,3))
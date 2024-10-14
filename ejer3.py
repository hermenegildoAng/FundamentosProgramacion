"""
    git push origin master (para subir)
    programa que calcula la hipotenuisa de un triangulo rectangulo
    a partir de sus catetos
    entradas: 
        c1: int
        c2: int
    salidas
        hipotenusa
"""
import math
cateto1 = int(input("Ingrese el valor del cateto 1: "))

cateto2 = int(input("Ingrese el valor del cateto 2: "))

hipotenusa = cateto1 * cateto1 + cateto2 * cateto2

hipotenusa = math.sqrt(hipotenusa)

print("El valor de la Hipotenusa es: ", round(hipotenusa,2))


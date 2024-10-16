'''
Pide al usuario dos pares de numeros  que representen 2 puntos en el plano
calcular y mostrar distancia
'''
import math
x1 = int(input("Escribe el primer numero del primer par (x1): "))
y1 = int(input("Escribe el segundo numero del primer par (y1): "))
x2 = int(input("Escribe el primer numero del segundo par (x2): "))
y2 = int(input("Escribe el segundo numero del segundo par par (y2): "))

distancia = (x2 - x1)**2 + (y2 - y1)**2
distancia = math.sqrt(distancia)

print("La distancia entre los 2 puntos es: ",distancia)
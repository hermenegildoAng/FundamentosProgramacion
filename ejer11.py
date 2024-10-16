'''
pide al usuario 2 numeros y muestra la distncia entre ellos
'''

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el primer segundo: "))

distancia = n1 - n2

if distancia < 0:
    distancia = distancia * (-1)

print("La distancia entre: ",n1," y: ",n2," es de: ",distancia)
'''
leer un numero de 2 cifras y regresar el invertido
'''

n = int(input("Escriba un numero de 2 cifras: "))

decimales = n//10
unidades = n%10

ninvert = (unidades*10)+decimales

print("El numero invertido de ",n," es: ",ninvert)

'''
calcular promedio de 3 numeros dados por teclado

'''

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

prom = (n1 + n2 + n3 )/3

print("La media de los 3 numeros es: ", round(prom, 2))
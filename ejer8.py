'''
un vendedor rrecibe un sueldo base mas 10% extra por comision de 
sus ventas, el vendedor desea saber cuanto dinero obtendra por concepto de comiciones
por las 3 ventas realizadas en el mes y el total que recibira en el mes tomando
en cuenta el sueldo base y comiciones
'''

venta1 = int(input("Ingrese el valor de la venta 1: "))
venta2 = int(input("Ingrese el valor de la venta 2: "))
venta3 = int(input("Ingrese el valor de la venta 3: "))

totalventas = venta1 + venta2 + venta3
comision = totalventas * 0.1

sueldob = int(input("Ingrese su sueldo base: "))

sueldototal = sueldob + comision

print("Su sueldo total es: ", sueldototal)



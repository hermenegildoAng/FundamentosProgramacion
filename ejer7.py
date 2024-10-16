''''
    programa que reciba una cantidad de minutos y muestre
    cuantas horas y minutos son
'''

minutos = int(input("Ingrese los minutos: "))

hrs = minutos // 60
mint = minutos % 60

print("Son : ", hrs ," hora con: ",mint, " minutos")

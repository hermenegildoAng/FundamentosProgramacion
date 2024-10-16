'''
alumno desea saber su calificacion final
'''

parcial1 = int(input("Escriba la calificacion del parcial 1: "))
parcial2 = int(input("Escriba la calificacion del parcial 2: "))
parcial3 = int(input("Escriba la calificacion del parcial 3: "))

totalp = (parcial1 + parcial2 + parcial3)/3
porcentajeparcial = (totalp * 55)/100

examen = int(input("Escriba la calificacion del examen: "))
porcentaE = examen * 30 / 100

tfinal = int(input("Escriba la calificacion del trabajo final: "))
porcentajeT = tfinal * 15 / 100

calificacionF = porcentajeparcial + porcentaE + porcentajeT

print("Su calificacion final es: ", round(calificacionF,2))
"""
    programa que caalcule area y perimetro
    base: integer
    altura: integer
"""
print("Calcular area de rectangulo ")

altura = input("Escribe la altura: ")
altura = int(altura)
base = input("Escribe la base: ")
base = int(base)

area = altura * base 
perimetro = altura * 2 + base * 2

print("El area del rectangulo es: " , area ) 
print("Y el perimetro del rectangulo es: " , perimetro)
    

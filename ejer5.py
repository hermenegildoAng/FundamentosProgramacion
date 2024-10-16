"""
    programa que convierta grados farenheit a celsius
"""

gfaren = int(input("Ingrese los grados farenheit: "))

gcelsius = (gfaren - 32) * (5/9)

print("Los grados celsius son: ", round(gcelsius, 2))


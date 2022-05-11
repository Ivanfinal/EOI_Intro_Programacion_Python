import math

altura = float(input("Introduce altura: "))
radio = float(input("Introduce radio: "))
area = 2 * radio * (altura + radio) * math.pi
volumen = radio**2 * altura * math.pi
print(f"Su area es: {round(area,1)}, y su volumen es: {round(volumen,1)}")
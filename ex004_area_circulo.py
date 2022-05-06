from math import pi
radio = float(input("Ingrese el radio del circulo:"))

area = round(pi * (radio ** 2),12)

#print(type(area))4

print(f"Area: {area:g}") #:g redondea a 4 decimales
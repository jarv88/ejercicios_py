#Calcular el Volumen de una Esfera a partir del Radio Dado
from math import pi

radio = int(input("Radio: "))

volumen_esfera = (4 * pi * (radio**3))/3

print(volumen_esfera)
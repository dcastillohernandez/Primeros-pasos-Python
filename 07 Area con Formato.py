#Programa que muestra el área con formato.

from math import pi

radio=float(input('Dame el radio: '))
area=pi*radio**2

print("El área de un círculo de radio %f es %f" %(radio,area))
print("El área de un círculo de radio %6.3f es %6.3f" %(radio,area))
# Programa para calcular el Volumen de una esfera
from math import pi

print('Programa para el cálculo del volumen de una esfera.')

radio=float(input('Dame el radio (en metros): '))
volumen=4.0/3.0*pi*radio**3

print('Volumen de la esfera: ',volumen,'(metros cúbicos)')

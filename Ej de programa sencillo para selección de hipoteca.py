#Programa para selección de una hipoteca.
#Autor: Dayron Castillo.
#Fecha: 10/6/2022.

print("Comprobador de elejibilidad 101")

#Entrada de datos:
name=input("Por favor, introdusca su nombre:").title()
age=int(input("Por favor, introdusca su edad: "))
salario=int(input("Por favor, ¿Cual es su salario?: "))

#Proceso de elegivilidad.
min_salario=5000
if age < 61 and age > 17:
    print(f"sr.{name}, usted cumple con la edad establecida.")
else:
    print(f"sr. {name} usted no cumple con el estandar de edad 18-60 años.")

#Impresion por pantalla.
if salario >= min_salario and age >= 61 and age<=17:
    print(f"Felicitaciones {name}, usted es elegible para una hipoteca.")
else:
    print(f"{name}, parece que no puede ser elegible en este momento.")

print(f"Muchas gracias {name} por elegir nuestro banco.")



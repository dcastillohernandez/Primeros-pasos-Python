#Ejemplo de un sencillo comprobador de elegibiliada para ver si una persona es apta para un sevicio o no.
#Auton: Dayron Castillo.
#Fecha:10/6/2022

#Impresión en pantalla de presentación.
print("¡Bienvenido a nuestro verificador de elegivilidad en línea!")

#Entrada de datos por el usuario.
age=int(input("Introduce tu edad: "))
has_license=(input("¿Tiénes licensia? [S/N]: ")).lower()
salario=int(input("Su salario mensual $: "))
correo=input("Teclee su correo electrónico(revisar bien antes de aseptar): ")

#Proceso de selección.
if age >= 20 and age <=35:
    print("¡La edad está bien!")
else:
    print("No cumple con la edad")

if has_license != "s":
    print("Lo siento pero necesitas tener una licensia válida (responda 's' (para si), y 'n' (para no)")
else:
   has_license=True
   print("Tiene licencia válida!")

if salario >=3500:
    print("El salario esta bien!")
else:
    print("lo siento pero su salario está por debajo de nuetro requisito mínimo")

#Impresion por pantalla.
print(f"Si usted cumple con los 3 requisitos le contactaremos por su gmail {correo}, de lo contrario queda descalificado.")
print("Muchas Gracias!")












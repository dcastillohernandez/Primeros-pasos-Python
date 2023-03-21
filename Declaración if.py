#Declaración if y else.

password=input("Crea una contraseña: ")
print("Bienvenido al portal.")

password_check=input("Por favor, introdusca su contraseña: ")

if password_check==password:
    print("¡Exitoso! ¡Bienvenido de nuevo!")
else:
    print("Lo siento! Contraseña errónea.")
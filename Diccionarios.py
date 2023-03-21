#Diccionarios, algunos ejemplos de usos.



amigo={
    "nombre":"James",
    "edad":"30",
    "correo electronico":"perezperz@gmail.com",
    "coche":"Tesla t1"
}

#impresion en pantalla, usando cadena formateada puedo usar todos los valores a mi antojo.
print(f"Señor",amigo["nombre"],"gracias por solicitar nuestros servicios.")
print(f"Se le contactará por medio de su correo",amigo["correo electronico"])

#Modificar valores de los diccionarios.
amigo["edad"]=60
print(amigo["edad"])

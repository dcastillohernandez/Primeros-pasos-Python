#Ejemplo del bucle while.
#Adivinar un numero (entero) solo con 3 intentos.

my_number=19
guess=0
max_guess=3

while guess<max_guess:
    number=int(input("Adivida el número: "))
    guess+=1
    if number==my_number:
        print("¡wow! ¡Mirate un genio!")
        break
    else:
        print("¡No! ¡Ni en un millon de años! ¡Intentelo de nuevo!")
else:
    print("Se te acabaron las posibilidades")



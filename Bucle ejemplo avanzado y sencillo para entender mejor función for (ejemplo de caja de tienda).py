#Queremos calcular un precio(ejemplo) final como si fuera una caja de una tienda.

prices=[5,10,15,20,25]
total=0
for item in prices:
    total+=item
print(f"Su precio total es ${total}")
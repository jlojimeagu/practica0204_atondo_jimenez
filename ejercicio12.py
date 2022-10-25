#Escribir un programa en el que se
# pregunte al usuario por una frase y una letra, y muestre
# por pantalla el número de veces que aparece
# la letra en la frase.
frase = input("indica una frase\n")
letra = input("introduce letra\n")
contador = 0
for pata in frase:
    if pata == letra:
        contador = contador + 1
print("la cantida", contador, "que se repite la letra en", frase)
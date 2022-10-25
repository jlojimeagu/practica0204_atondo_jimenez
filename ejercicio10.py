#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por
# la contraseña hasta que introduzca la contraseña correcta.
while True:
    password = input("introduzca la contaseña\n")
    if password=="patata":
        print("contaseña correcta")
        break
    else:
        print("contraseña incorrecta")

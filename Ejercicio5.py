nombre = input("Introduce el nombre\n")
sexo = input("Introduce el sexo(H o M)\n")

if sexo == "M":
    if nombre[0].lower() < "m":
        print("Grupo A")

    else:
        print("Grupo B")

else:
    if nombre[0].lower() < "n":
        print("Grupo B")

    else:
        print("Grupo A")


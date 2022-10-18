edad = float(input("edad del usuario:\n"))
ingreso = float(input("cuanto es tu ingreso:\n"))
if edad > 16 and ingreso >= 1000:
    print("tributas")
elif edad <= 16 and ingreso < 1000:
    print("no tributas")
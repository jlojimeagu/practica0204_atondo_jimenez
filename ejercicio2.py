#Escribir un programa que pida al usuario dos números
#y muestre por pantalla su división. Si el divisor es cero
#el programa debe mostrar un error.
while True:
    dividendo = float(input("digame el numero a dividir\n"))
    divisor = float(input("digame el numero que lo divide\n"))
    if divisor == 0:
        print("ERROR")
    else:
        division = dividendo/divisor
        print("el resultado es\n", division)
        break
numero = int(input("Introduce la altura del triángulo\n"))

for valor in range(1, numero+1, 2):

    for num in range(valor, 0, -2):
        print(num, end=" ")

    print("")

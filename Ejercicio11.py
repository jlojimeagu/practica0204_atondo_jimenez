palabra = input("Introduce una palabra\n")

for letra in range(len(palabra)-1, -1, -1):
    print(palabra[letra])

password = "contraseña"

user_password = input("Introduce contraseña:\n")

if user_password.lower() == password.lower():
    print("La contraseña es CORRECTA")

else:
    print("La contraseña es ERRONEA")


"""
Ej 2.3.5 - Escribir un programa que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!".
"""

PASSWORD = "1234"

def pedir_contrasena() -> str:
    contrasena = input("Password? ")
    if contrasena != PASSWORD:
        raise NameError("Incorrect Password!!")
    return contrasena


def main():
    try:
        pedir_contrasena()
        print("Yeah! you know your own password!")
    except NameError as e:
        print(e)


if __name__ == "__main__":
    main()

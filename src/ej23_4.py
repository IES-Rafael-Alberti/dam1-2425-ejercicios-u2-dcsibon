"""
Ej 2.3.4 - Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""

def pedir_entero() -> int:
    try:
        numero = int(input("Introduce un número entero: "))
        return numero
    except ValueError:
        print("La entrada no es correcta")
        raise  # Vuelve a lanzar la excepción capturada


def main():
    try:
        numero = pedir_entero()
        print(f"El número introducido es: {numero}")
    except ValueError:
        print("*ERROR* Se ha capturado la excepción ValueError.")


if __name__ == "__main__":
    main()

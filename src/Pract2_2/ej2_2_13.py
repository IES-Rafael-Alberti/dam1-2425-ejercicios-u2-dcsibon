"""
Ejercicio 2.2.13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

import os
from ej2_23 import borrarConsola


def ecoConsola(entrada: str):
    if entrada.strip().lower() == "salir":
        return True
    else:
        return False


def main():
    borrarConsola()

    print("Soy el eco.. háblame o escribe salir:")

    salir = False
    while not salir:
        entrada = input()
        salir = ecoConsola(entrada)
        if not salir:
            print(entrada)


if __name__ == "__main__":
    main()

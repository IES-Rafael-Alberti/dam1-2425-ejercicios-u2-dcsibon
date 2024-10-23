"""
Ejercicio 2.2.1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

import os

def repetirPalabra(palabra):
    for i in range(1, 10):
        palabra += palabra + "\n"


def borrarConsola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def main():
    borrarConsola()
    palabra = input("Introduzca una palabra: ").replace(" ", "")
    print(repetirPalabra(palabra))


if __name__ == "__main__":
    main()
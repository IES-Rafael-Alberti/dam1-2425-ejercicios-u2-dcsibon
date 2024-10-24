"""
Ejercicio 2.2.4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

import os
from ej2_23 import pedirNumeroEnteroPositivo, borrarConsola


def crearSerie(numero):
    serie = ""
    for i in range(numero, -1, -1):
        serie += str(i)
        if i > 0:
            serie += ", "
    return serie


def main():
    borrarConsola()
    numero = pedirNumeroEnteroPositivo("Introduzca un entero positivo: ")
    
    print(crearSerie(numero))


if __name__ == "__main__":
    main()
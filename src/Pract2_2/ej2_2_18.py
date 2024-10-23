"""
Ejercicio 2.2.18
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
"""

from ej2_23 import borrarConsola, esPar
from ej2_28 import pedirNumeroEntero


def sumarDigitos(numero):
    suma = 0

    entrada = str(numero)
    for i in range(0, len(entrada)):
        suma += int(entrada[i])

    return suma


def main():
    borrarConsola()

    totalNumerosPares = 0

    print("Introduzca números enteros positivos...")

    while True:
        numero = pedirNumeroEntero("")
        if numero >= -1:
            if numero == -1:
                break
            elif esPar(numero):
                totalNumerosPares += 1
            print(f"La suma de sus dígitos es {sumarDigitos(numero)}")

    print(f"\nTotal de números pares => {totalNumerosPares}\n")


if __name__ == "__main__":
    main()

"""
Ejercicio 2.2.15
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
"""

from ej2_23 import borrarConsola


def leeNumero():
    numero = int(input())
    if numero >= 0:
        return numero
    else:
        return -1


def main():
    borrarConsola()

    print("Introduzca números...")

    total = 0
    while True:
        numero = leeNumero()
        if numero > 0:
            total += numero
        elif numero == 0:
            break

    print(f"\n{total}\n")


if __name__ == "__main__":
    main()

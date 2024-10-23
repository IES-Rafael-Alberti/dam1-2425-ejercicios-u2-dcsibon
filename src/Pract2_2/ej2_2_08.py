"""
Ejercicio 2.2.8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

import os
from ej2_23 import borrarConsola, esPar


def comprobarNumero(entrada):
    return entrada.replace("-", "").isnumeric()


def pedirNumeroEntero(mensaje: str):
    entrada = input(mensaje).replace(" ", "")
    
    while not comprobarNumero(entrada):
        entrada = input("**ERROR**, vuelva a intentarlo\n" + mensaje).replace(" ", "")
    
    return int(entrada)


def construirFila(numero, fin, signo):
    fila = ""
    for i in range(numero, fin, -2):
        fila += str(i * signo) + " "

    return fila


def construirTriangulo(numero):
    if numero > 0:
        signo = 1
    else:
        signo = -1

    if esPar(numero):
        inicio = 0
    else:
        inicio = 1

    numero = abs(numero)

    triangulo = ""
    for i in range(inicio, numero + 1, 2):
        triangulo += construirFila(i, inicio - 1, signo) + "\n"

    return triangulo

def main():
    borrarConsola()
    numero = pedirNumeroEntero("Introduzca un número entero: ")
    print(construirTriangulo(numero))
    

if __name__ == "__main__":
    main()

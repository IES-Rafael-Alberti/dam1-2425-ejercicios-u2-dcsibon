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
import time

def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def es_par(num: int) -> bool:
    return num % 2 == 0


def comprobar_numero(entrada):
    return entrada.replace("-", "").isnumeric()


def pedir_numero_entero(mensaje: str) -> int:
    entrada = input(mensaje).replace(" ", "")
    
    while not comprobar_numero(entrada):
        entrada = input("**ERROR**, vuelva a intentarlo\n" + mensaje).replace(" ", "")
    
    return int(entrada)


def pedir_numero_entero_v2(mensaje: str) -> int:
    entrada_valida = False
    while not entrada_valida:
        entrada = input(mensaje).replace(" ", "")
        if entrada == "":
            # Retorno el valor None para marcar que termina el programa...
            return None
        else:
            try:
                num = int(entrada)
            except ValueError:
                print("**ERROR**, vuelva a intentarlo\n")
            else:
                entrada_valida = True
    
    return num


def construir_fila(numero, fin, signo):
    fila = ""
    for i in range(numero, fin, -2):
        fila += str(i * signo) + " "

    return fila


def construir_triangulo(numero):
    if numero > 0:
        signo = 1
    else:
        signo = -1

    if es_par(numero):
        inicio = 0
    else:
        inicio = 1

    numero = abs(numero)

    triangulo = ""
    for i in range(inicio, numero + 1, 2):
        triangulo += construir_fila(i, inicio - 1, signo) + "\n"

    return triangulo


def main():
    salir = False    

    while not salir:
        borrar_consola()

        numero = pedir_numero_entero_v2("Introduzca un número entero: ")
        
        if numero is None:
            salir = True
        else:
            print("\n" + construir_triangulo(numero))
            input("Presione una tecla para continuar...\n")
    

    borrar_consola()
    print("\n\nBye, bye...\n\n")
    time.sleep(2)
    borrar_consola()


if __name__ == "__main__":
    main()

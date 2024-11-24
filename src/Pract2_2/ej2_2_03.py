"""
Ejercicio 2.2.3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

import os

def comprobarNumero(entrada):
    return entrada.isnumeric() and int(entrada) > 0


def pedirNumeroEnteroPositivo(mensaje: str):
    entrada = input(mensaje).replace(" ", "")
    
    while not comprobarNumero(entrada):
        entrada = input("**ERROR**, vuelva a intentarlo\n" + mensaje).replace(" ", "")
    
    #Retornamos el número entero positivo introducido
    return int(entrada)


def crearSerie(numero):
    serie = ""
    for i in range(1, numero, 2):
        serie += str(i)
        if i < numero - 1:
            serie += ", "
    return serie


def esPar(numero):
    return numero % 2 == 0


def borrarConsola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def main():
    borrarConsola()
    numero = pedirNumeroEnteroPositivo("Introduzca un entero positivo: ")
    
    if not esPar(numero):
        numero += 1
    
    print(crearSerie(numero))


if __name__ == "__main__":
    main()
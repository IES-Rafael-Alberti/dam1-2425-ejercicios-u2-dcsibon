
import os


def borrarConsola():
    """
    Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def generarFila(num, res):
    """
    Crea una fila de la pirámide de sumas

    Parámetros
    ----------
    int
        un número por el que empezar la serie de la fila
    str
        la cadena de caracteres que acumulará todas las filas de la pirámide

    Retorna
    -------
    str
        la cadena de caracteres de la pirámide con la fila acumulada como otra línea
    """
    total = 0
    res += str(num) + " => " + str(num) + " "
    
    for i in range(num - 1, -1, -1):
        res += f"+ {i} "
        total += i
    
    if num != 0:
        res += f"= {total}"
    res += "\n"
    
    return res


def piramide(num: int):
    """
    Crea una pirámide de sumas de un número

    Parámetros
    ----------
    int
        un número, que será el valor máximo de la pirámide de sumas

    Retorna
    -------
    str
        la cadena de caracteres con la pirámide de sumas
    """
    res = ""

    while num >= 0:
        res = generarFila(num, res)
        num -= 1

    return res


def main():

    repetir = True
    while repetir:
        borrarConsola()

        num = int(input("Introduzca un número: "))

        while abs(num) > 100:
            num = int(input("**Error** Introduzca un número entre -100 y 100: "))

        print("\nSu pirámide de sumas es la siguiente:\n" + piramide(abs(num)))

        repetir = input("¿Quiere hacer otra pirámide? (s/n) ").replace(" ", "").upper()[0:1] == "S"


if __name__ == "__main__":
    main()
















































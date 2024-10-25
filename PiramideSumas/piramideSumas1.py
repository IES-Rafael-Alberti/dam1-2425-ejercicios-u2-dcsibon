
import os


def borrar_consola():
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


def pedir_numero(msj: str) -> int:
    numero_correcto = False
    while not numero_correcto:
        num = None
        
        try:
            num = int(input(msj).strip())
            if num < 0:
                raise ValueError("El número debe ser positivo")
            if num > 100:
                raise ValueError("El número debe estar entre el 0 y el 100")
        except ValueError as e:
            if num is None:
                print("*ERROR* No es un número entero. Inténtelo otra vez!")
            else:
                print(f"*ERROR* {e}. Inténtelo otra vez!")
        else:
            numero_correcto = True

    return num


def pedir_respuesta(msj: str) -> str:
    respuesta_correcta = False
    while not respuesta_correcta:
        try:
            respuesta = input(msj).replace(" ", "").upper()
            if respuesta == "" or not respuesta in "SN":
                raise ValueError("Respuesta incorrecta")
        except ValueError as e:
            print(f"*ERROR* {e}")
        else:
            respuesta_correcta = True

    return respuesta == "S"


def main():
    borrar_consola()
    repetir = True

    while repetir:
        num = pedir_numero("Introduzca un número: ")
        borrar_consola()
        
        print("\nSu pirámide de sumas es la siguiente:\n\n" + piramide(num))

        repetir = pedir_respuesta("¿Quiere hacer otra pirámide? (s/n) ")
        borrar_consola()

    print("\n\nBye, bye!!\n\n")
    

if __name__ == "__main__":
    main()

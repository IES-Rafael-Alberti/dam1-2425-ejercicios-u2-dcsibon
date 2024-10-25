
import os

MAXIMO_VALOR = 20


def borrar_consola():
    """
    Limpia la consola.
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def generar_fila_creciente_v2(fila_num: int) -> str:
    """
    Genera una fila de la pirámide en formato creciente.
    
    Args:
        fila_num (int): Número de la fila actual.
        
    Returns:
        str: La fila de la pirámide en formato creciente.
    """
    res = f"{fila_num} => {fila_num} "
    total = fila_num
    cont = fila_num - 1
    while cont >= 1:
        res += f"+ {cont} "
        total += cont
        cont -= 1
    res += f"+ 0 = {total}\n"
    return res


def generar_fila_decreciente_v2(fila_num: int) -> str:
    """
    Genera una fila de la pirámide en formato decreciente.
    
    Args:
        fila_num (int): Número de la fila actual.
        
    Returns:
        str: La fila de la pirámide en formato decreciente.
    """
    res = f"{fila_num} => 0 "
    total = 0
    cont = 1
    while cont <= fila_num:
        res += f"+ {cont} "
        total += cont
        cont += 1
    res += f"= {total}\n" if fila_num != 0 else "\n"
    return res


def generar_fila_creciente(fila_num: int) -> str:
    """
    Genera una fila de la pirámide en formato creciente.
    
    Args:
        fila_num (int): Número de la fila actual.
        
    Returns:
        str: La fila de la pirámide en formato creciente.
    """
    res = f"{fila_num} => {fila_num} "
    total = fila_num
    for cont in range(fila_num - 1, 0, -1):
        res += f"+ {cont} "
        total += cont
    res += f"+ 0 = {total}\n"
    return res


def generar_fila_decreciente(fila_num: int) -> str:
    """
    Genera una fila de la pirámide en formato decreciente.
    
    Args:
        fila_num (int): Número de la fila actual.
        
    Returns:
        str: La fila de la pirámide en formato decreciente.
    """
    res = f"{fila_num} => 0 "
    total = 0
    for cont in range(1, fila_num + 1):
        res += f"+ {cont} "
        total += cont
    res += f"= {total}\n" if fila_num != 0 else "\n"
    return res


def piramide_creciente(num: int) -> str:
    """
    Genera una pirámide en formato creciente hasta un número dado.
    
    Args:
        num (int): Número de filas de la pirámide.
        
    Returns:
        str: La pirámide en formato creciente.
    """
    res = ""
    for fila_num in range(1, num + 1):
        res += generar_fila_creciente(fila_num)
    return res


def piramide_decreciente(num: int) -> str:
    """
    Genera una pirámide en formato decreciente desde un número dado.
    
    Args:
        num (int): Número de filas de la pirámide.
        
    Returns:
        str: La pirámide en formato decreciente.
    """
    res = ""
    for fila_num in range(num, -1, -1):
        res += generar_fila_decreciente(fila_num)
    return res


def piramide(num: int) -> str:
    """
    Genera una pirámide combinando el formato decreciente y creciente.
    
    Args:
        num (int): Número de filas de la pirámide.
        
    Returns:
        str: La pirámide completa.
    """
    res = piramide_decreciente(num)
    res += piramide_creciente(num)
    return res


def pedir_numero(msj: str) -> int:
    numero_correcto = False
    while not numero_correcto:
        num = None
        
        try:
            num = int(input(msj).strip())
            if num < 0:
                raise ValueError("El número debe ser positivo")
            if num > MAXIMO_VALOR:
                raise ValueError(f"El número debe estar entre el 0 y el {MAXIMO_VALOR}")
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
















































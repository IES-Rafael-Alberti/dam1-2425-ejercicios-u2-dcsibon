
import os

MAXIMO_VALOR = 20


def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def piramide_decreciente(num: int):
    res = ""
    while num >= 0:
        cont = 1
        total = 0
        res += str(num) + " => 0 "
        while cont <= num:
            res += f"+ {cont} "
            total += cont
            cont += 1
        if num != 0:
            res += f"= {total}"
        res += "\n"
        num -= 1
    return res


def piramide_creciente(num: int):
    res = ""
    numFila = 1
    while numFila <= num:
        cont = numFila
        total = numFila
        res += str(numFila) + f" => {numFila} "
        while cont > 1:
            cont -= 1
            res += f"+ {cont} "
            total += cont
        res += f"+ 0 = {total}\n"
        numFila += 1
    return res


def piramide(num: int):
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















































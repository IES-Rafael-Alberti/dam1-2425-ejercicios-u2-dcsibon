
import os
import random


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    
    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def dame_pista(numero: int, numero_oculto: int, intentos: int) -> str:
    pista = "el número oculto es "
    
    if numero_oculto > numero:
        pista += f"MAYOR... ¡te quedan {intentos} intentos!"
    else:
        pista += f"MENOR... ¡te quedan {intentos} intentos!"

    diferencia = abs(numero_oculto - numero)
    
    if diferencia >= 15:
        pista = "* FRÍO, FRÍO, " + pista
    elif 10 <= diferencia < 15:
        pista = "* CALIENTE, CALIENTE, " + pista
    else:
        pista = "* TE QUEMAS, " + pista

    return pista


def adivina_el_numero(numero_oculto: int, total_intentos: int):
    
    numero = numero_oculto - 1
    intentos_realizados = 0
    numero_adivinado = False

    while numero != numero_oculto and total_intentos > 0:
        intentos_realizados += 1
        total_intentos -= 1
        numero = introduce_numero_entero(f"¿Qué número es? ")
        if numero != numero_oculto and total_intentos > 0:
            print(dame_pista(numero, numero_oculto, total_intentos))
        else:
            numero_adivinado = True

    return numero_adivinado, intentos_realizados


def comprobar_numero_entero(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]
    
    return valor.isdigit()


def introduce_numero_entero(msj: str) -> int:
    valor = input(msj).strip()
    
    while not comprobar_numero_entero(valor):
        print("**ERROR** Ha introducido un número entero no válido!")
        valor = input(msj).strip()

    return int(valor)


def genera_numero_oculto(min: int, max: int) -> int:
    return random.randint(min, max)


def configurar_juego():
    minimo = 0
    maximo = 0

    while not (minimo < maximo and (maximo - minimo) >= 100):
        minimo = introduce_numero_entero("Introduce el mínimo número posible: ")
        maximo = introduce_numero_entero("Introduce el máximo número posible: ")
        if not (minimo < maximo and (maximo - minimo) >= 100):
            print("*ERROR* Debe haber por lo menos 100 números de diferencia entre ellos...\n")

    intentos = introduce_numero_entero("Introduce el número de intentos: ")

    return minimo, maximo, intentos
    
    
def main():
    limpiar_pantalla()
    print("--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---\n\n")

    print("* Primero vamos a configurar el juego...\n")
    minimo, maximo, intentos = configurar_juego()

    numero_oculto = genera_numero_oculto(minimo, maximo)

    limpiar_pantalla()
    print(f"--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n")
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos)

    if numero_adivinado:
        print(f"¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print("GAME OVER - ¡Otra vez será!")


if __name__ == "__main__":
    main()

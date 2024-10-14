import os
import random
import time


MINIMO = 0
MAXIMO = 100
FRIO = 15
CALIENTE = 5
INTENTOS = 5


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausa():
    """
    Realiza una pausa hasta que el usuario presione ENTER.

    También limpia la pantalla después de que el usuario presiona ENTER.
    """
    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()


def evaluar_distancia(numero: int, numero_oculto: int, frio: int, caliente: int) -> str:
    """
    Evalúa la distancia entre el número oculto y el ingresado, y devuelve una pista basada en la cercanía.

    Args:
        numero (int): Número ingresado por el usuario.
        numero_oculto (int): Número que debe ser adivinado.
        frio (int): Diferencia máxima para considerar la pista como "Frío".
        caliente (int): Diferencia máxima para considerar la pista como "Caliente".

    Returns:
        str: Mensaje indicando si el número está "Frío", "Caliente" o "Te Quemas".
    """
    diferencia = abs(numero_oculto - numero)
    
    if diferencia > frio:
        return "* FRÍO, FRÍO,"
    elif diferencia > caliente:
        return "* CALIENTE, CALIENTE,"
    else:
        return "* TE QUEMAS,"


def generar_pista(numero: int, numero_oculto: int, intentos: int) -> str:
    """
    Genera una pista indicando si el número oculto es mayor o menor que el número ingresado.

    Args:
        numero (int): Número ingresado por el usuario.
        numero_oculto (int): Número que debe ser adivinado.
        intentos (int): Cantidad de intentos restantes.

    Returns:
        str: Mensaje indicando si el número oculto es mayor o menor, y cuántos intentos quedan.
    """
    pista = "el número oculto es "

    if numero_oculto > numero:
        pista += "MAYOR... "
    else:
        pista += "MENOR... "

    if intentos > 1:
        pista += f"¡te quedan {intentos} intentos!\n"
    else:
        pista += f"¡te queda {intentos} intento!\n"

    return pista


def mostrar_pista(numero: int, numero_oculto: int, intentos: int, frio: int, caliente: int):
    """
    Muestra una pista combinando la distancia y si el número oculto es mayor o menor.

    Args:
        numero (int): Número ingresado por el usuario.
        numero_oculto (int): Número que debe ser adivinado.
        intentos (int): Cantidad de intentos restantes.
        frio (int): Diferencia máxima para considerar la pista como "Frío".
        caliente (int): Diferencia máxima para considerar la pista como "Caliente".
    """
    pista = generar_pista(numero, numero_oculto, intentos)
    estado_calor = evaluar_distancia(numero, numero_oculto, frio, caliente)
    print(f"\n{estado_calor} {pista}")


def adivina_el_numero(numero_oculto: int, total_intentos: int, frio: int, caliente: int):
    """
    Gestiona el proceso de adivinación del número oculto, permitiendo que el usuario ingrese números.

    Args:
        numero_oculto (int): Número que debe ser adivinado.
        total_intentos (int): Cantidad total de intentos permitidos.
        frio (int): Diferencia máxima para considerar la pista como "Frío".
        caliente (int): Diferencia máxima para considerar la pista como "Caliente".

    Returns:
        tuple: Un booleano que indica si el número fue adivinado y el número de intentos realizados.
    """
    intentos_realizados = 0
    numero_adivinado = False
    salir = False

    while not salir and total_intentos > 0:
        numero = pedir_numero_usuario("¿Qué número es? ")
        intentos_realizados += 1
        total_intentos -= 1

        if numero != numero_oculto:
            if total_intentos > 0:
                mostrar_pista(numero, numero_oculto, total_intentos, frio, caliente)
        else:
            numero_adivinado = True
            salir = True

    return numero_adivinado, intentos_realizados


def comprobar_numero_entero(valor: str) -> bool:
    """
    Verifica si el valor ingresado es un número entero válido.

    Args:
        valor (str): Valor ingresado por el usuario.

    Returns:
        bool: True si el valor es un número entero válido, False en caso contrario.
    """
    if valor.startswith("-"):
        valor = valor[1:]
    return valor.isdigit()


def pedir_numero_usuario(mensaje: str) -> int:
    """
    Solicita al usuario que introduzca un número entero válido.

    Args:
        mensaje (str): Mensaje que se muestra al usuario para pedir el número.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    salir = False
    
    while not salir:
        valor = input(mensaje).strip()
        salir = comprobar_numero_entero(valor)
        
        if not salir:
            print("\n*ERROR* Ha introducido un número entero no válido!\n")

    return int(valor)


def genera_numero_oculto(minimo: int, maximo: int) -> int:
    """
    Genera un número oculto aleatorio dentro de un rango determinado.

    Args:
        minimo (int): El valor mínimo posible.
        maximo (int): El valor máximo posible.

    Returns:
        int: Número generado aleatoriamente entre mínimo y máximo.
    """
    return random.randint(minimo, maximo)
    

def main():

    limpiar_pantalla()

    print("--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---\n\n")
    time.sleep(2)

    # Configuración inicial por defecto
    minimo = MINIMO
    maximo = MAXIMO
    frio = FRIO
    caliente = CALIENTE
    intentos = INTENTOS

    limpiar_pantalla()
    print(f"--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n")

    numero_oculto = genera_numero_oculto(minimo, maximo)
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente)

    if numero_adivinado:
        print(f"\n¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print(f"\nGAME OVER - ¡Otra vez será! (#{numero_oculto}#)")

    pausa()
    print("Bye, bye...\n\n")


if __name__ == "__main__":
    main()

import os
import random
import time


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
    if numero_oculto > numero:
        return f"el número oculto es MAYOR... ¡te quedan {intentos} intentos!\n"
    else:
        return f"el número oculto es MENOR... ¡te quedan {intentos} intentos!\n"


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
            print("\n*ERROR* Ha introducido un número entero no válido!")

    return int(valor)


def configurar_rangos_numeros() -> tuple:
    """
    Configura el rango de números válidos para el juego.

    Returns:
        tuple: El mínimo y el máximo número posibles.
    """
    salir = False

    while not salir:
        minimo = pedir_numero_usuario("Introduce el mínimo número posible: ")
        maximo = pedir_numero_usuario("Introduce el máximo número posible: ")
        
        salir = (minimo < maximo) and ((maximo - minimo) >= 100)

        if not salir:
            print("\n*ERROR* Debe haber por lo menos 100 números de diferencia entre ellos...")

    return minimo, maximo


def configurar_pistas(minimo: int, maximo: int) -> tuple:
    """
    Configura los valores de frío y caliente para las pistas.

    Args:
        minimo (int): Mínimo número del rango.
        maximo (int): Máximo número del rango.

    Returns:
        tuple: Valores para las pistas de "Frío" y "Caliente".
    """
    salir = False

    while not salir:
        frio = pedir_numero_usuario("Introduce la diferencia para mostrar la pista FRÍO, FRÍO: ")
        caliente = pedir_numero_usuario("Introduce la diferencia para mostrar la pista CALIENTE, CALIENTE: ")
        
        salir = (frio > caliente) and (minimo <= frio <= maximo) and (minimo <= caliente <= maximo)

        if not salir:
            print(f"\n*ERROR* Deben estar dentro del rango ({minimo}.{maximo}) y no ser iguales...")

    return frio, caliente


def configurar_intentos() -> int:
    """
    Configura el número de intentos para adivinar el número oculto.

    Returns:
        int: Número de intentos configurado por el usuario.
    """
    salir = False

    while not salir:
        intentos = pedir_numero_usuario("Introduce el número de intentos: ")
        
        salir = intentos > 0
        
        if not salir:
            print("\n*ERROR* El número de intentos debe ser un entero positivo...")

    return intentos


def configurar_juego() -> tuple:
    """
    Configura todos los parámetros del juego: rango de números, pistas e intentos.

    Returns:
        tuple: Mínimo, máximo, número de intentos, valor para "Frío" y valor para "Caliente".
    """
    limpiar_pantalla()
    print("--- CONFIGURA EL JUEGO DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    
    minimo, maximo = configurar_rangos_numeros()
    frio, caliente = configurar_pistas(minimo, maximo)
    intentos = configurar_intentos()

    return minimo, maximo, intentos, frio, caliente


def mostrar_configuracion(minimo, maximo, intentos, frio, caliente):
    """
    Muestra la configuración actual del juego.

    Args:
        minimo (int): Mínimo número del rango.
        maximo (int): Máximo número del rango.
        intentos (int): Número de intentos posibles.
        frio (int): Diferencia mayor para la pista "Frío".
        caliente (int): Diferencia mayor para la pista "Caliente".
    """
    limpiar_pantalla()
    print(f"--- CONFIGURACIÓN ACTUAL DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print(f"* El número oculto será un número entre {minimo} y {maximo}.")
    print(f"* El número de intentos es {intentos}.")
    print(f"* Pista FRÍO si la diferencia es mayor a {frio}.")
    print(f"* Pista CALIENTE si la diferencia es mayor a {caliente}.")
    print(f"* Pista TE QUEMAS si la diferencia es menor.")
    pausa()


def mostrar_menu():
    """
    Muestra el menú principal del juego.
    """
    limpiar_pantalla()
    print(f"--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print("1. Jugar.")
    print("2. Configurar.")
    print("3. Mostrar configuración.")
    print("4. Salir.\n")


def comprobar_opcion(opcion: int) -> bool:
    """
    Comprueba si la opción elegida está dentro del rango permitido (1-4).

    Args:
        opcion (int): Opción ingresada por el usuario.

    Returns:
        bool: True si la opción es válida, False en caso contrario.
    """
    return 1 <= opcion <= 4


def elegir_opcion_menu() -> int:
    """
    Permite al usuario elegir una opción del menú.

    Returns:
        int: La opción elegida por el usuario.
    """
    mostrar_menu()
    salir = False

    while not salir:
        opcion = pedir_numero_usuario("Elije => ")
        salir = comprobar_opcion(opcion)
        
        if not salir:
            print(f"\n*ERROR* Opción {opcion} incorrecta! (1-4)")

    return opcion


def jugar(numero_oculto, intentos, frio, caliente):
    """
    Gestiona el proceso del juego de adivinar el número oculto y muestra los resultados.

    Args:
        numero_oculto (int): Número que debe ser adivinado.
        intentos (int): Número de intentos disponibles.
        frio (int): Diferencia máxima para la pista "Frío".
        caliente (int): Diferencia máxima para la pista "Caliente".
    """
    limpiar_pantalla()
    print(f"--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n")
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente)

    if numero_adivinado:
        print(f"\n¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print(f"\nGAME OVER - ¡Otra vez será! (#{numero_oculto}#)")
    
    pausa()


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
    """
    Función principal que ejecuta el flujo completo del juego de adivinar el número oculto.
    Configura los parámetros iniciales y gestiona el bucle principal del menú.
    """
    limpiar_pantalla()
    print("--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---\n\n")
    time.sleep(2)

    # Configuración inicial por defecto
    minimo = 0
    maximo = 100
    frio = 15
    caliente = 5
    intentos = 5

    salir = False

    while not salir:
        opcion = elegir_opcion_menu()

        if opcion == 1:
            numero_oculto = genera_numero_oculto(minimo, maximo)
            jugar(numero_oculto, intentos, frio, caliente)
        elif opcion == 2:
            minimo, maximo, intentos, frio, caliente = configurar_juego()
        elif opcion == 3:
            mostrar_configuracion(minimo, maximo, intentos, frio, caliente)
        else:
            salir = True

    limpiar_pantalla()
    print("Bye, bye...\n\n")


if __name__ == "__main__":
    main()

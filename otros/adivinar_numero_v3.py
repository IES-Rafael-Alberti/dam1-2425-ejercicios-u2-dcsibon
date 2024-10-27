import os
import random
import time


TITULOS = (
    "--- SECCIÓN NO DEFINIDA ---",
    "--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---",
    "--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---",
    "--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---",
    "--- CONFIGURA EL JUEGO DE ADIVINA EL NÚMERO OCULTO ---",
    "--- CONFIGURACIÓN ACTUAL DE ADIVINA EL NÚMERO OCULTO ---",
)


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausa(tiempo = 0, tecla_enter = False, limpiar = True):
    """
    Realiza una pausa hasta que el usuario presione ENTER.

    También limpia la pantalla después de que el usuario presiona ENTER.
    """
    if tecla_enter:
        input("\nPresione ENTER para continuar...")
    elif tiempo > 0:
        time.sleep(tiempo)
    
    if limpiar_pantalla:
        limpiar_pantalla()


def mostrar_titulo(seccion: int, intentos: int = 0):
    """
    Muestra el título correspondiente a la sección del juego.

    Args:
        seccion (int): El identificador de la sección. Los valores válidos son de 1 a 5.
        intentos (int): Número de intentos que puede ser usado en el título si corresponde.
    """
    if 0 < seccion < len(TITULOS):
        if intentos > 0:
            print(TITULOS[seccion].format(intentos = intentos) + "\n\n")
        else:
            print(f"{TITULOS[seccion]}\n\n")
    else:
        print(f"{TITULOS[0]}\n\n")


def mostrar_error(msjError: str):
    """Muestra un mensaje de error en la consola y pausa la ejecución.

    Args:
        msjError (str): Mensaje de error que se mostrará al usuario.
    """
    print("\n*ERROR* " + str(msjError))
    pausa(1)


def evaluar_diferencia(numero: int, numero_oculto: int, frio: int, caliente: int) -> int:
    """
    Evalúa la distancia entre el número oculto y el ingresado, y devuelve un código numérico
    basado en la cercanía.

    Args:
        numero (int): Número ingresado por el usuario.
        numero_oculto (int): Número que debe ser adivinado.
        frio (int): Diferencia máxima para considerar la pista como "Frío".
        caliente (int): Diferencia máxima para considerar la pista como "Caliente".

    Returns:
        int: 
            - 0 si el número está "Frío".
            - 1 si el número está "Caliente".
            - 2 si el número está "Te Quemas".
    
    Ejemplos:
        >>> evaluar_diferencia(50, 100, 15, 5)
        0  # Frío
        
        >>> evaluar_diferencia(95, 100, 15, 5)
        1  # Caliente
        
        >>> evaluar_diferencia(98, 100, 15, 5)
        2  # Te Quemas
    """
    diferencia = abs(numero_oculto - numero)
    
    if diferencia > frio:
        return 0  # Frío
    elif diferencia > caliente:
        return 1  # Caliente
    else:
        return 2  # Te Quemas


def obtener_pista(numero: int, numero_oculto: int, intentos: int, frio: int, caliente: int) -> str:
    """
    Obtiene una pista combinando la distancia (frío, caliente, te quemas) y si el número oculto
    es mayor o menor.

    Args:
        numero (int): Número ingresado por el usuario.
        numero_oculto (int): Número que debe ser adivinado.
        intentos (int): Cantidad de intentos restantes.
        frio (int): Diferencia máxima para considerar la pista como "Frío".
        caliente (int): Diferencia máxima para considerar la pista como "Caliente".
    
    Returns:
        str: Frase con la pista para el juego.
    """
    diferencia_code = evaluar_diferencia(numero, numero_oculto, frio, caliente)

    # Determinamos el mensaje según el código de diferencia
    if diferencia_code == 0:
        pista = "* FRÍO, FRÍO,"
    elif diferencia_code == 1:
        pista = "* CALIENTE, CALIENTE,"
    else:
        pista = "* TE QUEMAS,"

    pista += " el número oculto es "

    if numero_oculto > numero:
        pista += "MAYOR... "
    else:
        pista += "MENOR... "

    if intentos > 1:
        pista += f"¡te quedan {intentos} intentos!\n"
    else:
        pista += f"¡te queda {intentos} intento!\n"

    return pista


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
    # Hacer un bucle hasta que se adivine el número o realice todos los intentos posibles...
    # Utiliza pedir_numero_usuario("¿Qué número es? ") pero cuidado con la Excepción que debes controlar AQUÍ.
    # Muestra la pista con obtener_pista() si el número introducido no es el oculto.
    # La función debe retornar si el número fue adivinado y los intentos realizados.
    intentos_realizados = 0
    numero_adivinado = False

    while not numero_adivinado and total_intentos > 0:

        numero = None        
        try:
            numero = pedir_numero_usuario("¿Qué número es? ")
        except ValueError as e:
            mostrar_error(e)

        if numero != None:
            intentos_realizados += 1
            total_intentos -= 1

            if numero != numero_oculto:
                print(f"\n{obtener_pista(numero, numero_oculto, total_intentos, frio, caliente)}")
            else:
                numero_adivinado = True

    return numero_adivinado, intentos_realizados


def pedir_numero_usuario(mensaje: str, minimo: int = None, maximo: int = None) -> int:
    """
    Solicita al usuario que introduzca un número entero válido.

    Args:
        mensaje (str): Mensaje que se muestra al usuario para pedir el número.

    Returns:
        int: Número entero ingresado por el usuario.

    Exceptions:
        ValueError: Si el valor introducido no puede convertirse a un número entero.
    """
    num = int(input(mensaje).strip())

    if minimo != None and num < minimo:
        raise ValueError("")

    if maximo != None and num > maximo:
        raise ValueError("")

    return num


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
            mostrar_error("Debe haber por lo menos 100 números de diferencia entre ellos...")

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
            mostrar_error(f"Deben estar dentro del rango ({minimo}.{maximo}) y no ser iguales...")

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
            mostrar_error("El número de intentos debe ser un entero positivo...")

    return intentos


def configurar_juego() -> tuple:
    """
    Configura todos los parámetros del juego: rango de números, pistas e intentos.

    Returns:
        tuple: Mínimo, máximo, número de intentos, valor para "Frío" y valor para "Caliente".
    """
    limpiar_pantalla()
    mostrar_titulo(4)
    
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
    mostrar_titulo(5)
    print(f"* El número oculto será un número entre {minimo} y {maximo}.")
    print(f"* El número de intentos es {intentos}.")
    print(f"* Pista FRÍO si la diferencia es mayor a {frio}.")
    print(f"* Pista CALIENTE si la diferencia es mayor a {caliente}.")
    print(f"* Pista TE QUEMAS si la diferencia es menor.")
    pausa(tecla_enter = True)


def mostrar_menu():
    """
    Muestra el menú principal del juego.
    """
    limpiar_pantalla()
    mostrar_titulo(2)
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
    opcion_correcta = False

    while not opcion_correcta:
        mostrar_menu()
        try:
            opcion = pedir_numero_usuario("Elije => ")
            
        except ValueError as e:
            mostrar_error("Ha introducido un número entero no válido!")
        else:
            opcion_correcta = comprobar_opcion(opcion)
        
            if not opcion_correcta:
                mostrar_error(f"Opción {opcion} incorrecta! (1-4)")

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
    mostrar_titulo(3, intentos)
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente)

    if numero_adivinado:
        print(f"\n¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print(f"\nGAME OVER - ¡Otra vez será! (#{numero_oculto}#)")
    
    pausa(tecla_enter = True)


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
    mostrar_titulo(1)
    pausa(2)

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

import os
import random
import time


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausa():
    """Realiza una pausa hasta que el usuario presione ENTER."""
    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()


def mostrar_pista(numero: int, numero_oculto: int, intentos: int, frio: int, caliente: int):
    """Muestra la pista basada en la diferencia entre el número y el número oculto."""
    pista = generar_pista(numero, numero_oculto, intentos)
    estado_calor = evaluar_distancia(numero, numero_oculto, frio, caliente)
    print(f"\n{estado_calor} {pista}")


def generar_pista(numero: int, numero_oculto: int, intentos: int) -> str:
    """Genera un mensaje de pista indicando si el número oculto es mayor o menor."""
    if numero_oculto > numero:
        return f"el número oculto es MAYOR... ¡te quedan {intentos} intentos!\n"
    else:
        return f"el número oculto es MENOR... ¡te quedan {intentos} intentos!\n"


def evaluar_distancia(numero: int, numero_oculto: int, frio: int, caliente: int) -> str:
    """Evalúa la distancia entre el número oculto y el ingresado y devuelve el estado."""
    diferencia = abs(numero_oculto - numero)
    
    if diferencia > frio:
        return "* FRÍO, FRÍO,"
    elif diferencia > caliente:
        return "* CALIENTE, CALIENTE,"
    else:
        return "* TE QUEMAS,"


def adivina_el_numero(numero_oculto: int, total_intentos: int, frio: int, caliente: int):
    """Gestiona el proceso de adivinación del número oculto."""
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
    """Comprueba si el valor dado es un número entero."""
    if valor.startswith("-"):
        valor = valor[1:]
    return valor.isdigit()


def pedir_numero_usuario(mensaje: str) -> int:
    """Pide al usuario que introduzca un número entero, validándolo."""
    valor = input(mensaje).strip()
    
    while not comprobar_numero_entero(valor):
        print("\n*ERROR* Ha introducido un número entero no válido!")
        valor = input(mensaje).strip()

    return int(valor)


def genera_numero_oculto(minimo: int, maximo: int) -> int:
    """Genera un número oculto aleatorio dentro de un rango."""
    return random.randint(minimo, maximo)


def configurar_rangos_numeros() -> tuple:
    """Configura el rango de números válidos para el juego."""
    minimo = pedir_numero_usuario("Introduce el mínimo número posible: ")
    maximo = pedir_numero_usuario("Introduce el máximo número posible: ")

    while not (minimo < maximo and (maximo - minimo) >= 100):
        print("\n*ERROR* Debe haber por lo menos 100 números de diferencia entre ellos...")
        minimo = pedir_numero_usuario("Introduce el mínimo número posible: ")
        maximo = pedir_numero_usuario("Introduce el máximo número posible: ")

    return minimo, maximo


def configurar_pistas(minimo: int, maximo: int) -> tuple:
    """Configura los valores de frío y caliente para las pistas."""
    frio = pedir_numero_usuario("Introduce la diferencia para mostrar la pista FRÍO, FRÍO: ")
    caliente = pedir_numero_usuario("Introduce la diferencia para mostrar la pista CALIENTE, CALIENTE: ")

    while not (frio > caliente and minimo <= frio <= maximo and minimo <= caliente <= maximo):
        print(f"\n*ERROR* Deben estar dentro del rango ({minimo}.{maximo}) y no ser iguales...")
        frio = pedir_numero_usuario("Introduce la diferencia para mostrar la pista FRÍO, FRÍO: ")
        caliente = pedir_numero_usuario("Introduce la diferencia para mostrar la pista CALIENTE, CALIENTE: ")

    return frio, caliente


def configurar_intentos() -> int:
    """Configura el número de intentos para adivinar el número oculto."""
    return pedir_numero_usuario("Introduce el número de intentos: ")


def configurar_juego() -> tuple:
    """Configura todos los parámetros del juego: rango, pistas e intentos."""
    limpiar_pantalla()
    print("--- CONFIGURA EL JUEGO DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    
    minimo, maximo = configurar_rangos_numeros()
    frio, caliente = configurar_pistas(minimo, maximo)
    intentos = configurar_intentos()

    return minimo, maximo, intentos, frio, caliente


def mostrar_configuracion(minimo, maximo, intentos, frio, caliente):
    """Muestra la configuración actual del juego."""
    limpiar_pantalla()
    print(f"--- CONFIGURACIÓN ACTUAL DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print(f"* El número oculto será un número entre {minimo} y {maximo}.")
    print(f"* El número de intentos es {intentos}.")
    print(f"* Pista FRÍO si la diferencia es mayor a {frio}.")
    print(f"* Pista CALIENTE si la diferencia es mayor a {caliente}.")
    print(f"* Pista TE QUEMAS si la diferencia es menor.")
    pausa()


def mostrar_menu():
    """Muestra el menú principal."""
    limpiar_pantalla()
    print(f"--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print("1. Jugar.")
    print("2. Configurar.")
    print("3. Mostrar configuración.")
    print("4. Salir.\n")


def elegir_opcion_menu() -> int:
    """Permite al usuario elegir una opción del menú."""
    mostrar_menu()
    opcion = pedir_numero_usuario("Elije => ")

    while not comprobar_opcion(opcion):
        print(f"\n*ERROR* Opción {opcion} incorrecta! (1-4)")
        opcion = pedir_numero_usuario("Elije => ")

    return opcion


def comprobar_opcion(opcion: int) -> bool:
    """Comprueba si la opción elegida está en el rango permitido."""
    return 1 <= opcion <= 4


def jugar(numero_oculto, intentos, frio, caliente):
    """Gestiona el proceso de juego y muestra los resultados."""
    limpiar_pantalla()
    print(f"--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n")
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente)

    if numero_adivinado:
        print(f"\n¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print(f"\nGAME OVER - ¡Otra vez será! (#{numero_oculto}#)")
    
    pausa()


def main():
    """Función principal del juego."""
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

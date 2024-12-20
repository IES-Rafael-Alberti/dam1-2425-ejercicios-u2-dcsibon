import random
import os
import time
# Para mostrar cualquier ERROR debes usar la función mostrar_error(), no hagas print directamente.


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

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear' (os.name == "posix").
    """
    try:
		# Debe funcionar en todos los sistemas operativos
        os.system("cls")
        os.system("clear")
    except Exception as e:
        mostrar_error(f"Problemas al intentar limpiar la pantalla: {e}")


def pausa(tiempo, tecla_enter = False, limpiar = True):
    """
    Pausa la ejecución del programa según los parámetros especificados.

    Args:
        tiempo (int, opcional): Número de segundos para la pausa. Si es mayor a 0, se pausa 
            por este tiempo y se ignora `tecla_enter`.
        tecla_enter (bool, opcional): Si es True y `tiempo` es 0, espera a que el usuario presione 
            ENTER para continuar.
        limpiar (bool, opcional): Si es True, limpia la pantalla después de la pausa.

    """
    if tiempo != 0 :
        time.sleep(tiempo)
        if limpiar == True:
            limpiar_pantalla()
    if tiempo == 0:
        tecla_enter = True
        print("\nPresione ENTER para continuar...")
        if limpiar == True:
            limpiar_pantalla()
    # Desarrolla esta función y ejecute una pausa de un tiempo en segundos con time.sleep()
    # o una pausa esperando a que el usuario "\nPresione ENTER para continuar..."
    # Además, dependiendo del parámetro opcional limpiar debe limpiar la consola o no


def mostrar_titulo(seccion: int, intentos: int = 0):
    """
    Muestra el título correspondiente a la sección del juego.

    Args:
        seccion (int): El identificador de la sección. Los valores válidos son de 1 a len(TITULOS).
        intentos (int): Número de intentos que puede ser usado en el título si corresponde.
    """

    try:
        0 < seccion < len(TITULOS)
        if intentos > 0:
            print(TITULOS[seccion].format(intentos = intentos) + "\n\n")
        else:
            print(f"{TITULOS[seccion]}\n\n")
    except:
        print(f"{TITULOS[0]}\n\n")
	#
	# Hacer lo mismo que el código comentado, pero útilizando try-except 
	# para controlar si la seccion está fuera de rango


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
	# Realizar la función según la documentación que observáis


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

    Note:
        La función retorna uno de los siguientes mensajes según la proximidad del número ingresado al número oculto:

        - "* FRÍO, FRÍO, el número oculto es MENOR... ¡te quedan N intentos!\n"
        - "* FRÍO, FRÍO, el número oculto es MAYOR... ¡te quedan N intentos!\n"
        - "* CALIENTE, CALIENTE, el número oculto es MENOR... ¡te quedan N intentos!\n"
        - "* CALIENTE, CALIENTE, el número oculto es MAYOR... ¡te quedan N intentos!\n"
        - "* TE QUEMAS, el número oculto es MENOR... ¡te quedan N intentos!\n"
        - "* TE QUEMAS, el número oculto es MAYOR... ¡te quedan N intentos!\n"       

        En los mensajes, "N" representa el número de intentos restantes.   
    """
	# Realizar la función según la documentación que observáis
	# Daros cuenta que debéis hacer una llamada a la función evaluar_diferencia()
    if numero < numero_oculto and numero_oculto >= frio:
        return f"* FRÍO, FRÍO, el número oculto es MENOR... ¡te quedan {intentos - 1} intentos!\n"
    elif numero > numero_oculto and numero_oculto <= frio:
        return f"* FRÍO, FRÍO, el número oculto es MAYOR... ¡te quedan {intentos - 1} intentos!\n"
    elif numero < numero_oculto and numero_oculto <= caliente:
        return f"* CALIENTE, CALIENTE, el número oculto es MENOR... ¡te quedan {intentos - 1} intentos!\n"
    elif numero > numero_oculto and numero_oculto > caliente:
        return f"* CALIENTE, CALIENTE, el número oculto es MAYOR... ¡te quedan {intentos - 1} intentos!\n"
    elif numero < numero_oculto:
        return f"* TE QUEMAS, el número oculto es MENOR... ¡te quedan {intentos - 1} intentos!\n"
    elif numero > numero_oculto:
        return f"* TE QUEMAS, el número oculto es MAYOR... ¡te quedan {intentos - 1} intentos!\n"


def pedir_numero_usuario(mensaje: str, minimo: int = None, maximo: int = None) -> int:
    """
    Solicita al usuario que introduzca un número entero válido.

    Args:
        mensaje (str): Mensaje que se muestra al usuario para pedir el número.

    Returns:
        int: Número entero ingresado por el usuario.

    Raises:
        ValueError: Si el valor introducido no puede convertirse a un número entero.
    """
    # El código de esta función NO SE PUEDE TOCAR! Ya está terminada
    try:
        num = int(input(mensaje).strip())
    except ValueError:
        raise ValueError("El número introducido no es un entero válido!")

    if minimo != None and num < minimo:
        raise ValueError(f"El número introducido no es correcto (mínimo: {minimo})")

    if maximo != None and num > maximo:
        raise ValueError(f"El número introducido no es correcto (máximo: {maximo})")

    return num


def adivina_el_numero(numero_oculto: int, total_intentos: int, minimo: int, maximo: int, frio: int, caliente: int, intentos:int):
    """
    Gestiona el proceso de adivinación del número oculto, permitiendo que el usuario ingrese números.

    Args:
        numero_oculto (int): Número que debe ser adivinado.
        total_intentos (int): Cantidad total de intentos permitidos.
        minimo (int): Número mínimo que puede alcanzar el número oculto.
        maximo (int): Número máximo que puede alcanzar el número oculto.
        frio (int): Diferencia máxima para considerar la pista como "Frío".
        caliente (int): Diferencia máxima para considerar la pista como "Caliente".

    Returns:
        tuple: Un booleano que indica si el número fue adivinado y el número de intentos realizados.
    """
    while intentos != 0:
        numero = print(f"¿Qué número es? {pedir_numero_usuario()}")
        if numero != numero_oculto:
            print(obtener_pista(numero, numero_oculto, intentos, frio, caliente))
        else:
            numero_adivinado = numero
            intentos_realizados = intentos
        intentos -= 1
    return numero_adivinado, intentos_realizados
# Hacer un bucle hasta que se adivine el número o realice todos los intentos posibles...
    # Utiliza pedir_numero_usuario("¿Qué número es? ", minimo, maximo)
    # Muestra la pista con obtener_pista() si el número introducido no es el oculto (obtener_pista()).
    # La función debe retornar si el número fue adivinado y los intentos realizados.


def configurar_rangos_numeros() -> tuple:
    minimo = None
    maximo = None
    while minimo or maximo == None:
        minimo = print(f"Introduce un número minimo {pedir_numero_usuario()}")
        maximo = print(f"Introduce un número minimo {pedir_numero_usuario()}")
        if minimo > maximo:
            minimo = None
            maximo = None
            mostrar_error("*ERROR* El valor mínimo no puede ser superior al máximo.")
        elif (maximo - minimo) <100:
            minimo = None
            maximo = None
            mostrar_error("*ERROR* El rango del número oculto debe ser igual o superior a 100.")
    
    """
    Configura el rango de números válidos para el juego solicitando los valores mínimo y máximo.

    Returns:
        tuple: Una tupla que contiene el número mínimo y el número máximo configurados para el juego.

    Raises:
        ValueError: Si el valor mínimo es superior al máximo o si la diferencia entre el máximo y 
                    el mínimo es menor a 100.
    """
    # Debe usar pedir_numero_usuario() para solicitar el número mínimo y máximo del 
    # rango posible para el número oculto.
    # Requisitos que debe cumplir para aceptar el mínimo y máximo:
    # 1. El número mínimo debe ser menor que el máximo.
    #    (*ERROR* El valor mínimo no puede ser superior al máximo.)
    # 2. La diferencia entre ambos debe ser igual o superior a 100. 
    #    (*ERROR* El rango del número oculto debe ser igual o superior a 100.)

    return minimo, maximo


def configurar_pistas(minimo: int, maximo: int) -> tuple:
    frio = None
    caliente = None
    while frio or caliente == None:
        frio = print(f"El valor frio aparecera a partir del número: {pedir_numero_usuario()}")
        caliente = print(f"El valor caliente aparecera a partir del número: {pedir_numero_usuario()}")
        if frio <= caliente:
            frio = None
            caliente = None
            mostrar_error("*ERROR* La diferencia para la pista FRÍO no puede ser inferior o igual a la CALIENTE!")
        elif caliente == 0:
            frio = None
            caliente = None
            mostrar_error("*ERROR* La diferencia para la pista CALIENTE debe ser superior a 0!")
        elif frio > maximo or frio < minimo:
            frio = None
            caliente = None
            mostrar_error(f"*ERROR* La diferencia para la pista FRÍO debe estar entre {minimo} y {maximo}!")
        elif caliente > maximo or caliente < minimo:
            frio = None
            caliente = None
            mostrar_error(f"*ERROR* La diferencia para la pista CALIENTE debe estar entre {minimo} y {maximo}!")
        
    """
    Configura los valores de diferencia para las pistas "Frío" y "Caliente".

    Args:
        minimo (int): El número mínimo dentro del rango de juego.
        maximo (int): El número máximo dentro del rango de juego.

    Returns:
        tuple: Una tupla que contiene los valores para las pistas de "Frío" y "Caliente".

    Raises:
        ValueError: Si la diferencia para la pista "Frío" no es mayor que la de "Caliente",
                    si "Caliente" es menor o igual a 0, o si alguno de los valores se sale 
                    del rango (minimo, maximo).
    """
    # Debe usar pedir_numero_usuario() para solicitar los valores de diferencia 
    # para las pistas "Frío" y "Caliente".
    # Requisitos que debe cumplir para aceptar estos valores:
    # 1. La diferencia para la pista FRÍO no puede ser inferior o igual a la CALIENTE.
    #    (*ERROR* La diferencia para la pista FRÍO no puede ser inferior o igual a la CALIENTE!)
    # 2. La diferencia para la pista CALIENTE debe ser superior a 0. 
    #    (*ERROR* La diferencia para la pista CALIENTE debe ser superior a 0!)
    # 3. La diferencia para la pista FRÍO debe estar entre minimo y maximo.
    #    (*ERROR* La diferencia para la pista FRÍO debe estar entre {minimo} y {maximo}!)
    # 4. La diferencia para la pista CALIENTE debe estar entre minimo y maximo.
    #    (*ERROR* La diferencia para la pista CALIENTE debe estar entre {minimo} y {maximo}!)

    return frio, caliente


def configurar_intentos(minimo, maximo) -> int:
    intentos = None
    rango_numero_oculto = range(minimo, maximo)
    while not intentos:
        try:
            intentos = int(print(f"Introduce un número de intentos: {pedir_numero_usuario()}"))
        except ValueError:
            if intentos < 0:
                intentos = None
                raise ValueError(mostrar_error("*ERROR* El número de intentos debe ser un número entero positivo!"))
            if intentos > (rango_numero_oculto/10):
                intentos = None
                raise ValueError(mostrar_error("*ERROR* El número de intentos no puede ser superior al 10% del rango del número oculto!"))
            else:
                mostrar_error("ERROR, intentalo de nuevo")

    """
    Configura el número de intentos para adivinar el número oculto, asegurando que el valor es positivo 
    y no excede el 10% del rango de números.

    Args:
        rango_numero_oculto (int): El rango del número oculto (diferencia entre el máximo y el mínimo).

    Returns:
        int: El número de intentos configurado por el usuario.

    Raises:
        ValueError: Si el número de intentos es menor o igual a 0 o si excede el 10% del rango.
    """
    # Debe usar pedir_numero_usuario() para solicitar los intentos posibles.
    # Requisitos que debe cumplir para aceptar el valor:
    # 1. Número entero positivo mayor que cero.
    #    (*ERROR* El número de intentos debe ser un número entero positivo!)
    # 2. Inferior al 10% del rango del número oculto.
    #    (*ERROR* El número de intentos no puede ser superior al 10% del rango del número oculto!)

    return intentos


def configurar_juego() -> tuple:
    """
    Configura todos los parámetros del juego: rango de números, pistas e intentos.

    Returns:
        tuple: Mínimo, máximo, número de intentos, valor para "Frío" y valor para "Caliente".
    """
	# Completar la llamada a las funciones correctas...
    limpiar_pantalla()
    mostrar_titulo(4)
    
    minimo, maximo = configurar_rangos_numeros()
    frio, caliente = configurar_pistas(maximo, minimo)
    intentos = configurar_intentos(minimo, maximo)

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
	# Corregir posibles errores...
    limpiar_pantalla
    mostrar_titulo()
    print(f"* El número oculto será un número entre {minimo} y {maximo}.")
    print(f"* El número de intentos es {intentos}.")
    print(f"* Pista FRÍO si la diferencia es mayor a {frio}.")
    print(f"* Pista CALIENTE si la diferencia es mayor a {caliente}.")
    print("* Pista TE QUEMAS si la diferencia es menor.")
    pausa


def mostrar_menu():
    """
    Muestra el menú principal del juego.
    """
	# Corregir posibles errores...
    mostrar_titulo()
    print("1. Jugar.")
    print("2. Configurar.")
    print("3. Mostrar configuración.")
    print("4. Salir.\n")


def comprobar_opcion(opcion: int) -> bool:
	# Comprobación de opción
    if 1 <= opcion <= 4:
        return True
    else:
        return False


def elegir_opcion_menu() -> int:
    """
    Permite al usuario elegir una opción del menú.

    Returns:
        int: La opción elegida por el usuario.
    """
	# Corregir posibles errores...
    opcion_correcta = False

    while not opcion_correcta:
        mostrar_menu()

        opcion = pedir_numero_usuario("Elije => ")
            
        opcion_correcta = comprobar_opcion(opcion)
	
        if not opcion_correcta:
            mostrar_error(f"Opción {opcion} incorrecta! (1-4)")
    return opcion



def jugar(numero_oculto: int, intentos: int, frio: int, caliente: int):
    numero_oculto = random.randint(0,100)
    """
    Gestiona el proceso del juego de adivinar el número oculto y muestra los resultados al finalizar.
    Args:
        numero_oculto (int): Número que debe ser adivinado por el jugador.
        minimo (int): El límite inferior del rango de números posibles.
        maximo (int): El límite superior del rango de números posibles.
        intentos (int): Número máximo de intentos permitidos para el jugador.
        frio (int): Diferencia mínima para que se active la pista "Frío".
        caliente (int): Diferencia mínima para que se active la pista "Caliente".

    Note:
        - Un mensaje de éxito si el jugador adivina el número, indicando los intentos utilizados.
        - Un mensaje de fin de juego si el jugador no logra adivinar el número, mostrando el número oculto.
    """
	# Mostrar el mensaje correspondiente al final del juego:
	# - Si lo adivinó => "\n¡Bravo! ¡Lo conseguiste en N intentos!"
	# - Si no lo consiguió => "\nGAME OVER - ¡Otra vez será! (#XX#)"
	# Donde N es el númnero de intentos en el que consiguió acertarlo y XX el número oculto.
	# Recuerda que debes mostrar dichos mensajes hasta que el usuario presione ENTER...
	# También debes corregir posibles errores...
    limpiar_pantalla()
    mostrar_titulo(3, intentos)
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente, intentos)
   
    pausa


def genera_numero_oculto():
	# Creación de número oculto
    return random.randint(1, 100)
    

def main():
    """
    Función principal que ejecuta el flujo completo del juego de adivinar el número oculto.
    
    Configura los parámetros iniciales, muestra la configuración actual, y gestiona el bucle principal del menú 
    para permitir al usuario jugar, configurar el juego, mostrar la configuración actual del juego o salir.

    Note:
        1. Limpia la pantalla, muestra el título de bienvenida y hace una pausa inicial.
        2. Configura los parámetros iniciales del juego:
            - minimo: Límite inferior del rango de números (por defecto 0).
            - maximo: Límite superior del rango de números (por defecto 100).
            - frio: Diferencia mínima para la pista "Frío" (por defecto 15).
            - caliente: Diferencia mínima para la pista "Caliente" (por defecto 5).
            - intentos: Número máximo de intentos (por defecto 5).
        3. Muestra la configuración actual del juego y pide presionar una tecla para continuar...
        4. Permite al usuario interactuar mediante un menú:
            - Opción 1: Jugar e intentar adivinar el número oculto.
            - Opción 2: Configurar los parámetros del juego.
            - Opción 3: Visualizar la configuración actual del juego.
            - Opción 4: Salir del juego.
        5. Finaliza el juego mostrando un mensaje de despedida.
    """
    # Debe limpiar la pantalla, mostrar el título de la sección correspondiente y hacer una pausa de 2 segundos
    # Corrige los posibles errores...
    limpiar_pantalla()
    mostrar_titulo()
    pausa(1)

    minimo = 0
    maximo = 100
    frio = 15
    caliente = 5
    intentos = 5

    mostrar_configuracion(minimo, maximo, intentos, frio, caliente)
    pausa(0)

    salir = False

    while salir == False:
        opcion = elegir_opcion_menu()

        if opcion == 1:
            numero_oculto = genera_numero_oculto()
            jugar(numero_oculto, intentos, frio, caliente)
        elif opcion == 2:
            minimo, maximo, intentos, frio, caliente = configurar_juego()
        elif opcion == 3:
            mostrar_configuracion(minimo, maximo, intentos, frio, caliente)
        elif opcion == 4:
            salir = True

    limpiar_pantalla()
    print("Bye, bye...\n\n")


if __name__ == "__main__":
    main()

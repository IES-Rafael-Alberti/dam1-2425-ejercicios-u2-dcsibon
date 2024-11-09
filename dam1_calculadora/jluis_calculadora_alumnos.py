# TODO: ATENCIÓN!!!
# 1. Importar los paquetes necesarios
# 2. Usar la función mostrar_error para imprimir los errores por consola.
# 3. Los comentarios TODO os ayudan a resolver cada apartado de esta prueba.
# 4. CADA función SOLO puede tener una instrucción return.
# 5. En test_calculadora_alumnos.py crear el test unitario para la función es_resultado_negativo y hacer que todos los test unitarios se cumplan.

import os
import platform

# Mensajes de error predefinidos
MENSAJES_ERROR = (
    "Problemas al intentar limpiar la pantalla {error}",
    "Error al configurar los decimales. Formato: decimales <n>.",
    "Entrada no válida. Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo.",
    "Error: Introduzca un operador antes de otro número.",
    "Comando no reconocido. Escriba 'lista' para ver las operaciones disponibles.",
    "Error: no es posible la división por 0! Introduzca otro valor diferente a 0...",
    "Se produjo un error: {error}"
)

# Operadores soportados por la calculadora
OPERADORES = ('+', '-', 'x', '*', '/', ':', '**', 'exp')
# TODO: Ayuda: incluye en esta constante los símbolos que reconocerá la aplicación para el cálculo de las operaciones:
# '+' para la suma.
# '-' para la resta.
# 'x' o '*' para la multiplicación.
# '/' o ':' para la división.
# '**' o 'exp' para la potencia.

COMANDOS = ('', 'ce', 'lista', 'calculo', 'decimales')


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    """
    # TODO: El desarrollo de esta función está incompleto y con errores.
    try:
        sistema_operativo = platform.system()

        if sistema_operativo == "Linux" or sistema_operativo == "Darwin":
            os.system('clear')
        else:
            os.system('cls')

    except Exception as e:
        mostrar_error(0, e)



def pausa():
    """
    Pausa la ejecución del programa hasta que se pulse ENTER... "\nPresione ENTER para continuar..."
    """
    # TODO: Desarrollar esta función según su documentación. 
    enter = input('\nPresione ENTER para continuar...')


def mostrar_error(indice_error: int, msj_error = None):
    """
    Muestra un mensaje de error en la consola.
    
    Args:
        indice_error (int): Índice del mensaje de error en MENSAJES_ERROR.
        msj_error (str, opcional): Texto adicional para personalizar el mensaje de error.
    """
    # TODO: 
    # 1. Corrige el error que existe a la hora de acceder a los mensajes de error que están en la constante
    #    MENSAJES_ERROR. A los elementos de una tupla se accede igual que a los caracteres de una 
    #    cadena de caracteres.
    # 2. Completa el código de esta función para que controle específicamente las excepciones IndexError y 
    #    muestre el mensaje: "\n*ERROR* Mensaje de error no definido.\n"
    # 3. También se pide que se controle cualquier otra excepción que se pueda producir y muestre el mensaje:
    #    "\n*ERROR* Problemas al mostrar error!\n{e}\n"
    # 4. En esta función los mensajes de error deben mostrarse con print.
    try:
        if msj_error != None:
            print(f"\n*ERROR* {MENSAJES_ERROR.format(error = msj_error)}\n")
        else:
            print(f"\n*ERROR* {MENSAJES_ERROR[indice_error]}\n")
    except IndexError:
        print("\n*ERROR* Mensaje de error no definido.\n")
    except Exception as e:
        print(f"\n*ERROR* Problemas al mostrar error!\n{e}\n")


def sumar(num1: float, num2: float) -> float:
    '''
    Esta funcion suma los numeros introducidos
    
    Args:
        num1 (float): Primer numero
        num2 (float): Segundo numero

    Returns:
        float: Resultado de la resta
    '''
    return num1 + num2


def restar(num1: float, num2: float) -> float:
    '''
    Esta funcion resta los numeros introducidos
    
    Args:
        num1 (float): Primer numero
        num2 (float): Segundo numero

    Returns:
        float: Resultado de la resta
    '''
    return num1 - num2


def es_resultado_negativo(num1: float, num2: float) -> bool:
    """Determina si el resultado de una operación entre num1 y num2 debe ser negativo."""
    # TODO: Realizar el desarrollo completo de esta función teniendo en cuenta la documentación y completándola también. 
    # Debe pasar las pruebas unitarias.
    # Se trata de una función que os puede venir bien para utilizarla tanto en la función multiplicar, como en dividir.
    # Ya que va a determinar si la multiplicación o división entre dos números debería ser de signo negativo o no.
    if num1 < 0 and num2 < 0:
        negativo = False
    elif num1 < 0 or num2 < 0:
        negativo = True
    else:
        negativo = False

    return negativo

def multiplicar(num1: float, num2: float) -> int:
    """
    Realiza la multiplicación ENTERA de dos números usando solo sumas y restas.
    
    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.
    
    Returns:
        int: Resultado de la multiplicación.

    Note:
        Debe redondear los números recibidos a enteros para trabajar.
    """
    # TODO: 
    # 1. Realizar el desarrollo completo de esta función teniendo en cuenta la documentación. 
    # 2. Esta función debe pasar las pruebas unitarias.
    # 3. No podéis usar el operador de multiplicación de Python para realizar el desarrollo de la misma, 
    #    es decir, que debéis realizar la multiplicación con SUMAS y/o RESTAS...
    # 4. Aunque se reciben números de tipo float, debéis redondearlos como números enteros para 
    #    simplificar esta función, es decir, la operación 4.98 * 3.33, deberá convertirse en 5 * 3.
    # 5. Tened en cuenta que podéis recibir números negativos, es decir, la operación -5 * -5 = 25
    # 6. OBLIGATORIO usar un bucle for.
    # 7. Incluir algún comentario para mejorar la claridad y permitir que otros comprendan el propósito y funcionamiento del código.
    negativo = es_resultado_negativo(num1, num2)
    resultado = 0
    
    # Ponemos los numeros en valor absoluto para operar con ellos
    num1 = round(abs(num1))
    num2 = round(abs(num2))
    
    # A Diego le apetece que lo hagamos con un for, asi que para contentar a Diego hacemos un bucle for
    # que sume uno de los numeros, en este caso el num1, tantas veces como el num2. Debido a la propiedad
    # conmutativa de la multiplicacion, da igual cual sumemos.
    for i in range (num2):
        resultado += num1

    # Invertimos el resultado
    resultado_negativo = resultado - resultado - resultado
    
    return resultado_negativo if negativo else resultado



def dividir(num1: float, num2: float):
    """
    Realiza la división ENTERA de dos números usando solo sumas y restas.
    
    Args:
        num1 (float): Dividendo.
        num2 (float): Divisor.
    
    Returns:
        int: Resultado de la división.
    
    Raises:
        ZeroDivisionError: Si el divisor es cero.

    Note:
        Debe redondear los números recibidos a enteros para trabajar.        
    """
    # TODO: 
    # 1. Realizar el desarrollo completo de esta función teniendo en cuenta la documentación. 
    # 2. Esta función debe pasar las pruebas unitarias.
    # 3. No podéis usar el operador de división de Python para realizar el desarrollo de la misma, 
    #    es decir, que debéis realizar la división con SUMAS y/o RESTAS...
    # 4. Aunque se reciben números de tipo float, debéis redondearlos como números enteros para 
    #    simplificar esta función, es decir, la operación 4.98 / 3.33, deberá convertirse en 5 / 3.
    # 5. Tened en cuenta que podéis recibir números negativos, es decir, la operación -5 / -5 = 1
    # 6. Incluir algún comentario para mejorar la claridad y permitir que otros comprendan el propósito y funcionamiento del código.
    resultado = num1
    contador = 0
    negativo = es_resultado_negativo(num1, num2)
    
    # Ponemos los numeros en valor absoluto para operar con ellos
    num1 = round(abs(num1))
    num2 = round(abs(num2))

    # A Diego le apetece que lo hagamos con un while, asi que para contentar a Diego hacemos un bucle while
    # que cuente el numero de veces que le podemos restar el dividendo al divisor.
    while resultado > 0:
        resultado -= num2
        contador += 1

    # Invertimos el resultado
    contador_negativo = contador - contador - contador

    return contador_negativo if negativo else contador


def potencia(num1: float, num2: float) -> int:
    '''
    Esta funcion calcula la potencia de un numero

    Args:
        num1 (float): Numero a elevar
        num2 (float): Exponente

    Returns:
        int: Resultado
    '''
    # TODO: 
    # 1. Realizar el desarrollo completo de esta función y su documentación. 
    # 2. Esta función debe pasar las pruebas unitarias.
    # 3. PREMISAS a tener en cuenta:
    #    - Cualquier número elevado a 0 da como resultado 1.
    #    - Para simplificar esta función, vamos a suponer que un número elevado a un 
    #      exponente negativo siempre dará 0 (aunque en realidad no es así matemáticamente)
    # 4. Utiliza la función de multiplicar para realizar los cálculos que te 
    #    harán falta en esta función (RECUERDA que no puedes usar directamente los operadores 
    #    de Python para la multiplicación y división).
    # 5. Incluir algún comentario para mejorar la claridad y permitir que otros comprendan el propósito y funcionamiento del código.
    negativo = es_resultado_negativo(num1, num2)
    num1 = round(abs(num1))
    num2 = round(abs(num2))
    resultado = 1

    if num2 != 0:
        for i in range (num2):
            resultado = multiplicar(resultado, num1)
    elif num2 < 0:
        resultado = 0
    else: 
        resultado = 1

    resultado_negativo = resultado - resultado - resultado

    modulo = num2 % 2

    return resultado_negativo if negativo and modulo != 0 else resultado

def pedir_entrada(msj: str) -> str:
    """
    Pide al usuario una entrada, elimina espacios por delante y por detrás y la convierte a minúsculas.
    
    Args:
        msj (str): Mensaje para solicitar la entrada.
    
    Returns:
        str: Entrada del usuario.
    """
    # TODO: El desarrollo de esta función está incompleto, debéis terminarla teniendo en cuenta la documentación
    return input(msj).lower().strip()


def calcular_operacion(num1: float, num2: float, operador: str) -> float:
    """
    Realiza la operación especificada entre num1 y num2 dependiendo del valor del operador.
    
    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.
        operador (str): Operador de la operación.
    
    Returns:
        float: Resultado de la operación.

    Raises:
        ZeroDivisionError: Si el divisor es cero.
    """        
    # TODO: El desarrollo de esta función está incompleto... completadla teniendo en cuenta la documentación
    # y que debe realizar las llamadas adecuadas a las funciones ya creadas para realizar los distintos 
    # cálculos... sumar, restar, multiplicar, dividir y potencia.
    # IMPORTANTE: Si hacemos caso a la documentación de esta función, NO debéis capturar la excepción 
    # ZeroDivisionError aquí, sino que hay que dejadla que se propague a la función llamante, realizar_calculo(), 
    # dónde se os indica cómo realizar la gestión de estos errores.
    if operador == OPERADORES[0]:
        resultado = sumar(num1, num2)
    elif operador == OPERADORES[1]:
        resultado = restar(num1, num2)
    elif operador == OPERADORES[2] or operador == OPERADORES[3]:
        resultado = multiplicar(num1, num2)
    elif operador == OPERADORES[4] or operador == OPERADORES[5]:
        resultado = dividir(num1, num2)
    elif operador == OPERADORES[6] or operador == OPERADORES[7]:
        resultado = potencia(num1, num2)

    return resultado



def obtener_operaciones() -> str:
    """
    Devuelve una cadena con la lista de operaciones disponibles en la calculadora.

    Returns:
        (str): cadena de caracteres con la información de las operaciones disponibles.
    """
    # TODO: El desarrollo de esta función está incompleto... ver documentación para solucionarla correctamente.
    return 'Operaciones disponibles:\nce => Reiniciar resultado a 0\ndecimales <n> => Establecer decimales en resultado\ncadena vacía + <ENTER> => Pregunta si desea salir\ncalculo => Iniciar cálculo secuencial\n    + => Suma\n    - => Resta\n    x o * => Multiplicación\n    / o : => División\n    ** o exp => Potencia\n    cancelar => volver sin actualizar resultado de la calculadora\n    cadena vacía + <ENTER> => volver actualizando resultado de la calculadora'


def realizar_calculo(decimales: int, resultado_almacenado: float) -> float:
    """
    Realiza una secuencia de cálculos solicitando números y operadores al usuario.
    
    Args:
        decimales (int): Número de decimales para el resultado.
        resultado_almacenado (float): Valor almacenado en la calculadora.
    
    Returns:
        float: Resultado final del cálculo o None si se cancela.

    Note:
        * Dentro de esta función el usuario puede realizar cálculos secuenciales, es decir, 
          comenzará introduciendo un número, después un operador, y otro número... a partir 
          de aquí sobre el resultado acumulado, introducirá operador y número para seguir 
          realizando cálculos (ver ejemplos en README.md de la tarea en el repositorio de GitHub).
        * El usuario es guiado para introducir números y operadores secuencialmente 
          para realizar operaciones básicas.
        * El usuario puede utilizar "resultado" en la secuencia de cálculo para reutilizar el 
          resultado almacenado en la calculadora.
        * El cálculo finaliza al pulsar <ENTER>, volviendo y actualizando el resultado almacenado 
          de la calculadora con el cálculo realizado.
        * También podemos escribir "cancelar", volviendo sin realizar ningún cambio en el 
          resultado almacenado de la calculadora.    
    """
    # TODO: El desarrollo de esta función está incompleto... ver documentación para solucionarla correctamente.

    operador = None
    resultado = None
    realizando_calculos = True

    print("\n## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##\n")

    while realizando_calculos:
        if resultado == None:
            entrada = pedir_entrada(f"\t (Cálculo = 0.0) >> ")
        else:
            entrada = pedir_entrada(f"\t (Cálculo = {round(float(resultado), decimales)}) >> ")
        
        if entrada == "cancelar":
            resultado = None

        elif entrada == "":
            return resultado

        elif entrada in OPERADORES:
            operador = entrada

        else:
            # TODO: este código funciona cuando solucionéis que reconozca las variables resultado_almacenado y decimales.
            # Pero no gestiona los posibles tipos de Excepciones que se pueden producir: 
            #    - ValueError que debe mostrar el error que está en la posición 2 de MENSAJES_ERROR.
            #    - ZeroDivisionError que debe mostrar el error que está en la posición 5 de MENSAJES_ERROR.
            #    - Exception que debe mostrar el error que está en la posición 6 de MENSAJES_ERROR.
            if entrada == "resultado":
                resultado_almacenado = resultado
                resultado = None
                entrada = resultado_almacenado

            try:
                numero = float(entrada)

                if operador is not None:
                    if resultado is None:
                        resultado = 0
                    resultado = round(calcular_operacion(resultado, numero, operador), decimales)
                    operador = None

                elif resultado is None:
                    resultado = numero

                else:
                    mostrar_error(3)

            except ValueError:
                mostrar_error(2)
            except ZeroDivisionError:
                mostrar_error(5)
            except Exception:
                mostrar_error(6)


def main():
    """
    Función principal de la calculadora. Gestiona la entrada del usuario y coordina las operaciones.
    
    Note:
        El flujo del programa es el siguiente:

        1. Inicia la calculadora mostrando el resultado almacenado por defecto (0.00).
        
        2. El usuario ingresa un comando, que puede ser:
            - "lista" para ver todas las operaciones disponibles.
            - "ce" para reiniciar el resultado almacenado a 0.
            - "decimales <n>" para establecer el número de decimales mostrados en el resultado.
            - "calculo" para iniciar una secuencia de cálculo paso a paso.
            - Una entrada vacía y pulsa la tecla <ENTER> para salir de la calculadora.
        
        3. Según el comando ingresado:
            - El programa realiza la operación o ejecuta la acción indicada.
            - Al ingresar "calculo":
                * El usuario es guiado para introducir números y operadores secuencialmente para realizar operaciones básicas.
                * El usuario puede utilizar "resultado" en la secuencia de cálculo para reutilizar el resultado almacenado en la calculadora.
                * El cálculo finaliza al pulsar <ENTER>, volviendo y actualizando el resultado almacenado de la calculadora con el cálculo realizado.
                * También podemos escribir "cancelar", volviendo sin realizar ningún cambio en el resultado almacenado de la calculadora.
        
        4. La calculadora sigue ejecutándose hasta que el usuario confirma la salida al ingresar una entrada vacía y pulsar <ENTER>.
        
        5. Finalmente, se limpia la pantalla, el programa se despide con el mensaje "\n\nBye, bye...\n\n" y termina.
    """
    # TODO: Corrige los errores y haz que el main funcione correctamente...

    decimales = 2
    resultado = 0.0
    desea_salir = False

    while not desea_salir:

        if resultado == None:
            entrada = pedir_entrada(f"\t (Cálculo = 0.0) >> ")
        else:
            entrada = pedir_entrada(f"\t (Cálculo = {round(float(resultado), decimales)}) >> ")

        if entrada == "":
            salir = pedir_entrada("¿Desea salir de la calculadora? (s/n) ")
            if salir == 's':
                desea_salir = True
        elif entrada == "lista":
            lista = obtener_operaciones()
            print(lista)
            pausa()
        elif entrada == "ce":
            resultado = 0.0
        elif entrada.startswith("decimales"):
            # Extraemos las posiciones decimales y las convertimos a un valor entero
            decimales = str(entrada.split()[1])
            decimales = int(decimales)
            print(f"Decimales configurados a {decimales}.")
            pausa()
        elif entrada == "calculo":
            resultado = realizar_calculo(decimales, resultado)
        else:
            mostrar_error(4)
            pausa()

    limpiar_pantalla()
    print("\n\nBye, bye...\n\n")


if __name__ == '__main__':
    main()
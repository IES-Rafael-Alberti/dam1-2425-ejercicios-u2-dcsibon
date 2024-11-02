# ATENCIÓN!!!
# Importar los paquetes necesarios
# NO usar print de los errores en nigún sitio, SIEMPRE llamar a la función mostrar_error
# En comentarios internos tenéis ayuda para guiaros en la resolución de esta práctica.
# CADA función SOLO puede tener una instrucción return


# Mensajes de error predefinidos
import os


MENSAJES_ERROR = (
    "Problemas al intentar limpiar la pantalla {error}",
    "Error al configurar los decimales. Formato: decimales <n>.",
    "Entrada no válida. Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo.",
    "Error: Introduzca un operador antes de otro número.",
    "Comando no reconocido. Escriba 'lista' para ver las operaciones disponibles.",
)

# Operadores soportados por la calculadora
OPERADORES = "+-x*/:"


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    """
    # El desarrollo de esta función está incompleto y con errores...
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
    except Exception as e:
        mostrar_error(0)


def pausa():
    """
    Pausa la ejecución del programa hasta que se pulse ENTER... "\nPresione ENTER para continuar..."
    """
    # El desarrollo de esta sin realizar... ver documentación. 
    input("\nPresione ENTER para continuar...")


def mostrar_error(indice_error: int, msj_error = None):
    """
    Muestra un mensaje de error en la consola.
    
    Args:
        indice_error (int): Índice del mensaje de error en MENSAJES_ERROR.
        msj_error (str, opcional): Texto adicional para personalizar el mensaje de error.
    """
    # Completa el código de esta función para que controle específicamente las excepciones IndexError y 
    # muestre el mensaje: "\n*ERROR* Mensaje de error no definido.\n"
    # También se pide que se controle cualquier otra excepción que se pueda producir y muestr el mensaje:
    # "\n*ERROR* Problemas al mostrar error!\n{e}\n"
    try:
        if msj_error != None:
            print(f"\n*ERROR* {MENSAJES_ERROR[indice_error].format(error = msj_error)}\n")
        else:
            print(f"\n*ERROR* {MENSAJES_ERROR[indice_error]}\n")
    except IndexError:
        print("\n*ERROR* Mensaje de error no definido.\n")
    except Exception as e:
        print(f"\n*ERROR* Problemas al mostrar error!\n{e}\n")


def sumar(num1: float, num2: float) -> float:
    """
    Suma dos números y retorna el resultado

    Agrs:
        num1 (float): primero número a sumar
        num2 (float): segundo número a sumar

    Returns:
        (float): resultado de la suma de num1 y num2
    """
    # Desarrollo completo, incluida la documentación... recibe 2 números float y retorna la suma de ambos
    return num1 + num2


def restar(num1: float, num2: float) -> float:
    """
    Resta dos números y retorna el resultado

    Agrs:
        num1 (float): primero número a sumar
        num2 (float): segundo número a sumar

    Returns:
        (float): resultado de la resta de num1 y num2
    """    
    # Desarrollo completo, incluida la documentación... recibe 2 números float y retorna la resta de ambos
    return num1 - num2
    


def es_resultado_negativo(num1: float, num2: float) -> bool:
    """Determina si el resultado de una operación entre num1 y num2 debe ser negativo."""
    # El desarrollo de esta sin realizar y debe cumplirse la documentación y debe pasar las pruebas unitarias.


def multiplicar():
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
    # El desarrollo de esta sin realizar y debe cumplirse la documentación y debe pasar las pruebas unitarias.
    # OBLIGATORIO usar un bucle for




def dividir():
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
    # El desarrollo de esta sin realizar y debe cumplirse la documentación y debe pasar las pruebas unitarias.
    


def potencia():
    # El desarrollo de esta sin realizar y tampoco la documentación.
    # PREMISAS a tener en cuenta:
    # - Cualquier número elevado a 0 da como resultado 1.
    # - Para simplificar esta práctica vamos a suponer que un número elevado a un 
    #   exponente negativo siempre dará 0 (aunque en realidad no es así matemáticamente)


def pedir_entrada(msj: str) -> str:
    """
    Pide al usuario una entrada, elimina espacios por delante y por detrás y la convierte a minúsculas.
    
    Args:
        msj (str): Mensaje para solicitar la entrada.
    
    Returns:
        str: Entrada del usuario.
    """
    # El desarrollo de esta función está incompleto... leer documentación
    return input(msj)


def calcular_operacion(num1: float, num2: float, operador: str) -> float:
    # Crear la documentación que está incompleta...
    # El desarrollo de esta función está incompleto... realiza las llamadas adecuadas a las 
    # funciones ya creadas para realizar los distintos cálculos.

    return resultado


def obtener_operaciones() -> str:
    """Devuelve una cadena con la lista de operaciones disponibles en la calculadora."""
    # El desarrollo de esta función está incompleto
    """
    Operaciones disponibles:
      ce => Reiniciar resultado a 0
      decimales <n> => Establecer decimales en resultado
      cadena vacía + <ENTER> => Pregunta si desea salir
      calculo => Iniciar cálculo secuencial
          + => Suma
          - => Resta
          x o * => Multiplicación
          / o : => División
          ** exp => Potencia
          cancelar => vovler sin actualizar resultado de la calculadora
          cadena vacía + <ENTER> => volver actualizando resultado de la calculadora
    """


def realizar_calculo():
    """
    Realiza una secuencia de cálculos solicitando números y operadores al usuario.
    
    Args:
        decimales (int): Número de decimales para el resultado.
        resultado_almacenado (float): Valor almacenado en la calculadora.
    
    Returns:
        float: Resultado final del cálculo o None si se cancela.

    Note:
        * El usuario es guiado para introducir números y operadores secuencialmente para realizar operaciones básicas.
        * El usuario puede utilizar "resultado" en la secuencia de cálculo para reutilizar el resultado almacenado en la calculadora.
        * El cálculo finaliza al pulsar <ENTER>, volviendo y actualizando el resultado almacenado de la calculadora con el cálculo realizado.
        * También podemos escribir "cancelar", volviendo sin realizar ningún cambio en el resultado almacenado de la calculadora.    
    """
    # El desarrollo de esta función está incompleto... ver documentación para solucionarlo.

    operador = None
    resultado = None
    realizando_calculo = True

    print("\n## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##\n")

    while realizando_calculo:
        entrada = pedir_entrada(f"\t (Cálculo = {resultado if resultado is not None else 0}) >> ")
        
        if entrada == "cancelar":


        elif entrada == "":


        elif entrada in OPERADORES:


        else:
            if entrada == "resultado":
                entrada = resultado_almacenado

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
        
        5. Finalmente, se limpia la pantalla, el programa se despide y termina.
    """
    # Corrige los errores y haz que el main funcione correctamente...

    #
    # Agregar una NUEVA FUNCIONALIDAD a la calculadora: el cálculo del exponente
    #

    decimales = 2
    resultado = 0.0
    desea_salir = True

    while not desea_salir:
        print("### CALCULADORA ###\n    -----------\n\n")

        pedir_entrada(f"Operación (RES => resultado) >> ")

        if entrada == "":
            desea_salir = pedir_entrada("¿Desea salir de la calculadora? (s/n) ") == "S"

        elif entrada == "lista":
            obtener_operaciones()

        elif entrada == "ce":
            resultado = 0

        elif entrada.startswith("decimales"):
            try:
                decimales = int(entrada.split()[1])
                print(f"Decimales configurados a {decimales}.")
            except
                mostrar_error
            
            pausa()                

        elif entrada == "calculo":
            realizar_calculo(decimales, resultado)

            pausa()

        else:
            mostrar_error
            pausa()

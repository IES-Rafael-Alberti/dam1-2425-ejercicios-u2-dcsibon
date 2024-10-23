'''
Adivina el numero

Este algoritmo genera un numero aleatorio y comprueba si el usuario es capaz de adivinarlo,
para ello tiene 5 intentos. El algoritmo da pistas en funcion de si esta por encima o por
abajo del numero

Funciones disponibles:
    * modo_dificultad - selecciona la dificultad que tendra el juego
    * generar_numero_random - genera el numero a adivinar por el usuario 
    * pedir_num - pide el numero al usuario 
    * comprobar_num - comprueba que el numero sea valido (entero y en el rango de 0-100)
    * comprobar_acierto - comprueba si el usuario a acertado el numero 
    * calcular_diferencia - calcula la diferencia absoluta entre los dos numeros 
    * comparar_nums - compara cual de los dos numeros es mayor para calcular la diferencia
    absoluta
    * frio_caliente - da pistas al usuario sobre si esta cerca por arriba o por abajo del 
    numero a adivinar
    * main - funcion main

'''
import random

MENSAJE_INICIAL = '''
****************************************
*** ¡Bienvenido a Adivina el Numero! ***
****************************************
¿Que tan habil seras?
¿Conseguiras los 180 puntos?
'''

MENSAJES_INTENTOS = ('Primer intento', 'Segundo intento', 'Tercer intento', 'Cuarto intento', 
'Quinto intento', 'Sexto intento', 'Septimo intento')

def modo_dificultad() -> tuple: 
    '''
    Selecciona el modo de dificultad que tendra el juego

    Returns:
        tuple: El numero de intentos y el rango hasta el cual
        generar el numero aleatorio
    
    '''
    dificultad = input('Facil(1)\nMedio(2)\nDificil(3)\nSelecciona la dificultad: ')

    while dificultad not in ('1', '2', '3'):
        dificultad = input('**DIFICULTAD NO VALIDA**\nFacil(1)\nMedio(2)\nDificil(3)\nSelecciona la dificultad: ')

    # El primer valor son los intentos y el segundo el rango
    if dificultad == '1':
        return 7, 50
    elif dificultad == '2':
        return 5, 100
    else:
        return 3, 200


def generar_numero_random(dificultad: tuple) -> int:
    '''

    Genera un numero aleatorio

    Args: 
        dificultad (tuple): En funcion de la dificultad el rango del numero
        a generar sera mayor o menor

    Returns:
        int: Devuelve un numero aleatorio entre 0 y 100
    
    '''
    
    return random.randint(0, dificultad[1])


def pedir_num(dificultad: tuple) -> int:
    ''' 
    
    Pide un numero al usuario

    Args:
        dificultad (tuple): Dificultad del juego

    Returns:
        int: Devuelve un numero introducido por el usuario

    '''
    num = input(f'¡Prueba suerte! Introduce un numero entre 0 y {dificultad[1]}: ')
    print()
    while not comprobar_num(num, dificultad):
        num = input(f'ERROR, introduce un numero entre 0 y {dificultad[1]}: ')
        print()
    return int(num)


def comprobar_num(num: str, dificultad: tuple) -> bool:
    '''
    
    Comprueba que el numero introduce sea un numero entero y que este
    en el rango de 0-100
    
    Args: 
        num (str): Numero que introduce el usuario
        dificultad (tuple): Dificultad del juego

    Returns: 
        bool: Retorna True si es un numero y False si no lo es 

    '''
    num = num.strip()

    if num.isdigit():
        num = int(num)

        if 0 <= num <= dificultad[1]:
            return True
        else:
            return False
    else:
        return False


def comprobar_acierto(numA: int, numU: int) -> bool:
    '''
    
    Comprueba que el numero aleatorio y el introducido por el usuario
    sean iguales

    Args:
        numA (int): Numero aleatorio generado
        numU (int): Numero introducido por el usuario

    Returns:
        bool: Retorna True si son iguales y False si no

    '''
    return numA == numU


def calcular_diferencia(numA: int, numU: int) -> int:
    '''
    
    Calcula el valor absoluto de la diferencia entre el numero a 
    adivinar y el numero introducido por el usuario

    Args:
        numA (int): Numero aleatorio generado
        numU (int): Numero introducido por el usuario

    Returns:
        int: La diferencia absoluta entre los dos numeros
    
    '''
    return abs(numA - numU)


def numero_oculto_es_mayor(numA: int, numU: int) -> bool:
    '''
    
    Compara que numero es mayor de los dos

    Args:
        numA (int): Numero aleatorio generado
        numU (int): Numero introducido por el usuario

    Returns:
        bool: Retorna True si el numero a adivinar es mayor y
        False si no
    
    '''
    return numA > numU


def frio_caliente(numA: int, numU: int, diferencia: int) -> str:
    '''

    En funcion de la diferencia entre los numeros y de cual es mayor
    da pistas sobre que tan cerca esta y si tiene que aumentar o
    disminuir el numero introducido

    Args:
        numA (int): Numero aleatorio generado
        numU (int): Numero introducido por el usuario
        diferencia (int): Diferencia entre ambos numeros

    Returns:
        str: Retorna una pista

    '''
    if numero_oculto_es_mayor(numA, numU):

        if diferencia < 5:
            return 'TE VAS A QUEMAAR!!! Sube un poquito'
        elif diferencia < 10:
            return 'Estás a punto de quemarte, aumenta.'
        elif diferencia < 30:
            return 'Caliente, caliente, sigue subiendo'
        elif diferencia < 50:
            return 'Hace un poco de frío por aquí. Tiene que subir.'
        elif diferencia < 70:
            return 'No sabía que estabamos en Noruega. Aumenta más.' 
        elif diferencia < 100:
            return 'Acabo de ver pasar un pingüino. Sube, sube.'
        elif diferencia < 150:
            return '¿Que hace aqui Papa Noel? Ve subiendo.'
        else:
            return 'Que frío, parece que estamos en la carnicería del Makro. Tienes que aumentar.'
    
    else:
        if diferencia < 5:
            return 'TE VAS A QUEMAAR!!! Baja un poquito'
        elif diferencia < 10:
            return 'Estás a punto de quemarte, disminuye.'
        elif diferencia < 30:
            return 'Caliente, caliente, sigue bajando'
        elif diferencia < 50:
            return 'Hace un poco de frío por aquí. Tiene que bajar.'
        elif diferencia < 70:
            return 'No sabía que estabamos en Noruega. Disminuye más.' 
        elif diferencia < 100:
            return 'Acabo de ver pasar un pingüino. Baja, baja.'
        elif diferencia < 150:
            return '¿Que hace aqui Papa Noel? Ve bajando.'
        else:
            return 'Que frío, parece que estamos en la carniceria del Makro. Tienes que bajar.'


def generar_pista(num_a_adivinar: int, num_usuario: int) -> str:
    '''
    Genera una pista

    Args:
        num_a_adivinar (int): Numero que debe adivinar el usuario
        num_usuario (int): Numero del usuario

    Returns:
        str: Retorna una cadena de caracteres con una pista
    
    '''
    diferencia = calcular_diferencia(num_a_adivinar, num_usuario)
    pista = frio_caliente(num_a_adivinar, num_usuario, diferencia)
    return pista


def main():
    '''
    
    Funcion main

    DCS:

    1. Separa los valores que recibes de la función modo_dificultad en total_intentos (que ya la tienes) y rango_maximo (entiendo que el mínimo siempre es 0).
    2. Modifica la función generar_numero_random para que reciba ahora dos valores diferentes en vez de una tupla.
    3. Usa una constante que se llame por ejemplo RANGO_MINIMO para darle valor al mínimo valor posible del número oculto.
    4. Modifica el resto de funciones que usan solo un valor de la tupla dificultad por una variable con más significado, como pedir_num, frio_caliente, comprobar_num...
    5. Usa pedir_num dentro de la función modo_dificultad() y deja que la única responsabilidad de modo_dificultad sea la de gestionar la selección de la dificultad 1, 2 o 3.

    '''
    print(MENSAJE_INICIAL)

    dificultad = modo_dificultad()
    
    num_a_adivinar = generar_numero_random(dificultad)
    print(num_a_adivinar)

    total_intentos = dificultad[0]
    intento = 0
    acertaste = False
    print(f'\nIntenta adivinar el numero, tienes {total_intentos} intentos\n')

    while (not acertaste) and (intento < total_intentos):

        print(MENSAJES_INTENTOS[intento] + "...\n")

        num_usuario = pedir_num(dificultad)
        acertaste = comprobar_acierto(num_a_adivinar, num_usuario)
        intento += 1

        if acertaste:
            print(f'\nFelicidades! El numero a adivinar era el {num_a_adivinar}.')
            puntaje = int((100 - intento * 10) * (dificultad[1]/100))
            print(f'Obtuviste: {puntaje} puntos, enhorabuena.')
        elif intento < total_intentos:
            print(generar_pista(num_a_adivinar, num_usuario) + "\n")

    if not acertaste:
        print(f'Mala suerte no lo lograste. El numero a adivinar era el {num_a_adivinar}.')


if __name__ == '__main__':
    main()
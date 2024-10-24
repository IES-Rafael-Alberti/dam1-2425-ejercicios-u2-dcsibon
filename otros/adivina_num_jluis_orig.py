'''
Adivina el numero

Este algoritmo genera un numero aleatorio y comprueba si el usuario es capaz de adivinarlo,
para ello tiene 5 intentos. El algoritmo da pistas en funcion de si esta por encima o por
abajo del numero

Funciones disponibles:
    * generar_numero_random - genera el numero a adivinar por el usuario 
    * pedir_num - pide el numero al usuario 
    * comprobar_num - comprueba que el numero sea valido (entero y en el rango de 0-100)
    * comprobar_acierto - comprueba si el usuario a acertado el numero 
    * calcular_diferencia - calcula la diferencia absoluta entre los dos numeros 
    * comparar_nums - compara cual de los dos numeros es mayor para calcular la diferencia
    absoluta
    * frio_caliente - da pistas al usuario sobre si esta cerca por arriba o por abajo del 
    numero a adivinar

'''
import random

def generar_numero_random() -> int:
    '''

    Genera un numero aleatorio

    Returns:
        int: Devuelve un numero aleatorio entre 0 y 100
    
    '''
    return random.randint(0, 100)

def pedir_num() -> int:
    ''' 
    
    Pide un numero al usuario

    Returns:
        int: Devuelve un numero introducido por el usuario

    '''
    num = input('¡Prueba suerte! Introduce un numero entre 0 y 100: ')
    print()
    while not comprobar_num(num):
        num = input('ERROR, introduce un numero entre 0 y 100: ')
        print()
    return int(num)

def comprobar_num(num: str) -> bool:
    '''
    
    Comprueba que el numero introduce sea un numero entero y que este
    en el rango de 0-100
    
    Args: 
        num (str): Numero que introduce el usuario

    Returns: 
        bool: Retorna True si es un numero y False si no lo es 

    '''
    num = num.strip()

    if num.isdigit():
        num = int(num)

        if 0 <= num <= 100:
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
    if comparar_nums(numA, numU) is True:
        diferencia = abs(numA - numU)
    else:
        diferencia = abs(numU - numA)
    return diferencia

def comparar_nums(numA: int, numU: int) -> bool:
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

    Returns:
        str: Retorna una pista

    '''

    if comparar_nums(numA, numU) is True:

        if diferencia < 5:
            return 'TE VAS A QUEMAAR!!! Sube un poquito'
        elif diferencia < 10:
            return 'Estas a punto de quemarte, aumenta.'
        elif diferencia < 30:
            return 'Caliente, caliente, sigue subiendo'
        elif diferencia < 50:
            return 'Hace un poco de frio por aqui. Tiene que subir.'
        elif diferencia < 70:
            return 'No sabia que estabamos en Noruega. Aumenta mas.' 
        else:
            return 'Que frio, parece que estamos en la carniceria del Makro. Tienes que aumentar.'
    
    else:
        if diferencia < 5:
            return 'TE VAS A QUEMAAR!!! Baja un poquito'
        elif diferencia < 10:
            return 'Estas a punto de quemarte, disminuye.'
        elif diferencia < 30:
            return 'Caliente, caliente, sigue bajando'
        elif diferencia < 50:
            return 'Hace un poco de frio por aqui. Tiene que bajar.'
        elif diferencia < 70:
            return 'No sabia que estabamos en Noruega. Disminuye mas.' 
        else:
            return 'Que frio, parece que estamos en la carniceria del Makro. Tienes que bajar.'


def main():
    '''
    
    Funcion main
    
    '''
    print('\nIntenta adivinar el numero, tienes 5 intentos\nPrimer intento\n')

    num_a_adivinar = generar_numero_random()
    num_usuario = pedir_num()
    comprobacion = False
    mensajes = ['Segundo intento.', 'Tercer intento.','Cuarto intento', 'Ultimo intento.']

    
    for i in range (0,4):

        if comprobacion is False:
            print(mensajes[i])
            diferencia = calcular_diferencia(num_a_adivinar, num_usuario)
            pista = frio_caliente(num_a_adivinar, num_usuario, diferencia)
            print(pista)
            print()
            num_usuario = pedir_num()
            comprobacion = comprobar_acierto(num_a_adivinar, num_usuario)

        else:
            print(f'\nFelicidades! El numero a adivinar era {num_a_adivinar}.')

    if comprobacion is False:
        print('Mala suerte no lo lograste.')

if __name__ == '__main__':
    main()
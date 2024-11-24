import os
import random


CONFIG = {
    "bombo": {"min": 1, "max": 50, "total": 5},
    "estrellas": {"min": 1, "max": 12, "total": 2}
}


def mostrar_error(msj):
    print(msj)

def pausa(msj):
    """
    Realiza una pausa hasta que se pulse ENTER.
    Args:
    msj: mensaje introducido por el usuario.
    """
    input(f"\n {msj}")


def limpiar_pantalla():
    """
    Limpia la consola.
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")



def obtener_aciertos(numeros :set, numeros_premiados: set)->int:
    """
    Realiza una intersección entre el conjunto de números introducidos por el usuario y el conjunto de números generados de forma aleatoria, y saca los números que coinciden en los dos conjuntos.
    Args:
    numeros(set):números introducidos por el usuario.
    numeros_premiados(set): números generados de manera aleatoria.
    Returns:
    Número de aciertos.
    """
    aciertos = numeros.intersection(numeros_premiados)
    numero_aciertos = len(aciertos) #cuenta cada elemento del conjunto para sacar el número de aciertos.
    return numero_aciertos



def preguntar_total(desc: str, min: int)-> int:
    """
    Pregunta al usuario cuál será el total de números a apostar.
    Args:
    desc: descripción "estrellas" o "numeros".
    min: número mínimo dentro del rango.
    Returns:
    Número total.
    """
    max = min * 2
    return pedir_numero(f"Total de {desc} a jugar ({min}-{max})?>> ",min,max)
            
    
def sacar_bolas (min: int, max: int, total: int)->set:
    """
    Retorna un conjunto aleatorio dentro de un mínimo, un máximo y un total de números.
    Args:
    min: número mínimo dentro del rango.
    max: número máximo dentro del rango.
    total: total de números que genera el conjunto.
    Returns:
    Conjunto de números generados de manera aleatoria.
    """
    bolas = range(min, max + 1)

    return random.sample(bolas,total)



def generar_euromillon(premiados: set, estrellas: set):
    """
    Genera los números y estrellas premiados para el sorteo del Euromillón.

    Args:
        premiados (set): Conjunto donde se almacenarán los números premiados.
        estrellas (set): Conjunto donde se almacenarán las estrellas premiadas.
    """
    premiados.update(sacar_bolas(CONFIG["bombo"]["min"], CONFIG["bombo"]["max"], CONFIG["bombo"]["total"]))

    estrellas.update(sacar_bolas(CONFIG["estrellas"]["min"], CONFIG["estrellas"]["max"], CONFIG["estrellas"]["total"]))     

def pedir_numero(msj: str,min :int ,max: int)->int:
    """
    Pide números al usuario y lo retorna.
    Args:
    msj: mensaje introducido por el usuario.
    min: número mínimo dentro del rango.
    max: número máximo dentro del rango.
    Returns:
    número introducido por el usuario.
    """
    numero_correcto = False

    while not numero_correcto:
        try:
            numero = int(input(msj))

            if numero < min or numero > max:
                raise ValueError("ERROR, Introduce un número dentro del rango válido.")
            numero_correcto = True
        except ValueError as e:
            mostrar_error(e)
        except Exception:
            mostrar_error(e)

    return numero


def solicitar_numeros(desc: str, total: int, min: int, max: int)->set:
    """
    Pide números al usuario llamando a la función "pedir_número" y los añade a un conjunto.
    Args:
    desc: descripción "estrellas" o "numeros".
    total: total de números que tendrá el conjunto.
    min: número mínimo dentro del rango.
    max: número máximo dentro del rango.
    Returns:
    conjunto de números introducidos por el usuario.
    """
    conj_numeros = set()

    while len(conj_numeros) < total:
        numero = pedir_numero(f"Dame {desc} #{len(conj_numeros) + 1}#>> ", min, max)

        conj_numeros.add(numero)
        lista_numeros = list(conj_numeros)
        lista_numeros.sort()

        print(lista_numeros)

    # O también así...
    #
    # conj_numeros = set()
    #
    # while len(conj_numeros) < total:
    #     conj_numeros.add(pedir_numero(f"Dame {desc} #{len(conj_numeros) + 1}#>> ", min, max))
    #
    #     print(f"{sorted(conj_numeros)}")

    return conj_numeros



def mostrar_resultados(aciertos_numeros: int, aciertos_estrellas: int,premiados: set,estrellas: set,numeros_jugados: set,estrellas_jugadas: set):
    """
    Muestra los resultados del euromillón. 
    Args:
    aciertos_numeros (set): número de aciertos.
    aciertos_estrellas(set): número de aciertos de estrellas.
    premiados(set): conjunto de números generados al azar.
    estrellas(set): conjunto de estrellas generadas al azar.
    numeros_jugados(set): conjunto de números introducidos por el usuario.
    estrellas_jugadas(set): conjunto de estrellas(números) introducidas por el usuario.
    """
    print("RESULTDOS DEL EUROMILLÓN\n------------")

    print(f"Números premiados {premiados}\n Estrellas premiadas = {estrellas}\n")

    print(f"Números jugados = {numeros_jugados}\n Estrellas jugadas = {estrellas_jugadas}\n")

    print(f"Total de números acertados = {aciertos_numeros}\n Total de estrellas acertadas = {aciertos_estrellas}")


def main():
    premiados = set()
    estrellas = set()
    limpiar_pantalla()
    print("JUEGA AL EUROMILLÓN\n -------------")
    total_numeros = preguntar_total("números", CONFIG["bombo"]["total"])

    total_estrellas = preguntar_total("estrellas", CONFIG["estrellas"]["total"])

    pausa("Pulsa ENTER para continuar...")
    limpiar_pantalla()

    print(f"\n### Seleccione {total_numeros} números del {CONFIG["bombo"]["min"]} al {CONFIG["bombo"]["max"]} ###")
    numeros_jugados = solicitar_numeros("el número", total_numeros, CONFIG["bombo"]["min"], CONFIG["bombo"]["max"])

    print(f"\n### Seleccione {total_estrellas} estrellas del {CONFIG["estrellas"]["min"]} al {CONFIG["estrellas"]["max"]} ###")
    estrellas_jugadas = solicitar_numeros("la estrella", total_estrellas, CONFIG["estrellas"]["min"], CONFIG["estrellas"]["max"])

    pausa("Pulsa ENTER para ver el resultado del EUROMILLÓN... (si ganas me invitas a gambas)")

    limpiar_pantalla()

    generar_euromillon(premiados,estrellas)
    
    aciertos_numeros = obtener_aciertos(numeros_jugados,premiados)

    aciertos_estrellas = obtener_aciertos(estrellas_jugadas,estrellas)
    
    mostrar_resultados(aciertos_numeros,aciertos_estrellas,premiados,estrellas,numeros_jugados,estrellas_jugadas)



if __name__ == "__main__":
    main()
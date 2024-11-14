
import os
import random


BOMBO_MIN = 1
BOMBO_MAX = 50
BOMBO_TOTAL = 5

ESTRELLAS_MIN = 1
ESTRELLAS_MAX = 12
ESTRELLAS_TOTAL = 2

BOMBO = tuple(range(BOMBO_MIN, BOMBO_MAX + 1))
ESTRELLAS = tuple(range(ESTRELLAS_MIN, ESTRELLAS_MAX + 1))


def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')


def pausa():
    input("\nPresione ENTER para continuar...")


def pedir_numero(msj: str, minimo: int, maximo: int) -> int:
    numero = None
    while numero is None:
        try:
            numero = int(input(msj).strip())

            if not (minimo <= numero <= maximo):
                raise ValueError(f"El número debe estar entre el {minimo} y el {maximo}!")
            
        except ValueError as e:
            if numero is None:
                print("*ERROR* Número no válido!")
            else:
                numero = None
                print(f"*ERROR* {e}")

    return numero


def solicitar_numeros(desc: str, total: int, min: int, max: int) -> set:
    numeros = set()
    while len(numeros) < total:
        numeros.add(pedir_numero(f"{list(numeros) if len(numeros) > 0 else []} Dame {desc} #{len(numeros) + 1}#>> ", min, max))

    return numeros


def preguntar_total(desc: str, min: int) -> int:
    max = min * 2
    return pedir_numero(f"Total de {desc} a jugar ({min}-{max})? >> ", min, max)


def sacar_bolas(bombo: tuple, total: int) -> set:
    return set(random.sample(bombo, total))


def generar_euromillon(premiados: set, estrellas: set):
    premiados.update(sacar_bolas(BOMBO, BOMBO_TOTAL))
    estrellas.update(sacar_bolas(ESTRELLAS, ESTRELLAS_TOTAL))
    

def obtener_aciertos(jugados: set, premiados: set) -> int:
    # Cuenta los aciertos mediante la intersección de conjuntos
    return len(jugados & premiados)


def mostrar_resultados(numeros_premiados: set, 
                       estrellas_premiadas: set, 
                       numeros: set, 
                       estrellas: set, 
                       aciertos_numeros: int, 
                       aciertos_estrellas: int):
    limpiar_pantalla()
    print("RESULTADOS DEL EUROMILLÓN\n-------------------------\n\n")

    print(f"Números premiados = {sorted(numeros_premiados)}")
    print(f"Estrellas premiadas = {sorted(estrellas_premiadas)}")
    
    print(f"Números jugados = {sorted(numeros)}")
    print(f"Estrellas jugadas = {sorted(estrellas)}")

    # Comprobar el los números...
    aciertos_numeros = obtener_aciertos(numeros, numeros_premiados)
    aciertos_estrellas = obtener_aciertos(estrellas, estrellas_premiadas)

    print("\n\nTotal de números acertados = " + 
          f"{aciertos_numeros}\n" + 
          "Total de estrellas acertadas = " + 
          f"{aciertos_estrellas}")


def main():
    limpiar_pantalla()
    print("JUEGA AL EUROMILLÓN\n-------------------\n\n")

    # Preguntar cuantos números y estrellas puede el jugador introducir...
    total_numeros = preguntar_total("números", BOMBO_TOTAL)
    total_estrellas = preguntar_total("estrellas", ESTRELLAS_TOTAL)

    # Pedir los números y estrellas del euromillón...
    print(f"\n### Seleccione {total_numeros} números del {BOMBO_MIN} al {BOMBO_MAX} ###")
    numeros = solicitar_numeros("el número", total_numeros, BOMBO_MIN, BOMBO_MAX)
    print(f"\n### Seleccione {total_numeros} estrellas del {ESTRELLAS_MIN} al {ESTRELLAS_MAX} ###")
    estrellas = solicitar_numeros("la estrella", total_estrellas, ESTRELLAS_MIN, ESTRELLAS_MAX)

    # Sacar de los bombos los números y las estrellas premiadas...
    numeros_premiados = set()
    estrellas_premiadas = set()
    generar_euromillon(numeros_premiados, estrellas_premiadas)
    
    mostrar_resultados(numeros_premiados, estrellas_premiadas, numeros, estrellas)


if __name__ == "__main__":
    main()
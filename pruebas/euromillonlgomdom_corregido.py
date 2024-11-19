import os
import random


CONFIG = {
    "bombo": {
        "min": 1,
        "max": 50,
        "total": 5
    },
    "estrellas": {
        "min": 1,
        "max": 12,
        "total": 2
    },
}


def limpiar_pantalla():
    """
    Limpia pantalla independientemente del S.O
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def pausa():
    """
    Función que detiene el programa hasta pulsar ENTER
    """
    input("Pulsa ENTER para continuar...")


def solicitar_numeros(desc: str, total: int, min: int, max: int):
    vuelta = 1
    listanum = set()

    while vuelta <= total:
        numero = pedir_numero(f"Dame {desc} #{vuelta}#>> ", min, max)
        listanum.add(numero)
        print(sorted(listanum))
        vuelta += 1

    return listanum


def pedir_numero(msj:str,min:int,max:int):
    """
    Función que comprueba que el número está dentro del rango y no está repetido.
    """
    salir = False

    while salir == False:
        total = input(msj)

        try:
            total = int(total)
            if total < min or total > max:
                print(f"*ERROR* el número debe estar entre el {min} y el {max}")
            else:
                return total
            
        except ValueError:
            print("*ERROR* Número no válido")


def sacar_bolas(min: int, max: int, total: int):
    vuelta = 1
    bolas = set()

    while vuelta <= total:
        num = random.randint(min, max)
        bolas.add(num)
        vuelta += 1

    return bolas


def obtener_aciertos(numeros: set, numeros_premiados: set):
    aciertos = numeros & numeros_premiados
    totalaciertos = 0

    for numero in aciertos:
        totalaciertos += 1

    return totalaciertos


def preguntar_total(desc: str, min: int):
    max = min * 2
    total = pedir_numero(f"Total de {desc} a jugar ({min}-{max})? >> ", min, max)
    return total


def mostrar_resultados(numeros_premiados: set, 
                       estrellas_premiadas: set, 
                       numeros: set, 
                       estrellas: set):
    """
    Función que retorna una cadena de caracteres

    Args:
    Almacena en una variable la cadena de caracteres
    Returns:
    Retorna la cadena de caracteres con todos los resultados del flujo del programa que estan almacenados en la variable.
    """
    """
    resultados = f"RESULTADOS EUROMILLÓN\n-------------------------\n\n\nNúmeros premiados = {sorted(numeros_premiados)}\nEstrellas premiadas = {sorted(estrellas_premiadas)}\nNúmeros jugados = {sorted(numeros)}\nEstrellas jugadas = {sorted(estrellas)}\n\n\nTotal de números acertados = {aciertos_numeros}\nTotal de estrellas acertadas = {aciertos_estrellas}"
    
    return resultados
    """
    limpiar_pantalla()
    print("RESULTADOS DEL EUROMILLÓN\n-------------------------\n\n")

    print(f"Números premiados = {sorted(numeros_premiados)}")
    print(f"Estrellas premiadas = {sorted(estrellas_premiadas)}")
    
    print(f"Números jugados = {sorted(numeros)}")
    print(f"Estrellas jugadas = {sorted(estrellas)}")

    # Comprobar los resultados, obteniendo el número de aciertos que ha tenido...
    aciertos_numeros = obtener_aciertos(numeros, numeros_premiados)
    aciertos_estrellas = obtener_aciertos(estrellas, estrellas_premiadas)

    print("\n\nTotal de números acertados = " + 
          f"{aciertos_numeros}\n" + 
          "Total de estrellas acertadas = " + 
          f"{aciertos_estrellas}")    


def pregunta_desea_continuar() -> bool:
    """
    Pregunta si desea jugar otra partida al Euromillón.

    Returns:
        (bool): Si introduce 's' o 'S' devolverá True, sino False.
    """
    entrada = input("Deseas jugar otra? S/N >>  ").strip().upper()
    return entrada.upper() == "S"


def main():
    salir = False

    while not salir:
        limpiar_pantalla()
        total_numeros = preguntar_total("números", CONFIG["bombo"]["total"])
        total_estrellas = preguntar_total("estrellas", CONFIG["estrellas"]["total"])
        
        print(f"\n### Seleccione {total_numeros} números del {CONFIG["bombo"]["min"]} al {CONFIG["bombo"]["max"]} ###")
        numeros = solicitar_numeros("el número", total_numeros, CONFIG["bombo"]["min"], CONFIG["bombo"]["max"])
        
        print(f"\n### Seleccione {total_estrellas} números del {CONFIG["estrellas"]["min"]} al {CONFIG["estrellas"]["max"]} ###")
        estrellas = solicitar_numeros("el número", total_estrellas, CONFIG["bombo"]["min"], CONFIG["bombo"]["max"])

        numeros_premiados= sacar_bolas(CONFIG["bombo"]["min"],CONFIG["bombo"]["max"],total_numeros)
        estrellas_premiadas= sacar_bolas(CONFIG["estrellas"]["min"],CONFIG["estrellas"]["max"],total_estrellas)

        """
        aciertos_numeros = obtener_aciertos(numeros,numeros_premiados)
        aciertos_estrellas = obtener_aciertos(estrellas,estrellas_premiadas)

        print(mostrar_resultados(numeros_premiados,estrellas_premiadas,numeros,estrellas,aciertos_numeros,aciertos_estrellas))
        """
        mostrar_resultados(numeros_premiados, estrellas_premiadas, numeros, estrellas)

        """
        entrada = input("Deseas jugar otra? S/N >>  ").strip().upper()
        if entrada.upper() == "S":
            salir = False
        else:
            salir = True
        """

        salir = not pregunta_desea_continuar()

    limpiar_pantalla()
    print("¡Adiós! Que la suerte este contigo")



if __name__ =="__main__":
    main()
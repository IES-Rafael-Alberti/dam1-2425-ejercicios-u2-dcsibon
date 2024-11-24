import os
import random


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    """
    os.system('clear' if os.name == 'posix' else 'cls')


def pausa():
    """
    Pausa la ejecución del programa hasta que se pulse ENTER.
    """
    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()


def obtener_descripciones(asignaturas: list) -> str:
    resultado = ""
    for asignatura in asignaturas:
        resultado += f"Yo estudio {asignatura}\n"

    return resultado

def numero_aleatorio() -> int:
    return random.randint(0, 100)

def posicion_aleatoria(min: int, max: int) -> int:
    return random.randint(min, max)

def generar_lista_super_aleatoria() -> list:
    mi_lista = list()
    
    for i in range(10):
        pos = posicion_aleatoria(0, len(mi_lista))
        mi_lista.insert(pos, numero_aleatorio())
    
    return mi_lista


def main():

    limpiar_pantalla()

    conj = {1, 2}
    conj1 = {2, 1}

    print(conj == conj1)

    #print(conj.pop())

    conj2 = {6,1, 1, 1, 5}

    conj.update(conj2)

    for e in conj:
        print(e)

    #conj = set([4, 7, 8, '232'])

    print(conj)





    return

    mi_diccionario = {'uno': 1, 'dos': 2, 'tres': 3}

    mi_diccionario["cuatro"] = 4
    mi_diccionario["cuatro"] = 44

    mi_diccionario.update([("cuatro", 40), ("cinco", 5), ("seis", 6)])

    print(list(mi_diccionario.items()))

    return

    for elemento in mi_diccionario.items():
        print(elemento)

    print(mi_diccionario.items())

    return



    numeros = generar_lista_super_aleatoria()

    print(numeros)

    return

    asignaturas = ("SI", "PR", "BD", "IPE", "ED", "SOS", "DIG", "LM")

    print(obtener_descripciones(asignaturas))

    return




    limpiar_pantalla()

    print(asignaturas)
    pausa()

    for i in range(len(asignaturas)):
        print(asignaturas[i], end="")
        if i == len(asignaturas) - 1:
            print(".")
        else:
            print(end="-")
    
    pausa()



if __name__ == "__main__":
    main()
"""
Ejercicio 2.2.19
Mostrar un menú con tres opciones: 1 - Introduzca una nota, 2 - Imprimir listado, 3 - Finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
"""

from ej2_2_03 import borrarConsola


def mostrarMenu():
    print("MENÚ\n----")
    print("1 - Introduzca una nota\n2 - Imprimir listado\n3 - Finalizar programa")
    print("Seleccione una opción => ", end="")


def comprobarOpcionValida(entrada):
    if entrada.isnumeric() and 1 <= int(entrada) <= 3:
        return True
    else:
        return False
    

def imprimirListado(notas):
    print("Listado de notas")
    print("----------------")
    print(notas)


def leerNota(listado):
    nota = input("Introduzca una nota: ")
    listado += nota + "\n"
    return listado


def main():
    listado = ""

    while True:
        borrarConsola()
        mostrarMenu()
        opcion = input("")

        if comprobarOpcionValida(opcion):
            if opcion == '1':
                borrarConsola()
                listado = leerNota(listado)
            elif opcion == '2':
                borrarConsola()
                imprimirListado(listado)
            else:
                print("Programa finalizado.")
                break

            input("\nPulse <INTRO> para continuar...")


if __name__ == "__main__":
    main()
